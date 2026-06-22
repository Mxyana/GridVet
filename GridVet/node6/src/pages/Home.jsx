import React, { useEffect, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { API } from "../constants/api.js";
import TierBadge from "../components/TierBadge.jsx";
import { BASE_URL } from "../constants/api.js";

const cardStyle = {
  background: "var(--bg-card)",
  border: "1px solid var(--border)",
  borderRadius: 8,
  padding: 24,
};

const inputStyle = {
  width: "100%",
  background: "var(--bg-input)",
  border: "1px solid var(--border)",
  borderRadius: 6,
  padding: "10px 14px",
  color: "var(--text-primary)",
  fontFamily: "Inter, sans-serif",
  fontSize: 14,
  outline: "none",
  transition: "border-color 150ms ease",
};

const labelStyle = {
  display: "block",
  color: "var(--text-secondary)",
  fontFamily: "Inter, sans-serif",
  fontSize: 12,
  marginBottom: 6,
  letterSpacing: "0.02em",
};

const VULN_STATUS_STYLES = {
  RESISTED: {
    label: "Resisted",
    bg: "rgba(34,197,94,0.12)",
    color: "var(--green)",
    border: "rgba(34,197,94,0.3)",
  },
  VULNERABLE: {
    label: "Vulnerable",
    bg: "rgba(239,68,68,0.12)",
    color: "var(--red)",
    border: "rgba(239,68,68,0.3)",
  },
  UNTESTED: {
    label: "Untested",
    bg: "rgba(58,58,58,0.4)",
    color: "var(--text-secondary)",
    border: "var(--border)",
  },
};

const ATTACK_LABELS = {
  goal_hijack: "Goal Hijack",
  false_announcement: "False Announcement",
  wallet_redirect: "Wallet Redirect",
  panic_trigger: "Panic Trigger",
  tool_manipulation: "Tool Manipulation",
};

function tierLabelColor(tier) {
  if (!tier) return "var(--text-secondary)";
  const t = tier.toString().toUpperCase();
  if (t === "S") return "#ffd700";
  if (t === "A") return "#d1d5db";
  if (t === "B") return "#60a5fa";
  return "var(--red)";
}

const TEST_TIERS = [
  { key: "Quick", packets: 10, description: "Fast debugging — 10 packets for rapid iteration." },
  { key: "Standard", packets: 30, description: "Balanced assessment — 30 packets for reliable scoring." },
  { key: "Comprehensive", packets: 50, description: "Final gauntlet — 50 packets for full coverage." },
];

const TEST_MODES = [
  { key: "Practice", description: "Randomised seed — varied results each run." },
  { key: "Benchmark", description: "Fixed seed — deterministic, comparable runs." },
];

export default function Home() {
  const navigate = useNavigate();

  const [agentName, setAgentName] = useState("");
  const [agentEndpoint, setAgentEndpoint] = useState("");
  const [proofDisclaimer, setProofDisclaimer] = useState("");
  const [regStatus, setRegStatus] = useState(null);
  const [registering, setRegistering] = useState(false);
  const [starting, setStarting] = useState(false);

  const [history, setHistory] = useState(null);
  const [historyError, setHistoryError] = useState(false);

  const [testStatus, setTestStatus] = useState("IDLE");
  const [reportData, setReportData] = useState(null);
  const [narrative, setNarrative] = useState("");
  const [cardLoading, setCardLoading] = useState(false);
  const [cardError, setCardError] = useState("");

  const [selectedTier, setSelectedTier] = useState("Standard");
  const [selectedMode, setSelectedMode] = useState("Practice");

  const pollRef = useRef(null);

  // FIX (#3): keep latest agentName accessible from interval callback to avoid stale closure
  const agentNameRef = useRef(agentName);
  useEffect(() => {
    agentNameRef.current = agentName;
  }, [agentName]);

  useEffect(() => {
    try {
      const storedName = sessionStorage.getItem("gridvet_agent_name");
      const storedEp = sessionStorage.getItem("gridvet_agent_endpoint");
      if (storedName) setAgentName(storedName);
      if (storedEp) setAgentEndpoint(storedEp);
    } catch {}

    let cancelled = false;
    (async () => {
      try {
        const res = await fetch(API.TEST_HISTORY, { credentials: 'include' });
        if (!res.ok) throw new Error("bad response");
        const data = await res.json();
        const rows = Array.isArray(data)
          ? data
          : Array.isArray(data?.history)
          ? data.history
          : [];
        if (!cancelled) setHistory(rows);
      } catch (e) {
        if (!cancelled) {
          setHistoryError(true);
          setHistory([]);
        }
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  // FIX (#2): polling extracted so it can be (re)started on every Start Test click
  const startPolling = React.useCallback(() => {
    if (pollRef.current) return; // already polling

    let lastTriggeredFor = null;

    pollRef.current = setInterval(async () => {
      const sessionId = sessionStorage.getItem("gridvet_session_id");
      if (!sessionId) return;

      try {
        // NEW — note: status endpoint also needs the Bearer token; preferred path is
// to call getStatus(sessionId) from api.js. Minimum-change form:
const res = await fetch(API.STATUS(sessionId), {
  credentials: 'include',
  headers: { Authorization: `Bearer ${JSON.parse(sessionStorage.getItem('gridvet_session_tokens') || '{}')[sessionId] || ''}` },
});
        if (!res.ok) throw new Error("bad status");
        const data = await res.json();
        const next = data.status;

        setTestStatus((prev) => (prev !== next ? next : prev));

        if (next === "COMPLETE" || next === "STOPPED") {
          if (lastTriggeredFor !== next) {
            lastTriggeredFor = next;
            if (pollRef.current) {
              clearInterval(pollRef.current);
              pollRef.current = null;
            }
            fetchReportAndGenerate(sessionId);
          }
        } else if (next === "ERROR") {
          if (pollRef.current) {
            clearInterval(pollRef.current);
            pollRef.current = null;
          }
        }
      } catch (err) {
        // Transient network errors — the next tick will retry.
      }
    }, 3000);
  }, []);

  // Start polling on mount in case a test was already in flight (e.g. page refresh)
  useEffect(() => {
    if (sessionStorage.getItem("gridvet_session_id")) {
      startPolling();
    }
    return () => {
      if (pollRef.current) {
        clearInterval(pollRef.current);
        pollRef.current = null;
      }
    };
  }, [startPolling]);

  async function fetchReportAndGenerate(sessionId) {
    if (!sessionId) {
      setCardError("Session missing. Please re-register the agent.");
      return;
    }
    setCardLoading(true);
    setCardError("");
    try {
      const reportRes = await fetch(API.REPORT(sessionId), {
  credentials: 'include',
  headers: { Authorization: `Bearer ${/* same as above */ ''}` },
});
      const report = await getReport(sessionId);
      setReportData(report);
      const cardRes = await fetch(API.GENERATE_REPORT_CARD, {
  method: "POST",
  credentials: "include",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ report, agent_name: agentNameRef.current || "Agent" }),
});
      const cardData = await cardRes.json();
      setNarrative(cardData.narrative || "");
    } catch (err) {
      setCardError("Failed to generate report card.");
    } finally {
      setCardLoading(false);
    }
  }

  async function downloadReport() {
  const sessionId = sessionStorage.getItem("gridvet_session_id");
  if (!sessionId) {
    setCardError("Session missing. Please re-register the agent.");
    return;
  }
  // Pull bearer token the same way api.js does.
  let token = "";
  try {
    token = (JSON.parse(sessionStorage.getItem("gridvet_session_tokens") || "{}"))[sessionId] || "";
  } catch {}
  if (!token) {
    setCardError("Session token missing. Please re-register the agent.");
    return;
  }

  const url = `${BASE_URL}/download-report/${sessionId}?token=${encodeURIComponent(token)}`;
  let res;
  try {
    res = await fetch(url, { credentials: "include" });
  } catch (e) {
    setCardError("Network error while downloading report.");
    return;
  }

  if (res.status === 410) {
    setCardError("This report was already downloaded. Re-run the test to obtain a fresh signed report.");
    setReportData((prev) => prev ? { ...prev, downloaded: true, raw_master_text: null } : prev);
    return;
  }
  if (!res.ok) {
    setCardError(`Download failed: ${res.status}`);
    return;
  }

  const blob = await res.blob();
  const blobUrl = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = blobUrl;
  a.download = `${sessionId}.txt`;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(blobUrl);

  // Lock the UI — second click will 410 anyway.
  setReportData((prev) => prev ? { ...prev, downloaded: true, raw_master_text: null } : prev);
}

  const handleRegister = async () => {
    if (!agentName || !agentEndpoint) {
      setRegStatus({ ok: false, message: "Please fill in both fields." });
      return;
    }
    setRegistering(true);
    setRegStatus(null);
    
    try {
      const res = await fetch(API.REGISTER_AGENT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          agent_name: agentName,
          agent_endpoint: agentEndpoint,
        }),
      });
      if (!res.ok) throw new Error("register failed");

      const data = await res.json();
      if (data.proof_disclaimer) {
  setProofDisclaimer(data.proof_disclaimer);
}

      try {
        sessionStorage.setItem("gridvet_agent_name", agentName);
        sessionStorage.setItem("gridvet_agent_endpoint", agentEndpoint);
        if (data.session_id) {
          sessionStorage.setItem("gridvet_session_id", data.session_id);
        }
      } catch {}

      setRegStatus({ ok: true, message: `Agent registered: ${agentName}` });
    } catch (e) {
      setRegStatus({
        ok: false,
        message: "Failed to connect. Check your endpoint.",
      });
    } finally {
      setRegistering(false);
    }
  };

  const handleStart = async () => {
    const sessionId = sessionStorage.getItem("gridvet_session_id");
    if (!sessionId) {
      alert("No active session found. Please register your agent first.");
      return;
    }

    setStarting(true);
    setReportData(null);
    setNarrative("");
    setCardError("");

    try {
      const token = (JSON.parse(sessionStorage.getItem("gridvet_session_tokens") || "{}"))[sessionId] || "";
      const res = await fetch(API.RUN_TEST, {
        method: "POST",
        credentials: "include",
        headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${token}`,
  },
  body: JSON.stringify({
    tier: selectedTier,
    mode: selectedMode,
    session_id: sessionId,
  }),
});
      // FIX (#4): don't claim RUNNING on a failed request
      if (!res.ok) throw new Error("run failed");
      setTestStatus("RUNNING");
      startPolling(); // FIX (#2): re-arm polling for this run
      navigate("/live");
    } catch (e) {
      console.error("Failed to start test:", e);
      setCardError("Failed to start test. Please try again.");
    } finally {
      setStarting(false);
    }
  };

  return (
    <div style={{ maxWidth: 1200, margin: "0 auto" }}>
      <div style={{ marginBottom: 32 }}>
        <h1
          style={{
            fontFamily: "Inter, sans-serif",
            fontWeight: 600,
            fontSize: 24,
            color: "var(--text-primary)",
            letterSpacing: "-0.01em",
          }}
        >
          Agent Registration
        </h1>
        <p style={{ color: "var(--text-secondary)", fontSize: 14, marginTop: 6 }}>
          Connect your trading agent to the sandbox.
        </p>
      </div>

      <div className="home-grid">
        <div className="home-left">
          {renderRegistrationCard({
            agentName,
            setAgentName,
            agentEndpoint,
            setAgentEndpoint,
            registering,
            handleRegister,
            regStatus,
            proofDisclaimer,
          })}
          {renderRunTestCard({
            starting,
            handleStart,
            selectedTier,
            setSelectedTier,
            selectedMode,
            setSelectedMode,
          })}
          {renderRecentTests({ history, historyError })}
        </div>
        <div className="home-right">
          {renderReportCard({
            agentName,
            agentEndpoint,
            testStatus,
            cardLoading,
            cardError,
            reportData,
            narrative,
            downloadReport,
          })}
        </div>
      </div>

      <style>{`
        .home-grid {
          display: flex;
          gap: 32px;
          align-items: flex-start;
        }
        .home-left {
          flex: 0 0 60%;
          min-width: 0;
        }
        .home-right {
          flex: 0 0 calc(40% - 32px);
          min-width: 0;
          position: sticky;
          top: 0;
        }
        @media (max-width: 768px) {
          .home-grid {
            flex-direction: column;
            gap: 24px;
          }
          .home-left, .home-right {
            flex: 1 1 100%;
            width: 100%;
            position: static;
          }
        }
      `}</style>
    </div>
  );
}

function renderRegistrationCard({
  agentName,
  setAgentName,
  agentEndpoint,
  setAgentEndpoint,
  registering,
  handleRegister,
  regStatus,
  proofDisclaimer,
}) {
  return (
    <div style={{ ...cardStyle, marginBottom: 24 }}>
      <div
        style={{
          color: "var(--text-primary)",
          fontFamily: "Inter, sans-serif",
          fontWeight: 600,
          fontSize: 14,
          paddingBottom: 14,
          borderBottom: "1px solid var(--border-subtle)",
          marginBottom: 18,
        }}
      >
        Register Agent
      </div>

      <div style={{ marginBottom: 14 }}>
        <label style={labelStyle}>Agent Name</label>
        <input
          type="text"
          value={agentName}
          onChange={(e) => setAgentName(e.target.value)}
          placeholder="e.g. My BTC Agent v1"
          style={inputStyle}
          onFocus={(e) => (e.target.style.borderColor = "var(--gold-dim)")}
          onBlur={(e) => (e.target.style.borderColor = "var(--border)")}
        />
      </div>

      <div style={{ marginBottom: 18 }}>
        <label style={labelStyle}>Endpoint URL</label>
        <input
          type="text"
          value={agentEndpoint}
          onChange={(e) => setAgentEndpoint(e.target.value)}
          placeholder="https://your-agent.onrender.com/decide"
          style={inputStyle}
          onFocus={(e) => (e.target.style.borderColor = "var(--gold-dim)")}
          onBlur={(e) => (e.target.style.borderColor = "var(--border)")}
        />
      </div>

      {proofDisclaimer && (
  <div style={{ marginTop: 14, padding: "10px 14px", borderRadius: 6,
                background: "rgba(201,168,76,0.08)",
                border: "1px solid var(--gold-dim)",
                color: "var(--text-secondary)", fontSize: 12,
                fontFamily: "Inter, sans-serif", lineHeight: 1.5 }}>
    {proofDisclaimer}
  </div>
)}

      <button
        onClick={handleRegister}
        disabled={registering}
        className="btn-outline-gold"
      >
        {registering ? "Registering…" : "Register Agent"}
      </button>

      {regStatus && (
        <div
          style={{
            marginTop: 14,
            fontSize: 12,
            color: regStatus.ok ? "var(--green)" : "var(--red)",
            fontFamily: "Inter, sans-serif",
          }}
        >
          {regStatus.ok ? "✓ " : ""}
          {regStatus.message}
        </div>
      )}
    </div>
  );
}

function renderRunTestCard({
  starting,
  handleStart,
  selectedTier,
  setSelectedTier,
  selectedMode,
  setSelectedMode,
}) {
  return (
    <div style={{ ...cardStyle, marginBottom: 40 }}>
      <div
        style={{
          color: "var(--text-primary)",
          fontFamily: "Inter, sans-serif",
          fontWeight: 600,
          fontSize: 14,
          paddingBottom: 14,
          borderBottom: "1px solid var(--border-subtle)",
          marginBottom: 18,
        }}
      >
        Run Test
      </div>

      <p
        style={{
          color: "var(--text-secondary)",
          fontSize: 13,
          lineHeight: 1.55,
          marginBottom: 20,
        }}
      >
        Select a test tier and mode, then start the sandbox pipeline.
        Historical BTC/USDT market data will stream through the
        injection engine and reach your agent.
      </p>

      <div style={{ marginBottom: 20 }}>
        <label style={labelStyle}>Test Tier</label>
        <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
          {TEST_TIERS.map((t) => {
            const isActive = selectedTier === t.key;
            return (
              <div
                key={t.key}
                onClick={() => setSelectedTier(t.key)}
                style={{
                  flex: "1 1 0",
                  minWidth: 140,
                  padding: "14px 16px",
                  borderRadius: 8,
                  border: isActive
                    ? "1.5px solid var(--gold)"
                    : "1px solid var(--border)",
                  background: isActive
                    ? "rgba(201,168,76,0.08)"
                    : "var(--bg-input)",
                  cursor: "pointer",
                  transition: "border-color 150ms ease, background 150ms ease",
                }}
              >
                <div
                  style={{
                    fontFamily: "Inter, sans-serif",
                    fontWeight: 600,
                    fontSize: 14,
                    color: isActive ? "var(--gold)" : "var(--text-primary)",
                    marginBottom: 4,
                  }}
                >
                  {t.key}
                </div>
                <div
                  style={{
                    fontFamily: "'JetBrains Mono', monospace",
                    fontSize: 11,
                    color: isActive ? "var(--gold)" : "var(--text-secondary)",
                    marginBottom: 6,
                  }}
                >
                  {t.packets} packets
                </div>
                <div
                  style={{
                    fontFamily: "Inter, sans-serif",
                    fontSize: 11,
                    color: "var(--text-muted)",
                    lineHeight: 1.4,
                  }}
                >
                  {t.description}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      <div style={{ marginBottom: 24 }}>
        <label style={labelStyle}>Test Mode</label>
        <div style={{ display: "flex", gap: 10 }}>
          {TEST_MODES.map((m) => {
            const isActive = selectedMode === m.key;
            return (
              <div
                key={m.key}
                onClick={() => setSelectedMode(m.key)}
                style={{
                  flex: "1 1 0",
                  padding: "12px 16px",
                  borderRadius: 8,
                  border: isActive
                    ? "1.5px solid var(--gold)"
                    : "1px solid var(--border)",
                  background: isActive
                    ? "rgba(201,168,76,0.08)"
                    : "var(--bg-input)",
                  cursor: "pointer",
                  transition: "border-color 150ms ease, background 150ms ease",
                }}
              >
                <div
                  style={{
                    fontFamily: "Inter, sans-serif",
                    fontWeight: 600,
                    fontSize: 13,
                    color: isActive ? "var(--gold)" : "var(--text-primary)",
                    marginBottom: 4,
                  }}
                >
                  {m.key}
                </div>
                <div
                  style={{
                    fontFamily: "Inter, sans-serif",
                    fontSize: 11,
                    color: "var(--text-muted)",
                    lineHeight: 1.4,
                  }}
                >
                  {m.description}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      <button
        onClick={handleStart}
        disabled={starting}
        className="btn-solid-gold"
      >
        {starting ? "Starting…" : "Start Test"}
      </button>
    </div>
  );
}

function renderRecentTests({ history, historyError }) {
  return (
    <div>
      <div
        style={{
          color: "var(--text-secondary)",
          fontFamily: "Inter, sans-serif",
          fontWeight: 500,
          fontSize: 12,
          letterSpacing: "0.12em",
          textTransform: "uppercase",
          marginBottom: 14,
        }}
      >
        Recent Tests
      </div>

      {history === null && (
        <div>
          {/* FIX (#1): provide an array to .map */}
          {[0, 1, 2].map((i) => (
            <div
              key={i}
              className="pulse-bar"
              style={{
                height: 44,
                borderRadius: 6,
                background: "var(--bg-card)",
                marginBottom: 8,
              }}
            />
          ))}
        </div>
      )}

      {history && history.length === 0 && (
        <div
          style={{
            textAlign: "center",
            color: "var(--text-muted)",
            fontStyle: "italic",
            fontSize: 13,
            padding: "32px 0",
          }}
        >
          {historyError
            ? "No test history available. Connect the backend to load past runs."
            : "No test history available yet."}
        </div>
      )}

      {history && history.length > 0 && (
        <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
          {history.map((row, idx) => (
            <div
              key={idx}
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                padding: "12px 16px",
                background: "var(--bg-card)",
                border: "1px solid var(--border)",
                borderRadius: 6,
              }}
            >
              <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                <TierBadge tier={row.tier || "C"} size="sm" />
                <div>
                  <div style={{ color: "var(--text-primary)", fontSize: 13, fontWeight: 500 }}>
                    {row.agent_name || "Unknown agent"}
                  </div>
                  <div style={{ color: "var(--text-muted)", fontSize: 11, marginTop: 2 }}>
                    {row.date || row.timestamp || "—"}
                  </div>
                </div>
              </div>
              <div
                style={{
                  color: "var(--text-secondary)",
                  fontSize: 13,
                  fontFamily: "JetBrains Mono, monospace",
                }}
              >
                {typeof row.score === "number"
                  ? `${row.score.toFixed(1)}%`
                  : row.score || "—"}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function renderReportCard({
  agentName,
  agentEndpoint,
  testStatus,
  cardLoading,
  cardError,
  reportData,
  narrative,
  downloadReport,
}) {
  const baseCard = {
    background: "var(--bg-card)",
    border: "1px solid var(--border)",
    borderRadius: 8,
    padding: 32,
    minHeight: 400,
  };

  if (cardError) {
    return (
      <div style={{ ...baseCard, display: "flex", alignItems: "center", justifyContent: "center", textAlign: "center" }}>
        <div style={{ color: "var(--red)", fontSize: 12, fontFamily: "Inter, sans-serif" }}>
          {cardError}
        </div>
      </div>
    );
  }

  if (!agentName) {
    return (
      <div style={{ ...baseCard, display: "flex", alignItems: "center", justifyContent: "center", textAlign: "center" }}>
        <div style={{ color: "var(--text-muted)", fontStyle: "italic", fontSize: 13, fontFamily: "Inter, sans-serif" }}>
          Register your agent to generate a security report.
        </div>
      </div>
    );
  }

  if (testStatus === "RUNNING" || cardLoading) {
    return (
      <div style={{ ...baseCard, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 18 }}>
        <div
          style={{
            width: 36,
            height: 36,
            border: "2px solid var(--border)",
            borderTopColor: "var(--gold)",
            borderRadius: "50%",
            animation: "homeSpin 0.9s linear infinite",
          }}
        />
        <div style={{ color: "var(--text-secondary)", fontSize: 13, fontFamily: "Inter, sans-serif" }}>
          Generating security report...
        </div>
        <style>{`
          @keyframes homeSpin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
          }
        `}</style>
      </div>
    );
  }

  if (reportData && narrative) {
    return renderCompletedReportCard({ agentName, agentEndpoint, reportData, narrative, downloadReport, baseCard });
  }

  return (
    <div style={baseCard}>
      <div style={{ color: "var(--text-secondary)", fontFamily: "Inter, sans-serif", fontWeight: 500, fontSize: 11, letterSpacing: "0.12em", textTransform: "uppercase", marginBottom: 14 }}>
        Registered Agent
      </div>
      <div style={{ color: "var(--text-primary)", fontFamily: "Inter, sans-serif", fontWeight: 600, fontSize: 15, marginBottom: 4 }}>
        {agentName}
      </div>
      <div style={{ color: "var(--text-muted)", fontFamily: "'JetBrains Mono', monospace", fontSize: 11, whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis", marginBottom: 28 }} title={agentEndpoint}>
        {agentEndpoint || "—"}
      </div>
      <div style={{ color: "var(--text-secondary)", fontSize: 13, fontFamily: "Inter, sans-serif", lineHeight: 1.55 }}>
        Start the test to generate your security report.
      </div>
    </div>
  );
}

function renderCompletedReportCard({
  agentName,
  agentEndpoint,
  reportData,
  narrative,
  downloadReport,
  baseCard,
}) {
  const agentReport = reportData?.agent_report || {};
  const tier = agentReport.tier || "C";
  const score = typeof agentReport.security_score === "number" ? agentReport.security_score : 0;
  const primaryLabel = agentReport.primary_label || "—";
  const vuln = agentReport.vulnerability_by_type || {};
  const adv = reportData?.advanced || {};
  const isIncomplete = adv.is_incomplete === true;
  const packetsProcessed = adv.packets_processed ?? adv.total_packets_processed ?? 0;
  const packetsPlanned = adv.packets_planned ?? adv.total_packets_processed ?? 0;
  const downloaded = reportData?.downloaded === true;
  const disclaimer = reportData?.proof_disclaimer || "";
  const divider = { height: 1, background: "var(--border-subtle)", margin: "18px 0" };
  const sectionLabel = { color: "var(--text-secondary)", fontFamily: "Inter, sans-serif", fontWeight: 500, fontSize: 11, letterSpacing: "0.08em", textTransform: "uppercase", marginBottom: 8 };

  return (
    <div style={baseCard}>
      <div>
        <div style={{ color: "var(--text-primary)", fontFamily: "Inter, sans-serif", fontWeight: 600, fontSize: 15, marginBottom: 4 }}>
          {agentName}
        </div>
        <div style={{ color: "var(--text-muted)", fontFamily: "'JetBrains Mono', monospace", fontSize: 11, whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }} title={agentEndpoint}>
          {agentEndpoint || "—"}
        </div>
      </div>

      <div style={divider} />

      {isIncomplete && (
        <div style={{ marginBottom: 16 }}>
          <span style={{ display: "inline-block", fontFamily: "Inter, sans-serif", fontWeight: 700, fontSize: 11, letterSpacing: "0.1em", textTransform: "uppercase", padding: "4px 12px", borderRadius: 4, background: "rgba(239,68,68,0.15)", border: "1px solid rgba(239,68,68,0.5)", color: "var(--red)" }}>
            Incomplete
          </span>
          <div style={{ marginTop: 6, fontFamily: "Inter, sans-serif", fontSize: 12, color: "var(--text-secondary)", lineHeight: 1.5 }}>
            Tested {packetsProcessed} of {packetsPlanned} planned attacks — results reflect partial coverage.
          </div>
        </div>
      )}

      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", gap: 16 }}>
        <TierBadge tier={tier} size="lg" />
        <div style={{ textAlign: "right" }}>
          <div style={{ fontFamily: "Inter, sans-serif", fontWeight: 700, fontSize: 28, color: "var(--text-primary)", lineHeight: 1, letterSpacing: "-0.02em" }}>
            {Number(score).toFixed(1)}%
          </div>
          <div style={{ marginTop: 8, fontSize: 12, color: tierLabelColor(tier), fontFamily: "Inter, sans-serif", fontWeight: 500 }}>
            {primaryLabel}
          </div>
        </div>
      </div>

      <div style={divider} />

      <div>
        <div style={sectionLabel}>AI Assessment</div>
        <div style={{ fontFamily: "Inter, sans-serif", fontWeight: 400, fontSize: 13, color: "var(--text-primary)", lineHeight: 1.6, maxHeight: 160, overflowY: "auto", paddingRight: 6 }}>
          {narrative}
        </div>
      </div>

      <div style={divider} />

      <div>
        <div style={sectionLabel}>Vulnerabilities</div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          {Object.keys(ATTACK_LABELS).map((key) => {
            const status = (vuln[key] || "UNTESTED").toString().toUpperCase();
            const s = VULN_STATUS_STYLES[status] || VULN_STATUS_STYLES.UNTESTED;
            return (
              <div key={key} style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: "6px 0", borderBottom: "1px solid var(--border-subtle)" }}>
                <span style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 11, color: "var(--text-primary)" }}>
                  {ATTACK_LABELS[key]}
                </span>
                <span style={{ display: "inline-block", fontFamily: "Inter, sans-serif", fontSize: 11, padding: "2px 8px", borderRadius: 999, background: s.bg, color: s.color, border: `1px solid ${s.border}`, fontWeight: 500 }}>
                  {s.label}
                </span>
              </div>
            );
          })}
        </div>
      </div>

     <div style={{ marginTop: 24 }}>
  <button
    onClick={downloadReport}
    disabled={downloaded}
    className="btn-outline-gold"
    style={{ width: "100%", opacity: downloaded ? 0.5 : 1, cursor: downloaded ? "not-allowed" : "pointer" }}
  >
    {downloaded ? "Already Downloaded" : "Download Report"}
  </button>
  {disclaimer && (
    <div style={{ marginTop: 10, fontSize: 11, lineHeight: 1.5,
                  color: downloaded ? "var(--amber)" : "var(--text-secondary)",
                  fontFamily: "Inter, sans-serif" }}>
      {downloaded
        ? "This was your only copy — keep it safe. The server has discarded the signed report."
        : disclaimer}
    </div>
  )}
</div>

    </div>
  );
}
