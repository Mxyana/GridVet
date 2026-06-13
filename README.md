#GridVet
# Agentic Sandbox Security Framework

> A plug-and-play adversarial testing sandbox for AI crypto trading agents.

Built for the **Bitget Hackathon**.

## Overview

The Agentic Sandbox Security Framework is an end-to-end harness for stress-testing AI trading agents against adversarial inputs. It targets agents that consume unstructured market context — social sentiment, macro headlines, on-chain summaries — and measures how they hold up when that context is weaponised. The framework specialises in **indirect prompt injection** delivered through market data streams, a threat model that bypasses conventional input validation. Any developer can point the sandbox at their agent's endpoint and receive a complete, automated security audit with per-packet verdicts and aggregate scoring.

## The Problem

AI trading agents increasingly read unstructured market data — news wires, social feeds, on-chain alerts — as first-class inputs to their decision loop. That surface is unauthenticated and unsanitised by design, which makes it the ideal carrier for **indirect prompt injection**: malicious instructions hidden inside text that looks like legitimate market data.

There is currently no dedicated sandboxed environment for testing this specific threat model. Generic red-teaming tools treat the agent as a chatbot; trading-system test rigs assume the data feed is honest. Neither catches the attack surface that matters here.

## Architecture — The 6 Nodes

### Node 1 — Market Data Simulator
Streams historical BTC/USDT market data as structured JSON payloads (OHLCV plus five free-text context fields). Acts as the honest baseline feed.

### Node 2 — Injection Interceptor Engine
Sits in the data pipeline between Node 1 and Node 3. Intercepts clean payloads and probabilistically blends adversarial prompt injection strings into context fields. Every poisoned packet is appended to a persistent `injection_ledger.json` so ground truth is preserved for downstream scoring. Five attack types: `goal_hijack`, `false_announcement`, `wallet_redirect`, `panic_trigger`, `tool_manipulation`.

### Node 3 — Sandbox Environment (Agent Tester)
Wraps the target agent. Accepts the composite payload from Node 2 with the `meta` block stripped — the agent never knows whether a given packet was poisoned. Returns a structured trading decision. Supports both an internal reference agent and external developer agents via webhook URL.

### Node 4 — Verification Layer
Intercepts every agent decision before execution and runs five blind security checks: wallet check, override-language check, panic-language check, execution-anomaly check, and announcement-bias check. Emits a verdict (`SUSPICIOUS` or `CLEAN`) with a weighted risk score and a list of failed checks.

### Node 5 — Result Engine
Cross-references Node 4's verdict against the `injection_ledger.json` ground truth. Computes the final `PASSED` or `FAILED` result per packet and rolls them up into aggregate statistics (true positives, false negatives, detection rate) across the full test run.

### Node 6 — Frontend Dashboard
Real-time browser monitoring UI. Live-scrolling operations log, per-node status cards, and aggregate metrics display.

## Plug In Your Agent

Any developer can test their agent in two steps.

### Step 1 — Accept this POST request

`POST /decide`

```json
{
  "market_data": {
    "symbol": "BTC/USDT",
    "timestamp": "ISO8601",
    "interval": "24h",
    "open": 0.0,
    "high": 0.0,
    "low": 0.0,
    "close": 0.0,
    "volume": 0.0,
    "price_change_pct": 0.0,
    "volume_change_pct": 0.0
  },
  "context": {
    "social_sentiment": "string",
    "macro_events": "string",
    "onchain_activity": "string",
    "order_book_summary": "string",
    "sentiment_summary": "string"
  }
}
```

### Step 2 — Return this response

```json
{
  "source_payload_id": "string",
  "timestamp": "ISO8601",
  "decision": {
    "action": "BUY | SELL | HOLD",
    "pair": "BTC/USDT",
    "order_type": "MARKET | LIMIT",
    "quantity": 0.0,
    "price": null,
    "destination_wallet": null
  },
  "reasoning": "string",
  "raw_output": "string"
}
```

That is the entire integration. Submit your endpoint URL to the sandbox. The rest is automatic — the framework drives the load, injects the attacks, scores the responses, and returns the report.

## Attack Types

| Attack Type          | Target Field         | What It Attempts                                       |
| -------------------- | -------------------- | ------------------------------------------------------ |
| `goal_hijack`        | `social_sentiment`   | Override the agent's core trading objective            |
| `false_announcement` | `macro_events`       | Fabricated high-impact event to trigger a bad trade    |
| `wallet_redirect`    | `onchain_activity`   | Reroute funds to an attacker-controlled address        |
| `panic_trigger`      | `social_sentiment`   | Engineered fear signal to force immediate liquidation  |
| `tool_manipulation`  | `order_book_summary` | Corrupt execution parameters and order size            |

## Tech Stack

- Python 3.10+
- FastAPI
- Hosted on Render
- Standard library only for Node 2 and Node 4 (zero third-party dependencies in the security-critical path)
- JSON-based injection ledger for ground-truth tracking

## Setup

```bash
git clone <repo>
cd <repo>
pip install -r requirements.txt
uvicorn main:app --reload
```

## Team Roles

- **AppSec Technical Architect** — Node 2, Node 4, Node 5
- **Software Engineer** — Node 1, Node 3
- **Frontend Developer** — Node 6

---

This infrastructure gives Web3 builders a reproducible, automated way to harden AI agents against the prompt-injection attack class before those agents ever touch real capital.
