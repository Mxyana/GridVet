import React from "react";

const TIER_STYLES = {
  S: { color: "#ffd700", glow: "rgba(255,215,0,0.2)" },
  A: { color: "#d1d5db", glow: "rgba(209,213,219,0.15)" },
  B: { color: "#60a5fa", glow: "rgba(96,165,250,0.15)" },
  C: { color: "#ef4444", glow: "rgba(239,68,68,0.15)" },
  D: { color: "#ef4444", glow: "rgba(239,68,68,0.25)", pulse: true },
};

export default function TierBadge({ tier = "C", size = "lg" }) {
  const t = (tier || "C").toString().toUpperCase();
  const style = TIER_STYLES[t] || TIER_STYLES.C;

  if (size === "sm") {
    return (
      <div
        style={{
          width: 28,
          height: 28,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          border: `1.5px solid ${style.color}`,
          color: style.color,
          borderRadius: 6,
          fontFamily: "Inter, sans-serif",
          fontWeight: 700,
          fontSize: 13,
          lineHeight: 1,
        }}
      >
        {t}
      </div>
    );
  }

  return (
    <div
      className={style.pulse ? "tier-pulse" : ""}
      style={{
        width: 80,
        height: 80,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        border: `2px solid ${style.color}`,
        color: style.color,
        borderRadius: 14,
        fontFamily: "Inter, sans-serif",
        fontWeight: 700,
        fontSize: 36,
        lineHeight: 1,
        boxShadow: `0 0 24px ${style.glow}, inset 0 0 12px ${style.glow}`,
        background: "var(--bg-card)",
      }}
    >
      {t}
    </div>
  );
}
