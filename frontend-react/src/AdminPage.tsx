import { useEffect, useState } from "react";

const API_BASE = "http://localhost:8000/api";

interface Candidate {
  evaluation_id: number;
  score: number;
  feedback: string;
  user_message: string;
  qwen_response: string;
}

interface HistoryEntry {
  id: number;
  source_evaluation_id: number;
  example_content: string;
  promoted_at: string;
}

export default function AdminPage() {
  const [candidates, setCandidates] = useState<Candidate[]>([]);
  const [history, setHistory] = useState<HistoryEntry[]>([]);
  const [error, setError] = useState<string | null>(null);

  async function loadAll() {
    const [candRes, histRes] = await Promise.all([
      fetch(`${API_BASE}/candidates`),
      fetch(`${API_BASE}/example-history`),
    ]);
    setCandidates(await candRes.json());
    setHistory(await histRes.json());
  }

  useEffect(() => {
    loadAll();
  }, []);

  async function handlePromote(id: number) {
    setError(null);
    const res = await fetch(`${API_BASE}/candidates/${id}/promote`, { method: "POST" });
    if (!res.ok) {
      const body = await res.json();
      setError(`Promote failed for #${id}: ${body.detail}`);
      return;
    }
    loadAll();
  }

  async function handleReject(id: number) {
    await fetch(`${API_BASE}/candidates/${id}/reject`, { method: "POST" });
    loadAll();
  }

  return (
    <div style={{ maxWidth: 700, margin: "0 auto", padding: "2rem" }}>
      <h1>Example candidates</h1>
      <p>5-star responses awaiting review.</p>

      {error && <p style={{ color: "red" }}>{error}</p>}
      {candidates.length === 0 && <p>No pending candidates.</p>}

      {candidates.map((c) => (
        <div key={c.evaluation_id} style={{ border: "1px solid #ccc", padding: "1rem", marginBottom: "1rem" }}>
          <p><strong>#{c.evaluation_id}</strong> — Score: {c.score}</p>
          <p><strong>Question:</strong> {c.user_message}</p>
          <pre style={{ whiteSpace: "pre-wrap" }}>{c.qwen_response}</pre>
          <p><strong>Feedback:</strong> {c.feedback}</p>
          <button onClick={() => handlePromote(c.evaluation_id)}>Approve</button>{" "}
          <button onClick={() => handleReject(c.evaluation_id)}>Reject</button>
        </div>
      ))}

      <h2>History</h2>
      {history.length === 0 ? (
        <p>No promotions yet.</p>
      ) : (
        <table>
          <thead>
            <tr><th>Promoted at</th><th>Source</th><th>Content</th></tr>
          </thead>
          <tbody>
            {history.map((h) => (
              <tr key={h.id}>
                <td>{h.promoted_at}</td>
                <td>#{h.source_evaluation_id}</td>
                <td><pre style={{ whiteSpace: "pre-wrap", fontSize: "0.8rem" }}>{h.example_content}</pre></td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}