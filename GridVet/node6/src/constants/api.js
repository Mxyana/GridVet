// ================================================================
// BACKEND INTEGRATION — NODE 6 CONNECTION POINTS
// Replace BASE_URL with your deployed FastAPI URL on Render
// All endpoints are defined here. Do not hardcode URLs elsewhere.
// ================================================================

export const BASE_URL = import.meta.env.VITE_API_URL;
// ↑ REPLACE THIS with your Render deployment URL before going live

export const API = {
  REGISTER_AGENT: `${BASE_URL}/register-agent`,
  // POST — body: { agent_name: string, agent_endpoint: string }

  RUN_TEST: `${BASE_URL}/run-test`,
  // POST — body: { tier: string, mode: string, session_id: string }

  STOP_TEST: (id) => `${BASE_URL}/stop-test/${id}`,
  // POST — no body — halts the current run for the specific session

  REPORT: (id) => `${BASE_URL}/report/${id}`,
  // GET  — returns ResultEngine.get_full_report() JSON for the session

  STREAM: (id) => `${BASE_URL}/stream/${id}`,
  // GET (SSE) — streams one JSON event per packet result for the session
  // Connect with: new EventSource(API.STREAM(sessionId))

  TEST_HISTORY: `${BASE_URL}/test-history`,
  // GET  — returns list of past test run summaries

  STATUS: (id) => `${BASE_URL}/status/${id}`,
  // GET  — lightweight test-run status probe for the session

  GENERATE_REPORT_CARD: `${BASE_URL}/generate-report-card`,
  // POST — body: { report: object, agent_name: string }
  //        returns { narrative: string, status: "ok" }

  VERIFY: `${BASE_URL}/verify`,
  // POST — multipart/form-data with a single "file" field (the .txt report)
  //        returns { verified: bool, message: string, data: {...} }
};
