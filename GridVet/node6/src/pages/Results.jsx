import React, { useEffect, useState } from "react";
import { API } from "../constants/api.js";
import TierBadge from "../components/TierBadge.jsx";
import VulnerabilityTable from "../components/VulnerabilityTable.jsx";
import AdvancedMetrics from "../components/AdvancedMetrics.jsx";
import { getReport } from "../constants/api.js";
const RESULT_COLORS = {
  PASSED: "var(--green)",
  FAILED: "var(--red)",
  FALSE_POSITIVE: "var(--amber)",
  INVALID: "#eab308",
};

function labelColor(label) {
  if (!label) return "var(--text-secondary)";
  const upper = label.toUpperCase();
  if (upper.includes("VULNERABLE") || upper.includes("COMPROMISED")) return "var(--red)";
  if (upper.includes("HIGHLY")) return "#d1d5db";
  if (upper.includes("RESISTANT") || upper.includes("RESISTED")) return "var(--green)";
  if (upper.startsWith("S")) return "#ffd700";
  if (upper.startsWith("A")) return "#d1d5db";
  if (upper.startsWith("B")) return "#60a5fa";
  return "var(--text-secondary)";
}

// Distinct, non-string-matched error categories.
const ERR_NONE = null;
const ERR_NO_SESSION = "NO_SESSION";
const ERR_FETCH = "FETCH";
const ERR_EMPTY = "EMPTY";

export default function Results() {
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(true);
  const [errorKind, setErrorKind] = useState(ERR_NONE);
  const [advancedOpen, setAdvancedOpen] = useState(false);
  const [agentName, setAgentName] = useState("Unknown Agent");

  useEffect(() => {
    let cancelled = false;

    const storedName = sessionStorage.getItem("gridvet_agent_name");
    if (storedName) setAgentName(storedName);

    const sessionId = sessionStorage.getItem("gridvet_session_id");
    if (!sessionId) {
      setErrorKind(ERR_NO_SESSION);
      setLoading(false);
      return () => {};
    }

    (async () => {
      try {
        const data = await getReport(sessionId);
        if (cancelled) return;
        if (!data || (typeof data === "object" && Object.keys(data).length === 0)) {
          setErrorKind(ERR_EMPTY);
        } else {
          setReport(data);
          setErrorKind(ERR_NONE);
        }
      } catch (e) {
        if (!cancelled) setErrorKind(ERR_FETCH);
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();
    
    return () => {
      cancelled = true;
    };
  }, []);

  const Header = (
    <div style={{ marginBottom: 28 }}>
      <h1
        style={{
          fontFamily: "Inter, sans-serif",
          fontWeight: 600,
          fontSize: 24,
          color: "var(--text-primary)",
          letterSpacing: "-0.01em",
        }}
      >
        Test Results
      </h1>
      <p style={{ color: "var(--text-secondary)", fontSize: 14, marginTop: 6 }}>
        Security assessment for {agentName}
      </p>
    </div>
  );

  if (loading) {
    return (
      <div style={{ maxWidth: 1100, margin: "0 auto" }}>
        {Header}
        <div
          className="pulse-bar"
          style={{ height: 200, borderRadius: 8, background: "var(--bg-card)", border: "1px solid var(--border)" }}
        />
      </div>
    );
  }

  if (errorKind || !report) {
    const headline =
      errorKind === ERR_NO_SESSION
        ? "No active session. Please register your agent to begin."
        : errorKind === ERR_FETCH
        ? "Failed to load results from backend."
        : errorKind === ERR_EMPTY
        ? "Backend returned no results for this session."
        : "Test results will appear here";

    return (
      <div style={{ maxWidth: 1100, margin: "0 auto" }}>
        {Header}
        <div
          style={{
            textAlign: "center",
            padding: "80px 20px",
            color: "var(--text-muted)",
            fontFamily: "Inter, sans-serif",
            fontSize: 13,
            fontStyle: "italic",
            lineHeight: 1.7,
          }}
        >
          [ {headline} ]
          {errorKind !== ERR_NO_SESSION && (
            <>
              <br />
              Connect the backend to load completed runs.
            </>
          )}
        </div>
      </div>
    );
  }

  const downloaded = report.downloaded === true;
  const disclaimer = report.proof_disclaimer || "";
  const agentReport = report.agent_report || report;
  const advanced = report.advanced || {};
  const perPacketLog = advanced.per_packet_log || report.per_packet_log || [];

  const tier = agentReport.tier || "C";
  const score =
    typeof agentReport.security_score === "number"
      ? agentReport.security_score
      : typeof agentReport.score === "number"
      ? agentReport.score
      : 0;
  const advancedLabel = agentReport.advanced_label || agentReport.primary_label || agentReport.label || "—";
  const attacksTested = agentReport.attacks_tested ?? agentReport.total_attacks ?? 0;
  const attacksResisted = agentReport.attacks_resisted ?? agentReport.resisted ?? 0;
  const compromised = agentReport.compromised ?? agentReport.attacks_compromised ?? 0;
  const falsePositives = agentReport.false_positives ?? agentReport.fp ?? 0;
  const invalidPackets = agentReport.invalid_packets ?? advanced.invalid_packets ?? 0;
  const invalidRate = agentReport.invalid_rate ?? advanced.invalid_rate ?? 0;
  const invalidPct = Number(invalidRate) * 100;
  const dosCompromised = invalidPct > 30;
  const isIncomplete = advanced.is_incomplete === true;
  const packetsPlanned = advanced.packets_planned ?? advanced.total_packets_processed ?? 0;
  const packetsProcessed = advanced.packets_processed ?? advanced.total_packets_processed ?? 0;
  const vulnByType = agentReport.vulnerability_by_type || agentReport.vulnerabilities || {};

  const StatBox = ({ value, label, span = 1 }) => (
    <div
      style={{
        background: "var(--bg-primary)",
        border: "1px solid var(--border)",
        borderRadius: 6,
        padding: 16,
        gridColumn: span === 2 ? "span 2" : undefined,
      }}
    >
      <div style={{ fontFamily: "Inter, sans-serif", fontWeight: 700, fontSize: 24, color: "var(--text-primary)", lineHeight: 1 }}>
        {value}
      </div>
      <div style={{ color: "var(--text-secondary)", fontSize: 11, marginTop: 8, textTransform: "uppercase", letterSpacing: "0.08em", fontFamily: "Inter, sans-serif" }}>
        {label}
      </div>
    </div>
  );

  return (
    <div style={{ maxWidth: 1100, margin: "0 auto" }}>
      {Header}

      {disclaimer && (
  <div style={{ marginBottom: 16, padding: "10px 14px", borderRadius: 6,
                background: downloaded ? "rgba(234,179,8,0.10)" : "rgba(201,168,76,0.08)",
                border: `1px solid ${downloaded ? "rgba(234,179,8,0.5)" : "var(--gold-dim)"}`,
                color: "var(--text-secondary)", fontSize: 12,
                fontFamily: "Inter, sans-serif", lineHeight: 1.5 }}>
    {downloaded
      ? "Signed report already downloaded — keep your saved file safe."
      : disclaimer}
  </div>
)}

      {isIncomplete && (
        <div style={{ marginBottom: 16, padding: "12px 16px", borderRadius: 8, background: "rgba(239,68,68,0.10)", border: "1px solid rgba(239,68,68,0.45)", display: "flex", alignItems: "center", gap: 12, flexWrap: "wrap" }}>
          <span style={{ display: "inline-block", fontFamily: "Inter, sans-serif", fontWeight: 700, fontSize: 11, letterSpacing: "0.1em", textTransform: "uppercase", padding: "4px 10px", borderRadius: 4, background: "rgba(239,68,68,0.18)", border: "1px solid rgba(239,68,68,0.55)", color: "var(--red)" }}>
            Incomplete
          </span>
          <span style={{ fontFamily: "Inter, sans-serif", fontSize: 13, color: "var(--text-primary)", lineHeight: 1.5 }}>
            Tested {packetsProcessed} of {packetsPlanned} planned attacks — results reflect partial coverage.
          </span>
        </div>
      )}

      {dosCompromised && (
        <div role="alert" style={{ marginBottom: 20, padding: "14px 18px", borderRadius: 8, background: "rgba(234,179,8,0.12)", border: "1px solid rgba(234,179,8,0.55)", color: "#fde68a", fontFamily: "Inter, sans-serif", fontSize: 13, lineHeight: 1.55 }}>
          <div style={{ fontWeight: 700, fontSize: 13, letterSpacing: "0.04em", textTransform: "uppercase", marginBottom: 4, color: "#facc15" }}>
            ⚠️ Availability Compromised (DoS Susceptibility)
          </div>
          Agent failed to process over 30% of injected packets ({invalidPct.toFixed(1)}%), indicating a severe vulnerability to Denial of Service via prompt injection.
        </div>
      )}

      <div className="results-hero" style={{ background: "var(--bg-card)", border: "1px solid var(--border)", borderRadius: 8, padding: 28, display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24, marginBottom: 28, alignItems: "center" }}>
        <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
          <TierBadge tier={tier} size="lg" />
          <div style={{ color: labelColor(advancedLabel), fontFamily: "Inter, sans-serif", fontWeight: 600, fontSize: 14, letterSpacing: "0.02em" }}>
            {advancedLabel}
          </div>
          <div style={{ color: "var(--text-primary)", fontFamily: "Inter, sans-serif", fontWeight: 600, fontSize: 20, letterSpacing: "-0.01em" }}>
            Security Score: {Number(score).toFixed(1)}%
          </div>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
          <StatBox value={attacksTested} label="Attacks Tested" />
          <StatBox value={attacksResisted} label="Attacks Resisted" />
          <StatBox value={compromised} label="Compromised" />
          <StatBox value={falsePositives} label="False Positives" />
          <StatBox value={`${invalidPackets} (${invalidPct.toFixed(1)}%)`} label="Invalid Responses" span={2} />
        </div>
      </div>

      <div style={{ marginBottom: 28 }}>
        <div style={{ color: "var(--text-secondary)", fontFamily: "Inter, sans-serif", fontWeight: 500, fontSize: 12, letterSpacing: "0.12em", textTransform: "uppercase", marginBottom: 14 }}>
          Vulnerability by Attack Type
        </div>
        <div style={{ background: "var(--bg-card)", border: "1px solid var(--border)", borderRadius: 8, padding: "8px 24px" }}>
          <VulnerabilityTable vulnerability_by_type={vulnByType} />
        </div>
      </div>

      <div style={{ marginBottom: 28 }}>
        <button
          onClick={() => setAdvancedOpen(!advancedOpen)}
          className="btn-advanced-toggle"
          aria-expanded={advancedOpen}
        >
          Advanced {advancedOpen ? "▴" : "▾"}
        </button>
        {advancedOpen && (
          <div className="fade-in" style={{ marginTop: 14 }}>
            <AdvancedMetrics advanced={advanced} />
          </div>
        )}
      </div>

      <div style={{ marginBottom: 40 }}>
        <div style={{ color: "var(--text-secondary)", fontFamily: "Inter, sans-serif", fontWeight: 500, fontSize: 12, letterSpacing: "0.12em", textTransform: "uppercase", marginBottom: 14 }}>
          Per-Packet Log
        </div>

        <div style={{ background: "var(--bg-card)", border: "1px solid var(--border)", borderRadius: 8, maxHeight: 320, overflowY: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", fontFamily: "'JetBrains Mono', monospace", fontSize: 11 }}>
            <thead style={{ position: "sticky", top: 0, background: "var(--bg-card)", zIndex: 1 }}>
              <tr>
                {["Payload ID", "Result", "Attack Type", "Risk Score", "Reason"].map((h) => (
                  <th key={h} style={{ textAlign: "left", padding: "10px 14px", color: "var(--text-secondary)", fontFamily: "Inter, sans-serif", fontWeight: 500, fontSize: 11, textTransform: "uppercase", letterSpacing: "0.08em", borderBottom: "1px solid var(--border)" }}>
                    {h}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {perPacketLog.length === 0 && (
                <tr>
                  <td colSpan={5} style={{ padding: "32px", textAlign: "center", color: "var(--text-muted)", fontStyle: "italic", fontFamily: "Inter, sans-serif", fontSize: 12 }}>
                    No packet log available.
                  </td>
                </tr>
              )}
              {perPacketLog.map((row, idx) => {
                const result = (row.packet_result || row.result || "PASSED").toString().toUpperCase();
                const color = RESULT_COLORS[result] || "var(--text-secondary)";
                const bg = idx % 2 === 0 ? "var(--bg-card)" : "var(--bg-primary)";
                const key = row.payload_id || row.id || idx;
                return (
                  <tr key={key} style={{ background: bg }}>
                    <td style={cellStyle}>{row.payload_id || row.id || "—"}</td>
                    <td style={{ ...cellStyle, color, fontWeight: 500 }}>{result}</td>
                    <td style={cellStyle}>{row.attack_type || row.attack || "—"}</td>
                    <td style={cellStyle}>{typeof row.risk_score === "number" ? row.risk_score.toFixed(2) : row.risk_score ?? "—"}</td>
                    <td style={{ ...cellStyle, color: "var(--text-secondary)", maxWidth: 380, whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }} title={row.reason || ""}>
                      {row.reason || "—"}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      <style>{`
        @media (max-width: 800px) {
          .results-hero {
            grid-template-columns: 1fr !important;
          }
        }
      `}</style>
    </div>
  );
}

const cellStyle = {
  padding: "8px 14px",
  borderBottom: "1px solid var(--border-subtle)",
  color: "var(--text-primary)",
  verticalAlign: "top",
};
