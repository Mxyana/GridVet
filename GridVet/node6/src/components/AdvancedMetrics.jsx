import React, { useState } from "react";

const RESULT_COLORS = {
  PASSED: "var(--green)",
  FAILED: "var(--red)",
  FALSE_POSITIVE: "var(--amber)",
  INVALID: "#eab308", // yellow — DoS bucket
};

export default function AdvancedMetrics({ advanced = {} }) {
  const totalPackets = advanced.total_packets_processed ?? 0;
  const detectionRate = advanced.detection_rate ?? 0;
  const falsePositiveRate = advanced.false_positive_rate ?? 0;
  const cleanPackets =
    advanced.clean_packets ?? advanced.clean_packet_count ?? 0;
  const poisonedPackets =
    advanced.poisoned_packets ?? advanced.poisoned_packet_count ?? 0;
  const invalidPackets = advanced.invalid_packets ?? 0;
  const invalidRate = advanced.invalid_rate ?? 0;
  const perPacketLog = Array.isArray(advanced.per_packet_log)
    ? advanced.per_packet_log
    : [];

  // Track which rows are expanded — keyed by index so duplicate payload IDs
  // (unlikely but possible) don't collide.
  const [expanded, setExpanded] = useState(() => new Set());
  const toggle = (idx) => {
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(idx)) next.delete(idx);
      else next.add(idx);
      return next;
    });
  };

  const card = {
    background: "var(--bg-card)",
    border: "1px solid var(--border)",
    borderRadius: 6,
    padding: 16,
    flex: 1,
  };

  const numberStyle = {
    fontFamily: "Inter, sans-serif",
    fontWeight: 700,
    fontSize: 22,
    color: "var(--gold)",
    lineHeight: 1,
  };

  const labelStyle = {
    color: "var(--text-secondary)",
    fontSize: 11,
    marginTop: 8,
    textTransform: "uppercase",
    letterSpacing: "0.08em",
    fontFamily: "Inter, sans-serif",
  };

  const cellStyle = {
    padding: "8px 14px",
    borderBottom: "1px solid var(--border-subtle)",
    color: "var(--text-primary)",
    verticalAlign: "top",
    fontFamily: "'JetBrains Mono', monospace",
    fontSize: 11,
  };

  return (
    <div>
      {/* Top-level KPI strip */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: 12,
          marginBottom: 16,
        }}
      >
        <div style={card}>
          <div style={numberStyle}>{totalPackets}</div>
          <div style={labelStyle}>Total Packets</div>
        </div>
        <div style={card}>
          <div style={numberStyle}>
            {(Number(detectionRate) * 100).toFixed(1)}%
          </div>
          <div style={labelStyle}>Detection Rate</div>
        </div>
        <div style={card}>
          <div style={numberStyle}>
            {(Number(falsePositiveRate) * 100).toFixed(1)}%
          </div>
          <div style={labelStyle}>False Positive Rate</div>
        </div>
        <div style={card}>
          <div style={{ ...numberStyle, color: "#eab308" }}>
            {(Number(invalidRate) * 100).toFixed(1)}%
          </div>
          <div style={labelStyle}>Invalid Rate (DoS)</div>
        </div>
      </div>

      <div
        style={{
          color: "var(--text-secondary)",
          fontSize: 13,
          fontFamily: "Inter, sans-serif",
          marginBottom: 20,
        }}
      >
        Clean Packets: {cleanPackets} &nbsp;·&nbsp; Poisoned Packets:{" "}
        {poisonedPackets} &nbsp;·&nbsp; Invalid Packets:{" "}
        <span style={{ color: "#eab308" }}>{invalidPackets}</span>
      </div>

      {/* Developer-focused per-packet log with expandable raw_output rows */}
      <div
        style={{
          color: "var(--text-secondary)",
          fontFamily: "Inter, sans-serif",
          fontWeight: 500,
          fontSize: 12,
          letterSpacing: "0.12em",
          textTransform: "uppercase",
          marginBottom: 10,
        }}
      >
        Per-Packet Log — click a row to view raw agent output
      </div>

      <div
        style={{
          background: "var(--bg-card)",
          border: "1px solid var(--border)",
          borderRadius: 8,
          maxHeight: 420,
          overflowY: "auto",
        }}
      >
        <table
          style={{
            width: "100%",
            borderCollapse: "collapse",
          }}
        >
          <thead
            style={{
              position: "sticky",
              top: 0,
              background: "var(--bg-card)",
              zIndex: 1,
            }}
          >
            <tr>
              {["", "Payload ID", "Result", "Attack Type", "Reason"].map(
                (h, i) => (
                  <th
                    key={i}
                    style={{
                      textAlign: "left",
                      padding: "10px 14px",
                      color: "var(--text-secondary)",
                      fontFamily: "Inter, sans-serif",
                      fontWeight: 500,
                      fontSize: 11,
                      textTransform: "uppercase",
                      letterSpacing: "0.08em",
                      borderBottom: "1px solid var(--border)",
                      width: i === 0 ? 24 : undefined,
                    }}
                  >
                    {h}
                  </th>
                )
              )}
            </tr>
          </thead>
          <tbody>
            {perPacketLog.length === 0 && (
              <tr>
                <td
                  colSpan={5}
                  style={{
                    padding: "32px",
                    textAlign: "center",
                    color: "var(--text-muted)",
                    fontStyle: "italic",
                    fontFamily: "Inter, sans-serif",
                    fontSize: 12,
                  }}
                >
                  No packet log available.
                </td>
              </tr>
            )}
            {perPacketLog.map((row, idx) => {
              const result = (
                row.packet_result || row.result || "PASSED"
              )
                .toString()
                .toUpperCase();
              const color = RESULT_COLORS[result] || "var(--text-secondary)";
              const bg =
                idx % 2 === 0 ? "var(--bg-card)" : "var(--bg-primary)";
              const isOpen = expanded.has(idx);
              const raw =
                row.raw_output ||
                row.rawOutput ||
                "(no raw output captured)";
              const payloadId =
                row.source_payload_id || row.payload_id || row.id || "—";
              const reason =
                row.result_reason || row.reason || "—";

              return (
                <React.Fragment key={idx}>
                  <tr
                    onClick={() => toggle(idx)}
                    style={{
                      background: bg,
                      cursor: "pointer",
                      userSelect: "none",
                    }}
                    title="Click to expand raw agent output"
                  >
                    <td
                      style={{
                        ...cellStyle,
                        color: "var(--text-secondary)",
                        textAlign: "center",
                      }}
                    >
                      {isOpen ? "▾" : "▸"}
                    </td>
                    <td style={cellStyle}>{payloadId}</td>
                    <td style={{ ...cellStyle, color, fontWeight: 600 }}>
                      {result}
                    </td>
                    <td style={cellStyle}>
                      {row.attack_type || row.attack || "—"}
                    </td>
                    <td
                      style={{
                        ...cellStyle,
                        color: "var(--text-secondary)",
                        maxWidth: 380,
                        whiteSpace: "nowrap",
                        overflow: "hidden",
                        textOverflow: "ellipsis",
                      }}
                      title={reason}
                    >
                      {reason}
                    </td>
                  </tr>
                  {isOpen && (
                    <tr style={{ background: bg }}>
                      <td colSpan={5} style={{ padding: "0 14px 14px" }}>
                        <div
                          style={{
                            fontFamily: "Inter, sans-serif",
                            fontSize: 11,
                            color: "var(--text-secondary)",
                            textTransform: "uppercase",
                            letterSpacing: "0.08em",
                            marginBottom: 6,
                          }}
                        >
                          Raw Agent Output
                        </div>
                        <pre
                          style={{
                            margin: 0,
                            padding: 12,
                            background: "var(--bg-primary)",
                            border: "1px solid var(--border)",
                            borderRadius: 6,
                            fontFamily: "'JetBrains Mono', monospace",
                            fontSize: 11,
                            color: "var(--text-primary)",
                            whiteSpace: "pre-wrap",
                            wordBreak: "break-word",
                            maxHeight: 240,
                            overflowY: "auto",
                          }}
                        >
                          {raw}
                        </pre>
                      </td>
                    </tr>
                  )}
                </React.Fragment>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
