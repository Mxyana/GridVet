import React from "react";
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import Sidebar from "./components/Sidebar.jsx";
import Home from "./pages/Home.jsx";
import LiveTest from "./pages/LiveTest.jsx";
import Results from "./pages/Results.jsx";
import Verify from "./pages/Verify.jsx";

function PageFade({ children }) {
  const location = useLocation();
  return (
    <div key={location.pathname} className="fade-in h-full">
      {children}
    </div>
  );
}

function Layout() {
  return (
    <div
      className="flex h-screen w-screen overflow-hidden"
      style={{ background: "var(--bg-primary)", color: "var(--text-primary)" }}
    >
      <Sidebar />
      <main className="flex-1 overflow-y-auto" style={{ padding: "32px" }}>
        <PageFade>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/live" element={<LiveTest />} />
            <Route path="/results" element={<Results />} />
            <Route path="/verify" element={<Verify />} />
          </Routes>
        </PageFade>
      </main>
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <Layout />
    </BrowserRouter>
  );
}
