/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
        mono: ["JetBrains Mono", "monospace"],
      },
      colors: {
        "bg-primary": "var(--bg-primary)",
        "bg-card": "var(--bg-card)",
        "bg-hover": "var(--bg-hover)",
        "bg-input": "var(--bg-input)",
        border: "var(--border)",
        "border-subtle": "var(--border-subtle)",
        "text-primary": "var(--text-primary)",
        "text-secondary": "var(--text-secondary)",
        "text-muted": "var(--text-muted)",
        gold: "var(--gold)",
        "gold-dim": "var(--gold-dim)",
        green: "var(--green)",
        red: "var(--red)",
        amber: "var(--amber)",
        "grey-out": "var(--grey-out)",
      },
    },
  },
  plugins: [],
};
