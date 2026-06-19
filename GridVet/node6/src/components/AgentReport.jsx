import React, { useEffect, useRef, useState } from "react";
import { API } from "../constants/api.js";
import TierBadge from "./TierBadge.jsx";
import VulnerabilityTable from "./VulnerabilityTable.jsx";

const LABEL_COLORS = {
  VULNERABLE: "var(--red)",
  COMPROMISED: "var(--red)",
  RESISTANT: "var(--green)",
  "HIGHLY RESISTANT": "#d1d5db",
};

function labelColor(label) {
  if (!label) return "var(--text-secondary)";
  const upper = label.toUpperCase();
  if (upper.includes("VULNERABLE") || upper.includes("COMPROMISED"))
    return "var(--red)";
  if (upper.includes("HIGHLY")) return "#d1d5db";
  if (upper.includes("RESISTANT") || upper.includes("RESISTED"))
    return "var(--green)";
  if (upper.startsWith("S")) return "#ffd700";
  if (upper.startsWith("A")) return "#d1d5db";
  if (upper.startsWith("B")) return "#60a5fa";
  return "var(--text-secondary)";
}

export default function AgentReport({ status }) {
  const [report, setReport] = useState(null);
  const [error, setError] = useState(false);
  const intervalRef = useRef(null);

  const fetchReport = async () => {
    try {
      // ⚡ BACKEND: GET API.REPORT — fetches live agent report
      const res = await fetch(API.REPORT);
      if (!res.ok) throw new Error("bad response");
      const data = await res.json();
      setReport(data);
      setError(false);
    } catch (e) {
      setError(true);
    }
  };

  useEffect(() => {
    fetchReport();
    intervalRef.current = setInterval(() => {
      fetchReport();
    }, 2000);
    return () => {
      if (intervalRef.current) clearInterval(intervalRef.current);
    };
  }, []);

  useEffect(() => {
    if (status === "COMPLETE" && intervalRef.current) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
      fetchReport(); // one final fetch
    }
  }, [status]);

  // Placeholder state
  if (error || !report) {
    return (
      <div
        style={{
          textAlign: "center",
          padding: "60px 20px",
          color: "var(--text-muted)",
          fontFamily: "Inter, sans-serif",
          fontSize: 13,
          fontStyle: "italic",
          lineHeight: 1.7,
        }}
      >
        [ Agent report will appear here ]
        <br />
        Connect the backend and register an agent to begin.
      </div>
    );
  }

  const agentReport = report.agent_report || report;
  const tier = agentReport.tier || "C";
  const score =
    typeof agentReport.security_score === "number"
      ? agentReport.security_score
      : typeof agentReport.score === "number"
      ? agentReport.score
      : 0;
  const primaryLabel =
    agentReport.primary_label || agentReport.label || "—";
  const vulnByType =
    agentReport.vulnerability_by_type || agentReport.vulnerabilities || {};

  const attacksTested =
    agentReport.attacks_tested ?? agentReport.total_attacks ?? 0;
  const attacksResisted =
    agentReport.attacks_resisted ?? agentReport.resisted ?? 0;
  const compromised =
    agentReport.compromised ?? agentReport.attacks_compromised ?? 0;

  return (
    <div
      style={{
        background: "var(--bg-card)",
        border: "1px solid var(--border)",
        borderRadius: 8,
        padding: 24,
      }}
    >
      {/* Top section: tier + score */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 20,
          marginBottom: 20,
        }}
      >
        <TierBadge tier={tier} size="lg" />
        <div>
          <div
            style={{
              fontFamily: "Inter, sans-serif",
              fontWeight: 700,
              fontSize: 32,
              color: "var(--text-primary)",
              lineHeight: 1,
              letterSpacing: "-0.02em",
            }}
          >
            {Number(score).toFixed(1)}%
          </div>
          <div
            style={{
              marginTop: 8,
              fontFamily: "Inter, sans-serif",
              fontSize: 13,
              fontWeight: 500,
              color: labelColor(primaryLabel),
              letterSpacing: "0.02em",
            }}
          >
            {primaryLabel}
          </div>
        </div>
      </div>

      <div
        style={{
          height: 1,
          background: "var(--border-subtle)",
          margin: "8px 0 20px 0",
        }}
      />

      {/* Middle: vulnerability table */}
      <VulnerabilityTable vulnerability_by_type={vulnByType} />

      {/* Bottom: counts */}
      <div
        style={{
          marginTop: 18,
          fontSize: 12,
          color: "var(--text-secondary)",
          fontFamily: "Inter, sans-serif",
        }}
      >
        {attacksTested} attacks tested · {attacksResisted} resisted ·{" "}
        {compromised} compromised
      </div>
    </div>
  );
}
