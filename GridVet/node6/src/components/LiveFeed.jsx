import React, { useEffect, useRef, useState } from "react";
import { API } from "../constants/api.js";

const RESULT_COLORS = {
  PASSED: "var(--green)",
  FAILED: "var(--red)",
  FALSE_POSITIVE: "var(--amber)",
};

function pad(n) {
  return String(n).padStart(2, "0");
}

function fmtTime(d) {
  return `${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
}

function padRight(str, len) {
  const s = (str ?? "").toString();
  if (s.length >= len) return s.slice(0, len);
  return s + " ".repeat(len - s.length);
}

export default function LiveFeed() {
  const [entries, setEntries] = useState([]);
  const [connected, setConnected] = useState(false);
  const scrollRef = useRef(null);

  useEffect(() => {
    // ⚡ BACKEND: SSE API.STREAM — streams per-packet results
    let source;
    try {
      source = new EventSource(API.STREAM);

      source.onopen = () => setConnected(true);

      source.onmessage = (event) => {
        try {
          const payload = JSON.parse(event.data);
          const entry = {
            time: fmtTime(new Date()),
            payload_id: payload.payload_id || payload.id || "—",
            packet_result:
              payload.packet_result || payload.result || "PASSED",
            attack_type:
              payload.attack_type || payload.attack || "clean",
            risk_score:
              typeof payload.risk_score === "number"
                ? payload.risk_score
                : 0,
          };
          setEntries((prev) => {
            const next = [...prev, entry];
            return next.length > 200 ? next.slice(next.length - 200) : next;
          });
        } catch (e) {
          // ignore malformed
        }
      };

      source.onerror = () => {
        setConnected(false);
      };
    } catch (e) {
      setConnected(false);
    }

    return () => {
      if (source) source.close();
    };
  }, []);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [entries]);

  return (
    <div
      style={{
        background: "var(--bg-card)",
        border: "1px solid var(--border)",
        borderRadius: 8,
        height: 480,
        overflow: "hidden",
        display: "flex",
        flexDirection: "column",
      }}
    >
      {/* Header row */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          padding: "14px 18px",
          borderBottom: "1px solid var(--border-subtle)",
        }}
      >
        <div
          style={{
            color: "var(--text-secondary)",
            fontFamily: "Inter, sans-serif",
            fontSize: 12,
            textTransform: "uppercase",
            letterSpacing: "0.12em",
            fontWeight: 500,
          }}
        >
          Live Feed
        </div>
        <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
          <span
            className={connected ? "dot-pulse" : ""}
            style={{
              width: 8,
              height: 10,
              borderRadius: "50%",
              background: connected ? "var(--green)" : "var(--grey-out)",
              display: "inline-block",
            }}
          />
          <span
            style={{
              fontSize: 11,
              color: "var(--text-muted)",
              fontFamily: "Inter, sans-serif",
            }}
          >
            {connected ? "connected" : "offline"}
          </span>
        </div>
      </div>

      {/* Log area */}
      <div
        ref={scrollRef}
        style={{
          flex: 1,
          overflowY: "auto",
          padding: "16px",
          fontFamily: "'JetBrains Mono', monospace",
          fontSize: 12,
        }}
      >
        {entries.length === 0 && (
          <div
            style={{
              height: "100%",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              color: "var(--text-muted)",
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 13,
            }}
          >
            Waiting for test to start...
          </div>
        )}

        {entries.map((entry, i) => {
          const color = RESULT_COLORS[entry.packet_result] || "var(--text-secondary)";
          const widthPct = Math.max(0, Math.min(1, entry.risk_score)) * 100;
          return (
            <div
              key={i}
              className="fade-in"
              style={{ marginBottom: 8 }}
            >
              <div
                style={{
                  display: "flex",
                  whiteSpace: "pre",
                  color: "var(--text-secondary)",
                  lineHeight: 1.6,
                }}
              >
                <span style={{ color: "var(--text-muted)" }}>
                  [{entry.time}]{"  "}
                </span>
                <span style={{ color: "var(--text-primary)" }}>
                  {padRight(entry.payload_id, 20)}
                </span>
                <span style={{ marginLeft: 8, color, fontWeight: 500 }}>
                  {padRight(entry.packet_result, 14)}
                </span>
                <span style={{ marginLeft: 4, color: "var(--text-secondary)" }}>
                  {entry.attack_type}
                </span>
              </div>
              <div
                style={{
                  height: 2,
                  background: "var(--border-subtle)",
                  borderRadius: 2,
                  marginTop: 4,
                  overflow: "hidden",
                }}
              >
                <div
                  className="bar-fade"
                  style={{
                    width: `${widthPct}%`,
                    height: "100%",
                    background: color,
                    transition: "width 200ms ease",
                  }}
                />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
