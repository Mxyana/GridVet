// ================================================================
// BACKEND INTEGRATION — NODE 6 CONNECTION POINTS
// Replace BASE_URL with your deployed FastAPI URL on Render
// All endpoints are defined here. Do not hardcode URLs elsewhere.
// ================================================================

export const BASE_URL = "http://localhost:8000";
// ↑ REPLACE THIS with your Render deployment URL before going live

export const API = {
  REGISTER_AGENT: `${BASE_URL}/register-agent`,
  // POST — body: { agent_name: string, agent_endpoint: string }

  RUN_TEST: `${BASE_URL}/run-test`,
  // POST — no body — triggers the full pipeline

  STOP_TEST: `${BASE_URL}/stop-test`,
  // POST — no body — halts the current run

  REPORT: `${BASE_URL}/report`,
  // GET  — returns ResultEngine.get_full_report() JSON

  STREAM: `${BASE_URL}/stream`,
  // GET (SSE) — streams one JSON event per packet result
  // Connect with: new EventSource(API.STREAM)

  TEST_HISTORY: `${BASE_URL}/test-history`,
  // GET  — returns list of past test run summaries

  STATUS: `${BASE_URL}/status`,
  // GET  — lightweight test-run status probe

  GENERATE_REPORT_CARD: `${BASE_URL}/generate-report-card`,
  // POST — body: { report: object, agent_name: string }
  //        returns { narrative: string, status: "ok" }

  VERIFY: `${BASE_URL}/verify`,
  // POST — multipart/form-data with a single "file" field (the .txt report)
  //        returns { verified: bool, message: string, data: {...} }
};
