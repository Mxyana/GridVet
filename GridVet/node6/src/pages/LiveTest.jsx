import React, { useEffect, useState } from "react";
import { API } from "../constants/api.js";
import LiveFeed from "../components/LiveFeed.jsx";
import AgentReport from "../components/AgentReport.jsx";
import { openStream, stopTest as apiStopTest } from "../constants/api.js";
import { getReport } from "../constants/api.js";
function StatusPill({ status }) {
  if (status === "RUNNING") {
    return (
      <span
        style={{
          display: "inline-flex",
          alignItems: "center",
          gap: 6,
          padding: "4px 12px",
          borderRadius: 999,
          background: "rgba(34,197,94,0.12)",
          border: "1px solid rgba(34,197,94,0.3)",
          color: "var(--green)",
          fontFamily: "Inter, sans-serif",
          fontSize: 12,
          fontWeight: 500,
        }}
      >
        <span
          className="dot-pulse"
          style={{
            width: 7,
            height: 7,
            borderRadius: "50%",
            background: "var(--green)",
            display: "inline-block",
          }}
        />
        Running
      </span>
    );
  }
  if (status === "COMPLETE") {
    return (
      <span
        style={{
          display: "inline-flex",
          alignItems: "center",
          gap: 6,
          padding: "4px 12px",
          borderRadius: 999,
          background: "rgba(201,168,76,0.12)",
          border: "1px solid rgba(201,168,76,0.4)",
          color: "var(--gold)",
          fontFamily: "Inter, sans-serif",
          fontSize: 12,
          fontWeight: 500,
        }}
      >
        ✓ Complete
      </span>
    );
  }
  if (status === "STOPPED") {
    return (
      <span
        style={{
          display: "inline-flex",
          alignItems: "center",
          gap: 6,
          padding: "4px 12px",
          borderRadius: 999,
          background: "rgba(239,68,68,0.12)",
          border: "1px solid rgba(239,68,68,0.3)",
          color: "var(--red)",
          fontFamily: "Inter, sans-serif",
          fontSize: 12,
          fontWeight: 500,
        }}
      >
        ■ Stopped
      </span>
    );
  }
  if (status === "ERROR") {
    return (
      <span
        style={{
          display: "inline-flex",
          alignItems: "center",
          gap: 6,
          padding: "4px 12px",
          borderRadius: 999,
          background: "rgba(239,68,68,0.12)",
          border: "1px solid rgba(239,68,68,0.3)",
          color: "var(--red)",
          fontFamily: "Inter, sans-serif",
          fontSize: 12,
          fontWeight: 500,
        }}
      >
        Error
      </span>
    );
  }
  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 6,
        padding: "4px 12px",
        borderRadius: 999,
        background: "rgba(58,58,58,0.4)",
        border: "1px solid var(--border)",
        color: "var(--text-secondary)",
        fontFamily: "Inter, sans-serif",
        fontSize: 12,
        fontWeight: 500,
      }}
    >
      <span
        style={{
          width: 7,
          height: 7,
          borderRadius: "50%",
          background: "var(--grey-out)",
          display: "inline-block",
        }}
      />
      Idle
    </span>
  );
}

export default function LiveTest() {
  const [agentName, setAgentName] = useState("Unknown Agent");
  const [status, setStatus] = useState("IDLE");
  const [stopMsg, setStopMsg] = useState(null);
  const [sessionId, setSessionId] = useState(null);

  useEffect(() => {
    const storedName = sessionStorage.getItem("gridvet_agent_name");
    if (storedName) setAgentName(storedName);

    const storedSession = sessionStorage.getItem("gridvet_session_id");
    setSessionId(storedSession);
  }, []);

  useEffect(() => {
    if (sessionId === null) return; // wait until we've read sessionStorage

    if (!sessionId) {
      setStatus("ERROR");
      setStopMsg({
        ok: false,
        message: "No active session ID. Please register again.",
      });
      return;
    }

    let source;
    let gotTerminalEvent = false;

    try {
      // NEW — also needs the token query param (line 161 silently relies on a
// header-less call that the hardened backend will reject).
// Use openStream() from api.js:
      source = openStream(sessionId);

      source.onopen = () =>
        setStatus((p) =>
          p === "COMPLETE" || p === "STOPPED" ? p : "RUNNING"
        );

      source.onmessage = (event) => {
        let parsed = null;
        try {
          parsed = JSON.parse(event.data);
        } catch {
          parsed = null;
        }

        if (parsed && parsed.event === "COMPLETE") {
          gotTerminalEvent = true;
          setStatus("COMPLETE");
          setStopMsg({
            ok: true,
            message:
              "Test complete. Return to Dashboard to view your agent's report card.",
          });
          source.close();
          return;
        }
        if (parsed && parsed.event === "STOPPED") {
          gotTerminalEvent = true;
          setStatus("STOPPED");
          setStopMsg({
            ok: true,
            message:
              "Test stopped. Return to Dashboard to view your agent's report card.",
          });
          source.close();
          return;
        }

        setStatus((p) =>
          p === "COMPLETE" || p === "STOPPED" ? p : "RUNNING"
        );
      };

      source.onerror = () => {
        // Don't infer COMPLETE from a transport error — that lies to the user.
        if (gotTerminalEvent) return;
        setStatus((p) =>
          p === "COMPLETE" || p === "STOPPED" ? p : "ERROR"
        );
        setStopMsg({
          ok: false,
          message: "Stream disconnected. Check backend or retry.",
        });
      };
    } catch {
      setStatus("ERROR");
      setStopMsg({
        ok: false,
        message: "Failed to open event stream.",
      });
    }

    return () => {
      if (source) source.close();
    };
  }, [sessionId]);

  const handleStop = async () => {
    setStopMsg(null);

    if (!sessionId) {
      setStopMsg({ ok: false, message: "No session found to stop." });
      return;
    }

    try {
      await apiStopTest(sessionId);
      setStatus("STOPPED");
      setStopMsg({
        ok: true,
        message:
          "Test stopped. Return to Dashboard to view your agent's report card.",
      });
    } catch (e) {
      setStopMsg({
        ok: false,
        message: "Could not reach backend to stop test.",
      });
    }
  };

  const noSession = status === "ERROR" && !sessionId;

  return (
    <div style={{ maxWidth: 1280, margin: "0 auto" }}>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          marginBottom: 24,
          gap: 12,
          flexWrap: "wrap",
        }}
      >
        <div>
          <h1
            style={{
              fontFamily: "Inter, sans-serif",
              fontWeight: 600,
              fontSize: 22,
              color: "var(--text-primary)",
              letterSpacing: "-0.01em",
            }}
          >
            Live Test — {agentName}
          </h1>
          <p
            style={{
              color: "var(--text-secondary)",
              fontSize: 13,
              marginTop: 4,
            }}
          >
            Streaming attack packets through the injection engine.
          </p>
        </div>
        <StatusPill status={status} />
      </div>

      {noSession ? (
        <div
          style={{
            background: "var(--bg-card)",
            border: "1px solid var(--border)",
            borderRadius: 8,
            padding: 20,
            color: "var(--red)",
            fontFamily: "Inter, sans-serif",
            fontSize: 13,
          }}
        >
          {stopMsg?.message ||
            "No active session ID. Please register again."}
        </div>
      ) : (
        <div
          className="livetest-grid"
          style={{
            display: "grid",
            gridTemplateColumns: "60fr 40fr",
            gap: 20,
          }}
        >
          <div>
            <LiveFeed sessionId={sessionId} />
          </div>

          <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
            <AgentReport status={status} sessionId={sessionId} />

            <div
              style={{
                background: "var(--bg-card)",
                border: "1px solid var(--border)",
                borderRadius: 8,
                padding: 20,
              }}
            >
              <div
                style={{
                  color: "var(--text-secondary)",
                  fontFamily: "Inter, sans-serif",
                  fontSize: 12,
                  textTransform: "uppercase",
                  letterSpacing: "0.12em",
                  marginBottom: 12,
                }}
              >
                Run Controls
              </div>
              <button
                onClick={handleStop}
                className="btn-stop"
                disabled={status === "COMPLETE" || status === "STOPPED"}
              >
                Stop Test
              </button>
              {stopMsg && (
                <div
                  style={{
                    marginTop: 12,
                    fontSize: 12,
                    color: stopMsg.ok ? "var(--green)" : "var(--red)",
                    fontFamily: "Inter, sans-serif",
                  }}
                >
                  {stopMsg.message}
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      <style>{`
        @media (max-width: 900px) {
          .livetest-grid {
            grid-template-columns: 1fr !important;
          }
        }
      `}</style>
    </div>
  );
}
