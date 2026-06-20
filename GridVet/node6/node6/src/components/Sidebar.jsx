import React, { useState } from "react";
import { NavLink } from "react-router-dom";

const navItems = [
  { to: "/", label: "Dashboard", end: true },
  { to: "/live", label: "Live Test", end: false },
  { to: "/results", label: "Results", end: false },
  { to: "/verify", label: "Verify Result", end: false },
];

export default function Sidebar() {
  const [open, setOpen] = useState(false);

  const NavInner = () => (
    <div className="flex flex-col h-full">
      {/* Top brand */}
      <div style={{ padding: "50px 20px 20px 20px" }}>
        <div
          style={{
            color: "var(--gold)",
            fontFamily: "Inter, sans-serif",
            fontWeight: 700,
            fontSize: "20px",
            letterSpacing: "-0.01em",
          }}
        >
         GridVet
        </div>
        <div
          style={{
            color: "var(--text-muted)",
            fontSize: "11px",
            marginTop: "4px",
            letterSpacing: "0.04em",
          }}
        >
          Security Framework
        </div>
      </div>

      {/* Nav links */}
      <nav className="flex flex-col" style={{ padding: "0 12px" }}>
        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            end={item.end}
            onClick={() => setOpen(false)}
            className="sidebar-link"
          >
            {({ isActive }) => (
              <div
                className="sidebar-link-inner"
                style={{
                  padding: "9px 14px",
                  borderLeft: `2px solid ${
                    isActive ? "var(--gold)" : "transparent"
                  }`,
                  color: isActive ? "var(--gold)" : "var(--text-secondary)",
                  fontFamily: "Inter, sans-serif",
                  fontWeight: isActive ? 500 : 400,
                  fontSize: "13px",
                  borderRadius: "4px",
                  transition: "all 150ms ease",
                  cursor: "pointer",
                }}
              >
                {item.label}
              </div>
            )}
          </NavLink>
        ))}
      </nav>

      {/* Bottom version tag */}
      <div className="mt-auto" style={{ padding: "20px" }}>
        <div
          style={{
            color: "var(--text-muted)",
            fontSize: "10px",
            letterSpacing: "0.03em",
          }}
        >
          v1.0 — Hackathon Build
        </div>
      </div>
    </div>
  );

  return (
    <>
      {/* Mobile hamburger */}
      <button
        className="md:hidden"
        onClick={() => setOpen(!open)}
        aria-label="Toggle navigation"
        style={{
          position: "fixed",
          top: 14,
          left: 14,
          zIndex: 50,
          width: 36,
          height: 36,
          borderRadius: 6,
          border: "1px solid var(--border)",
          background: "var(--bg-card)",
          color: "var(--text-primary)",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <div style={{ display: "flex", flexDirection: "column", gap: 3 }}>
          <span style={{ width: 14, height: 1.5, background: "currentColor" }} />
          <span style={{ width: 14, height: 1.5, background: "currentColor" }} />
          <span style={{ width: 14, height: 1.5, background: "currentColor" }} />
        </div>
      </button>

      {/* Desktop sidebar */}
      <aside
        className="hidden md:flex"
        style={{
          width: 220,
          flexShrink: 0,
          background: "var(--bg-card)",
          borderRight: "1px solid var(--border)",
        }}
      >
        <NavInner />
      </aside>

      {/* Mobile drawer */}
      {open && (
        <>
          <div
            onClick={() => setOpen(false)}
            className="md:hidden"
            style={{
              position: "fixed",
              inset: 0,
              background: "rgba(0,0,0,0.5)",
              zIndex: 40,
            }}
          />
          <aside
            className="md:hidden fade-in"
            style={{
              position: "fixed",
              top: 0,
              left: 0,
              bottom: 0,
              width: 220,
              background: "var(--bg-card)",
              borderRight: "1px solid var(--border)",
              zIndex: 45,
              display: "flex",
            }}
          >
            <NavInner />
          </aside>
        </>
      )}
    </>
  );
}
