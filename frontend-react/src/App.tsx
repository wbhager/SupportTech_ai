import { useState, useEffect, useRef } from "react";
import ReactMarkdown from "react-markdown";

type Message = {
  id: number;
  text: string;
  role: "user" | "assistant";
  popped: boolean;
};

type FlyingBubble = {
  id: number;
  role: "user" | "assistant";
  startX: number;
  startY: number;
  endX: number;
  endY: number;
};

function App() {
  const [convId] = useState(() => crypto.randomUUID());
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [flyingBubbles, setFlyingBubbles] = useState<FlyingBubble[]>([]);
  const [theme, setTheme] = useState("theme-default");
  const [isLoading, setIsLoading] = useState(false);
  const [conversations, setConversations] = useState<{conv_id: string, title: string}[]>([]);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const feedRef = useRef<HTMLDivElement>(null);
  const inputRectRef = useRef<DOMRect | null>(null);

  useEffect(() => {
    document.documentElement.className = theme;
  }, [theme]);

  useEffect(() => {
    const el = textareaRef.current;
    if (!el) return;
    el.style.height = "auto";
    el.style.height = el.scrollHeight + "px";
  }, [message]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  useEffect(() => {
    const update = () => {
      if (textareaRef.current) {
        inputRectRef.current = textareaRef.current.getBoundingClientRect();
      }
    };
    update();
    window.addEventListener("resize", update);
    return () => window.removeEventListener("resize", update);
  }, []);

  useEffect(() => {
    if (sidebarOpen) {
      fetch("http://localhost:8000/conversations")
        .then((res) => res.json())
        .then((data) => {
          setConversations(data.conversations);
        })
        .catch((err) => {
          console.error("Error fetching conversations:", err);
        });
    }
  }, [sidebarOpen]);

  const sendMessage = async () => {
    if (!message.trim() || isLoading) return;
    
    // Capture position first, before anything changes
    if (textareaRef.current) {
      inputRectRef.current = textareaRef.current.getBoundingClientRect();
    }
    const inputRect = inputRectRef.current;
    
    const userText = message;
    setMessage("");
  
    // Capture rects synchronously before any state changes
    const feedRect = feedRef.current?.getBoundingClientRect();
  
    // Helper to build a flying bubble using pre-captured rects
    const launchBubble = (text: string, role: "user" | "assistant") => {
      const id = Date.now() + Math.random();
  
      const startX = inputRect
        ? inputRect.left + inputRect.width / 2
        : window.innerWidth / 2;
      const startY = inputRect ? inputRect.top : window.innerHeight - 100;
  
      // Placing bubble at correct position
      const endRect = messagesEndRef.current?.getBoundingClientRect();
      const endY = Math.min(
        Math.max(endRect ? endRect.top : feedRect ? feedRect.bottom - 60 : window.innerHeight - 200, 50),
        window.innerHeight - 50
      );
      
      const endX = Math.min(
        Math.max(
          endRect
            ? role === "user"
              ? Math.min(endRect.right - 60, window.innerWidth - 80)
              : Math.max(endRect.left + 60, 80)
            : role === "user" ? window.innerWidth - 80 : 80,
          50
        ),
        window.innerWidth - 50
      );
  
      setFlyingBubbles((prev) => [...prev, { id, role, startX, startY, endX, endY }]);
  
      setTimeout(() => {
        setFlyingBubbles((prev) => prev.filter((b) => b.id !== id));
        setMessages((prev) => [...prev, { id, text, role, popped: false }]);
        setTimeout(() => {
          setMessages((prev) =>
            prev.map((m) => (m.id === id ? { ...m, popped: true } : m))
          );
        }, 50);
      }, 2200);
    };
  
    launchBubble(userText, "user");
    setIsLoading(true);
  
    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ conv_id: convId, message: userText }),
      });
      const data = await res.json();
      launchBubble(data.response, "assistant");
    } finally {
      setIsLoading(false);
    }
  };

  const deleteConversation = async (conv_id: string) => {
    await fetch(`http://localhost:8000/conversations/${conv_id}`, {
      method: "DELETE",
    });
    setConversations(prev => prev.filter(c => c.conv_id !== conv_id));
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <>
    <div className="page">
      {/* flying bubbles overlay */}
      {flyingBubbles.map((b) => (
        <FlyingBubbleEl key={b.id} bubble={b} />
      ))}

      <div className="page-top">
        <div className="theme-switcher">
          <span className="theme-label"> Apply New Color Theme </span>
          <div className="theme-options">
            <button className="btn-default" onClick={() => setTheme("theme-default")}>Default</button>
            <button className="btn-dark" onClick={() => setTheme("theme-dark")}>Dark</button>
          </div>
        </div>
      </div>

      <div className="messages-feed" ref={feedRef}>
        {messages.map((m) => (
          <div key={m.id} className={`bubble-row ${m.role}`}>
            <div className={`bubble-outer ${m.popped ? "popped" : "pre-pop"}`}>
              <div className="bubble-text">
                <ReactMarkdown>{m.text}</ReactMarkdown>
              </div>
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="bubble-row assistant">
            <div className="bubble-outer popped">
              <div className="bubble-text loading-bubble">
                <span /><span /><span />
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="page-bottom">
        <textarea
          ref={textareaRef}
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={isLoading}
          placeholder="Type a message… (Enter to send, Shift+Enter for newline)"
          rows={1}
          className="chat-input"
        />
        <button onClick={sendMessage} disabled={isLoading} className="send-btn">
          {isLoading ? "Sending…" : "Send"}
        </button>
      </div>
    </div>

  <div className="sidebar-container">
    <button 
      className={`sidebar-toggle ${sidebarOpen ? "sidebar-toggle-open" : ""}`}
      onClick={() => setSidebarOpen(!sidebarOpen)}
    >
      {sidebarOpen ? "✕" : "💬"}
  </button>

    {sidebarOpen && (
      <div className="sidebar-panel">
        {conversations.map((conv, index) => (
          <div 
            key={conv.conv_id} 
            className="sidebar-item"
            style={{ animationDelay: `${0.05 + index * 0.1}s` }}
          >
            <span>{conv.title}</span>
            <button onClick={() => deleteConversation(conv.conv_id)}>✕</button>
          </div>
        ))}
      </div>
    )}
  </div>
  </>
  );
}

// ── animated flying bubble component ──────────────────────────────────────────
function FlyingBubbleEl({ bubble }: { bubble: FlyingBubble }) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const animRef = useRef<number>(0);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const { startX, startY, endX, endY } = bubble;
    const duration = 2200;
    const start = performance.now();

    // generate squiggly waypoints between start and end
    const numPoints = 8;
    const waypoints: { x: number; y: number }[] = [];
    for (let i = 0; i <= numPoints; i++) {
      const t = i / numPoints;
      const baseX = startX + (endX - startX) * t;
      const baseY = startY + (endY - startY) * t;
      // perpendicular wiggle, stronger in the middle, random direction
      const wiggleStrength = Math.sin(t * Math.PI) * 120;
      const wiggleX = (Math.random() - 0.5) * wiggleStrength;
      const wiggleY = (Math.random() - 0.5) * wiggleStrength * 0.5;
      waypoints.push({ x: baseX + wiggleX, y: baseY + wiggleY });
    }
    // pin start and end exactly
    waypoints[0] = { x: startX, y: startY };
    waypoints[numPoints] = { x: endX, y: endY };

    // catmull-rom interpolation along waypoints
    function catmullRom(
      pts: { x: number; y: number }[],
      t: number
    ): { x: number; y: number } {
      const n = pts.length - 1;
      const scaled = t * n;
      const i = Math.min(Math.floor(scaled), n - 1);
      const lt = scaled - i;
      const p0 = pts[Math.max(i - 1, 0)];
      const p1 = pts[i];
      const p2 = pts[Math.min(i + 1, n)];
      const p3 = pts[Math.min(i + 2, pts.length - 1)];
      const x =
        0.5 *
        ((2 * p1.x) +
          (-p0.x + p2.x) * lt +
          (2 * p0.x - 5 * p1.x + 4 * p2.x - p3.x) * lt * lt +
          (-p0.x + 3 * p1.x - 3 * p2.x + p3.x) * lt * lt * lt);
      const y =
        0.5 *
        ((2 * p1.y) +
          (-p0.y + p2.y) * lt +
          (2 * p0.y - 5 * p1.y + 4 * p2.y - p3.y) * lt * lt +
          (-p0.y + 3 * p1.y - 3 * p2.y + p3.y) * lt * lt * lt);
      return { x, y };
    }

    // easing: slow start, slow end, slightly bouncy
    function ease(t: number): number {
      return t < 0.5
        ? 4 * t * t * t
        : 1 - Math.pow(-2 * t + 2, 3) / 2;
    }

    // bubble size: starts small, grows, then shrinks right before pop
    function bubbleSize(t: number): number {
      if (t < 0.1) return 6 + t * 10 * 14;        // grow from 6 to 20
      if (t < 0.85) return 20 + Math.sin(t * Math.PI * 3) * 3; // gentle breathe
      return 20 * (1 - ((t - 0.85) / 0.15));       // shrink to 0 before pop
    }

    function drawBubble(x: number, y: number, r: number, alpha: number) {
      if (r <= 0) return;
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // outer ring (the "soap film" edge)
      const isPrimary = bubble.role === "user";
      const ringColor = isPrimary
        ? `rgba(255, 79, 216, ${alpha * 0.7})`
        : `rgba(160, 160, 180, ${alpha * 0.5})`;

      ctx.beginPath();
      ctx.arc(x, y, r, 0, Math.PI * 2);
      ctx.strokeStyle = ringColor;
      ctx.lineWidth = 2.5;
      ctx.stroke();

      // transparent fill with subtle inner glow
      const grad = ctx.createRadialGradient(
        x - r * 0.3, y - r * 0.3, r * 0.05,
        x, y, r
      );
      grad.addColorStop(0, `rgba(255,255,255,${alpha * 0.18})`);
      grad.addColorStop(0.5, `rgba(255,255,255,${alpha * 0.04})`);
      grad.addColorStop(1, isPrimary
        ? `rgba(255, 79, 216, ${alpha * 0.12})`
        : `rgba(160,160,200,${alpha * 0.08})`
      );
      ctx.beginPath();
      ctx.arc(x, y, r, 0, Math.PI * 2);
      ctx.fillStyle = grad;
      ctx.fill();

      // specular highlight (top-left shine)
      const shine = ctx.createRadialGradient(
        x - r * 0.38, y - r * 0.38, 0,
        x - r * 0.38, y - r * 0.38, r * 0.45
      );
      shine.addColorStop(0, `rgba(255,255,255,${alpha * 0.6})`);
      shine.addColorStop(1, `rgba(255,255,255,0)`);
      ctx.beginPath();
      ctx.arc(x, y, r, 0, Math.PI * 2);
      ctx.fillStyle = shine;
      ctx.fill();

      // tiny secondary highlight (bottom-right, dimmer)
      const shine2 = ctx.createRadialGradient(
        x + r * 0.5, y + r * 0.5, 0,
        x + r * 0.5, y + r * 0.5, r * 0.25
      );
      shine2.addColorStop(0, `rgba(255,255,255,${alpha * 0.2})`);
      shine2.addColorStop(1, `rgba(255,255,255,0)`);
      ctx.beginPath();
      ctx.arc(x, y, r, 0, Math.PI * 2);
      ctx.fillStyle = shine2;
      ctx.fill();
    }

    function animate(now: number) {
      const elapsed = now - start;
      const raw = Math.min(Math.max(elapsed / duration, 0), 1);
      const t = ease(raw);

      const pos = catmullRom(waypoints, t);
      const size = bubbleSize(raw);
      const alpha = raw < 0.9 ? 1 : 1 - ((raw - 0.9) / 0.1);

      drawBubble(pos.x, pos.y, size, alpha);

      if (raw < 1) {
        animRef.current = requestAnimationFrame(animate);
      } else {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
    }

    animRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(animRef.current);
  }, [bubble]);

  return (
    <canvas
      ref={canvasRef}
      style={{
        position: "fixed",
        top: 0,
        left: 0,
        pointerEvents: "none",
        zIndex: 9999,
      }}
    />
  );
}

export default App;