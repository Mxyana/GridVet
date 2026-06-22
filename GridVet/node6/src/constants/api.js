// ================================================================
// BACKEND INTEGRATION — NODE 6 CONNECTION POINTS
//
// This module is the SINGLE source of truth for backend calls.
// Components must call the helper functions exported here
// (registerAgent, runTest, getTestHistory, …) rather than calling
// fetch() directly against API.* URLs, otherwise the X-Client-Id
// and Authorization headers will be missing and:
//   - /test-history will return an empty list (rows are scoped to
//     the calling browser via X-Client-Id)
//   - /run-test, /stop-test, /status, /report, /session,
//     /stream will reject the call (require Bearer session_token)
//
// The raw URL map (`API.*`) is kept for backward compatibility only.
// ================================================================

export const BASE_URL = import.meta.env.VITE_API_URL;

export const API = {
  REGISTER_AGENT:        `${BASE_URL}/register-agent`,
  RUN_TEST:              `${BASE_URL}/run-test`,
  STOP_TEST:             (id) => `${BASE_URL}/stop-test/${id}`,
  REPORT:                (id) => `${BASE_URL}/report/${id}`,
  STREAM:                (id) => `${BASE_URL}/stream/${id}`,
  TEST_HISTORY:          `${BASE_URL}/test-history`,
  STATUS:                (id) => `${BASE_URL}/status/${id}`,
  SESSION:               (id) => `${BASE_URL}/session/${id}`,
  GENERATE_REPORT_CARD:  `${BASE_URL}/generate-report-card`,
  VERIFY:                `${BASE_URL}/verify`,
  DOWNLOAD_REPORT: (id) => `${BASE_URL}/download-report/${id}`,
};


// ----------------------------------------------------------------
// Client-Id (per-browser, persistent)
// ----------------------------------------------------------------
// Scopes /test-history so Browser A on PC 1 and Browser B (incognito)
// on PC 2 never see each other's runs. Generated once on first load
// and stored in localStorage. Sent on /register-agent and every
// /test-history call. The server echoes the value it actually used
// in the /register-agent response; we reconcile with it in case the
// browser was the one that minted it.

const CLIENT_ID_KEY = 'gridvet_client_id';

export function getClientId() {
  let id = null;
  try {
    id = localStorage.getItem(CLIENT_ID_KEY);
  } catch { /* localStorage blocked — fall through */ }

  if (!id) {
    id = (crypto?.randomUUID?.() ?? _fallbackUuid());
    try { localStorage.setItem(CLIENT_ID_KEY, id); } catch { /* ignore */ }
  }
  return id;
}

function _setClientId(id) {
  if (!id) return;
  try { localStorage.setItem(CLIENT_ID_KEY, id); } catch { /* ignore */ }
}

function _fallbackUuid() {
  // Only used if crypto.randomUUID is unavailable (very old browsers).
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
    const r = (Math.random() * 16) | 0;
    return (c === 'x' ? r : (r & 0x3) | 0x8).toString(16);
  });
}


// ----------------------------------------------------------------
// Session token (per-session, per-tab — survives reloads)
// ----------------------------------------------------------------
// The server returns session_token ONCE from /register-agent. It
// authorizes every session-scoped route. We persist it in
// sessionStorage so:
//   - a page refresh keeps the running session usable
//   - closing the tab discards the token (matches the server's
//     in-memory _SESSIONS lifetime)
//   - other tabs / windows can't read it (sessionStorage is
//     scoped per browsing context, unlike localStorage)
//
// Storage shape: a single JSON object under one key, mapping
// session_id -> session_token. A single key keeps reads/writes
// atomic enough for our needs and makes "clear all" trivial.

const SESSION_TOKEN_KEY = 'gridvet_session_tokens';

function _readTokenMap() {
  try {
    const raw = sessionStorage.getItem(SESSION_TOKEN_KEY);
    if (!raw) return {};
    const obj = JSON.parse(raw);
    return obj && typeof obj === 'object' ? obj : {};
  } catch {
    return {};
  }
}

function _writeTokenMap(map) {
  try {
    sessionStorage.setItem(SESSION_TOKEN_KEY, JSON.stringify(map));
  } catch { /* quota or disabled — silent */ }
}

export function getSessionToken(sessionId) {
  if (!sessionId) return null;
  return _readTokenMap()[sessionId] || null;
}

function _setSessionToken(sessionId, token) {
  if (!sessionId || !token) return;
  const map = _readTokenMap();
  map[sessionId] = token;
  _writeTokenMap(map);
}

function _deleteSessionToken(sessionId) {
  if (!sessionId) return;
  const map = _readTokenMap();
  if (sessionId in map) {
    delete map[sessionId];
    _writeTokenMap(map);
  }
}

/**
 * List every session_id that still has a token in this tab.
 * Useful for "resume" flows after a reload — pair with getStatus()
 * to filter for sessions the server still recognizes.
 */
export function listKnownSessions() {
  return Object.keys(_readTokenMap());
}

/**
 * Wipe every stored token in this tab. Does not contact the server.
 */
export function clearAllSessionTokens() {
  try { sessionStorage.removeItem(SESSION_TOKEN_KEY); } catch { /* ignore */ }
}

function _authHeaders(sessionId) {
  const tok = getSessionToken(sessionId);
  if (!tok) {
    throw new Error(
      `No session_token for session "${sessionId}". Either the tab was ` +
      `closed since registerAgent() was called, or the session was opened ` +
      `in a different tab.`
    );
  }
  return { 'Authorization': `Bearer ${tok}` };
}


// ----------------------------------------------------------------
// fetch helpers
// ----------------------------------------------------------------

async function _json(res) {
  const text = await res.text();
  let body;
  try { body = text ? JSON.parse(text) : {}; } catch { body = { raw: text }; }
  if (!res.ok) {
    const detail = body?.detail || body?.message || res.statusText;
    const err = new Error(`HTTP ${res.status}: ${detail}`);
    err.status = res.status;
    err.body = body;
    throw err;
  }
  return body;
}


// ================================================================
// PUBLIC API — use these from components
// ================================================================

/**
 * Register an external agent and start a new session.
 * Persists session_token (in memory) and reconciles client_id.
 * Returns the full server response, including session_id.
 */
export async function registerAgent({ agent_name, agent_endpoint }) {
  const res = await fetch(API.REGISTER_AGENT, {
    method: 'POST',
    credentials: 'include',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ agent_name, agent_endpoint }),
  });
  const body = await _json(res);
  _setSessionToken(body.session_id, body.session_token);
  // body.proof_disclaimer is surfaced by the caller (Home.jsx).
  return body;
}

export async function runTest({ session_id, tier, mode, injection_rate, packet_delay_seconds, seed }) {
  const res = await fetch(API.RUN_TEST, {
    method: 'POST',
    credentials:'include',
    headers: {
      'Content-Type': 'application/json',
      ..._authHeaders(session_id),
    },
    body: JSON.stringify({
      session_id, tier, mode, injection_rate, packet_delay_seconds, seed,
    }),
  });
  return _json(res);
}

export async function stopTest(session_id) {
  const res = await fetch(API.STOP_TEST(session_id), {
    method: 'POST',
    credentials: 'include',
    headers: _authHeaders(session_id),
  });
  return _json(res);
}

export async function getStatus(session_id) {
  const res = await fetch(API.STATUS(session_id), {
    headers: _authHeaders(session_id),
  });
  return _json(res);
}

export async function getReport(session_id) {
  const res = await fetch(API.REPORT(session_id), {
    headers: _authHeaders(session_id),
  });
  return _json(res);
}

/**
 * One-shot signed-report download. Server returns 410 on second call.
 * Returns { ok: true } on success, or { ok: false, status, alreadyDownloaded }.
 */
export async function downloadReport(session_id) {
  const tok = getSessionToken(session_id);
  if (!tok) throw new Error(`No session_token for session "${session_id}".`);
  const url = `${API.DOWNLOAD_REPORT(session_id)}?token=${encodeURIComponent(tok)}`;
  const res = await fetch(url, { credentials: 'include' });
  if (res.status === 410) {
    return { ok: false, status: 410, alreadyDownloaded: true };
  }
  if (!res.ok) {
    return { ok: false, status: res.status, alreadyDownloaded: false };
  }
  const blob = await res.blob();
  const blobUrl = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = blobUrl;
  a.download = `${session_id}.txt`;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(blobUrl);
  return { ok: true };
}

export async function evictSession(session_id) {
  const res = await fetch(API.SESSION(session_id), {
    method: 'DELETE',
    headers: _authHeaders(session_id),
  });
  // Drop the token from storage regardless of server outcome.
  _deleteSessionToken(session_id);
  return _json(res);
}

/**
 * Build a URL for `new EventSource(...)`.
 * EventSource cannot set custom headers, so the session_token is
 * passed as a query parameter — the server accepts both forms.
 */
export function streamUrl(session_id) {
  const tok = getSessionToken(session_id);
  if (!tok) {
    throw new Error(`No session_token for session "${session_id}".`);
  }
  return `${API.STREAM(session_id)}?token=${encodeURIComponent(tok)}`;
}

/**
 * Open an EventSource bound to this session. Caller is responsible
 * for attaching .onmessage / .onerror / .close().
 */
export function openStream(session_id) {
  return new EventSource(streamUrl(session_id), { withCredentials: true });
}
/**
 * Per-browser run history. Empty list if the server has no rows for
 * our client_id (e.g. fresh incognito window).
 */
export async function getTestHistory() {
  const res = await fetch(API.TEST_HISTORY, {
    headers: { 'X-Client-Id': getClientId() },
  });
  return _json(res);
}

export async function clearTestHistory() {
  const res = await fetch(API.TEST_HISTORY, {
    method: 'DELETE',
    headers: { 'X-Client-Id': getClientId() },
  });
  return _json(res);
}

export async function generateReportCard({ report, agent_name }) {
  const res = await fetch(API.GENERATE_REPORT_CARD, {
    method: 'POST',
    credentials: 'include',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ report, agent_name }),
  });
  return _json(res);
}

export async function verifyReport(file) {
  const form = new FormData();
  form.append('file', file);
  const res = await fetch(API.VERIFY, { method: 'POST',
  credentials: 'include', body: form });
  return _json(res);
}
