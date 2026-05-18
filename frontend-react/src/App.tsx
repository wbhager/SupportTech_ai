import { useState, useEffect , useRef} from "react";
import ReactMarkdown from "react-markdown";

type Message = {
  id: number;
  text: string;
  role: "user" | "assistant";
  popped: boolean;
};

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [theme, setTheme] = useState("theme-default");
  const [isLoading, setIsLoading] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

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

  const addMessage = (text: string, role: "user" | "assistant") => {
    const id = Date.now();
    // Phase 1: tiny floating bubble
    setMessages((prev) => [...prev, { id, text, role, popped: false }]);
  
    // Phase 2: pop open into text bubble after it "floats" up
    setTimeout(() => {
      setMessages((prev) =>
        prev.map((m) => (m.id === id ? { ...m, popped: true } : m))
      );
    }, 800);
  };

  const sendMessage = async () => {
    if (!message.trim() || isLoading) return;
    const userText = message;
    setMessage("");
    addMessage(userText, "user");
    setIsLoading(true);
    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText }),
      });
      const data = await res.json();
      addMessage(data.response, "assistant");
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className = "page">
      <div className = "page-top">
        <div className= "theme-switcher">
          <span className = "theme-label"> Apply New Color Theme </span>
          <div className = "theme-options">
            <button className="btn-default" onClick={() => setTheme("theme-default")}>Default</button>
            <button className="btn-dark" onClick={() => setTheme("theme-dark")}>Dark</button>
          </div>
        </div>
      </div>

      <div className="messages-feed">
        {messages.map((m) => (
          <div key={m.id} className={`bubble-row ${m.role}`}>
            <div className={`bubble-outer ${m.popped ? "popped" : "floating"}`}>
              <div className="bubble-dot" />
              <div className="bubble-text">
                <ReactMarkdown>{m.text}</ReactMarkdown>
              </div>
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="bubble-row assistant">
            <div className="bubble-outer popped">
              <div className="bubble-dot" />
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
  );
}

export default App;