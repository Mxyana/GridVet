import React, { useRef, useState } from "react";
import { API } from "../constants/api.js";

// ============================================================================
// Verify.jsx — V2 Verification Portal
// Upload a signed GridVet AppSec report (.txt) and confirm against the
// records.json ledger that the file has not been altered since emission.
// Styling mirrors Home.jsx (dark surface + gold accents + JetBrains Mono).
// ============================================================================

const cardStyle = {
  background: "var(--bg-card)",
  border: "1px solid var(--border)",
  borderRadius: 8,
  padding: 24,
};

const labelStyle = {
  display: "block",
  color: "var(--text-secondary)",
  fontFamily: "Inter, sans-serif",
  fontSize: 12,
  marginBottom: 6,
  letterSpacing: "0.02em",
};

const monoStyle = {
  fontFamily: "'JetBrains Mono', monospace",
  fontSize: 12,
  color: "var(--text-primary)",
  wordBreak: "break-all",
};

const sectionLabel = {
  color: "var(--text-secondary)",
  fontFamily: "Inter, sans-serif",
  fontWeight: 500,
  fontSize: 11,
  letterSpacing: "0.08em",
  textTransform: "uppercase",
  marginBottom: 8,
};

export default function Verify() {
  const fileInputRef = useRef(null);
  const [fileName, setFileName] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState(null); // {verified, message, data}
  const [errorMsg, setErrorMsg] = useState("");

  // -------------------------------------------------------------------------
  // File selection — triggers POST to /verify immediately
  // -------------------------------------------------------------------------
  async function handleFileChange(e) {
    const file = e.target.files?.[0];
    if (!file) return;

    setFileName(file.name);
    setResult(null);
    setErrorMsg("");

    if (!file.name.toLowerCase().endsWith(".txt")) {
      setErrorMsg("Only .txt report files are accepted.");
      return;
    }

    setSubmitting(true);
    try {
      const form = new FormData();
      form.append("file", file);

      const res = await fetch(API.VERIFY, {
        method: "POST",
        body: form,
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setErrorMsg("Failed to reach verification service. Check the backend.");
    } finally {
      setSubmitting(false);
    }
  }

  function handlePickFile() {
    if (fileInputRef.current) fileInputRef.current.click();
  }

  function handleReset() {
    setFileName("");
    setResult(null);
    setErrorMsg("");
    if (fileInputRef.current) fileInputRef.current.value = "";
  }

  // -------------------------------------------------------------------------
  // Render
  // -------------------------------------------------------------------------
  return (
    <div style={{ maxWidth: 900, margin: "0 auto" }}>
      {/* Header */}
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
          Verify Report
        </h1>
        <p
          style={{
            color: "var(--text-secondary)",
            fontSize: 14,
            marginTop: 6,
          }}
        >
          Upload a GridVet security report (.txt) to confirm its
          cryptographic signature against the audit ledger.
        </p>
      </div>

      {/* Upload card */}
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
          Upload Report
        </div>

        <label style={labelStyle}>Report File (.txt)</label>

        <input
          ref={fileInputRef}
          type="file"
          accept=".txt,text/plain"
          onChange={handleFileChange}
          style={{ display: "none" }}
        />

        <div
          style={{
            display: "flex",
            gap: 12,
            alignItems: "center",
            flexWrap: "wrap",
          }}
        >
          <button
            onClick={handlePickFile}
            disabled={submitting}
            className="btn-outline-gold"
          >
            {submitting ? "Verifying…" : "Choose File"}
          </button>

          <div
            style={{
              ...monoStyle,
              color: fileName ? "var(--text-primary)" : "var(--text-muted)",
              fontSize: 12,
              flex: "1 1 auto",
              minWidth: 0,
              overflow: "hidden",
              textOverflow: "ellipsis",
              whiteSpace: "nowrap",
            }}
            title={fileName}
          >
            {fileName || "No file selected."}
          </div>

          {(result || errorMsg) && (
            <button onClick={handleReset} className="btn-outline-gold">
              Reset
            </button>
          )}
        </div>

        {errorMsg && (
          <div
            style={{
              marginTop: 16,
              fontSize: 12,
              color: "var(--red)",
              fontFamily: "Inter, sans-serif",
            }}
          >
            {errorMsg}
          </div>
        )}
      </div>

      {/* Loading state */}
      {submitting && (
        <div
          style={{
            ...cardStyle,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            gap: 14,
            padding: 32,
          }}
        >
          <div
            style={{
              width: 32,
              height: 32,
              border: "2px solid var(--border)",
              borderTopColor: "var(--gold)",
              borderRadius: "50%",
              animation: "verifySpin 0.9s linear infinite",
            }}
          />
          <div
            style={{
              color: "var(--text-secondary)",
              fontSize: 13,
              fontFamily: "Inter, sans-serif",
            }}
          >
            Computing SHA-256 and matching ledger…
          </div>
          <style>{`
            @keyframes verifySpin {
              from { transform: rotate(0deg); }
              to   { transform: rotate(360deg); }
            }
          `}</style>
        </div>
      )}

      {/* Result state */}
      {!submitting && result && renderResultCard(result)}
    </div>
  );
}

// ===========================================================================
// Result card — green "Authentic" or red "Forged / Altered"
// ===========================================================================
function renderResultCard(result) {
  const isAuthentic = result?.verified === true;
  const data = result?.data || {};
  const message = result?.message || "";

  const accent = isAuthentic ? "var(--green)" : "var(--red)";
  const accentBg = isAuthentic
    ? "rgba(34,197,94,0.12)"
    : "rgba(239,68,68,0.12)";
  const accentBorder = isAuthentic
    ? "rgba(34,197,94,0.35)"
    : "rgba(239,68,68,0.35)";
  const badgeLabel = isAuthentic ? "Authentic Report" : "Forged or Altered";

  return (
    <div
      style={{
        ...cardStyle,
        borderColor: accentBorder,
      }}
    >
      {/* Badge */}
      <div style={{ marginBottom: 18 }}>
        <span
          style={{
            display: "inline-block",
            fontFamily: "Inter, sans-serif",
            fontWeight: 700,
            fontSize: 12,
            letterSpacing: "0.1em",
            textTransform: "uppercase",
            padding: "6px 14px",
            borderRadius: 4,
            background: accentBg,
            border: `1px solid ${accentBorder}`,
            color: accent,
          }}
        >
          {isAuthentic ? "✓ " : "✗ "}
          {badgeLabel}
        </span>
      </div>

      {/* Human-readable message */}
      {message && (
        <div
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: 13,
            color: "var(--text-primary)",
            lineHeight: 1.55,
            marginBottom: 22,
          }}
        >
          {message}
        </div>
      )}

      {/* Divider */}
      <div
        style={{
          height: 1,
          background: "var(--border-subtle)",
          margin: "0 0 18px 0",
        }}
      />

      {/* Metadata block */}
      <div style={sectionLabel}>Ledger Metadata</div>

      <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
        {renderMetaRow("Audit ID", data.report_id || data.session_key)}
        {renderMetaRow("Bot Name", data.bot_name)}
        {renderMetaRow("Status", data.status)}
        {renderMetaRow(
          "Timestamp",
          data.timestamp_ms
            ? `${new Date(Number(data.timestamp_ms)).toUTCString()}`
            : null
        )}
        {renderMetaRow("Expected SHA-256", data.secure_hash, true)}
        {renderMetaRow("Computed SHA-256", data.computed_hash, true)}
      </div>
    </div>
  );
}

function renderMetaRow(label, value, mono = false) {
  if (value === undefined || value === null || value === "") return null;
  return (
    <div
      style={{
        display: "flex",
        gap: 14,
        alignItems: "flex-start",
        padding: "8px 0",
        borderBottom: "1px solid var(--border-subtle)",
      }}
    >
      <div
        style={{
          flex: "0 0 140px",
          color: "var(--text-secondary)",
          fontFamily: "Inter, sans-serif",
          fontSize: 12,
          letterSpacing: "0.02em",
        }}
      >
        {label}
      </div>
      <div
        style={{
          flex: "1 1 auto",
          color: "var(--text-primary)",
          fontFamily: mono ? "'JetBrains Mono', monospace" : "Inter, sans-serif",
          fontSize: mono ? 11 : 13,
          wordBreak: "break-all",
        }}
      >
        {String(value)}
      </div>
    </div>
  );
}
