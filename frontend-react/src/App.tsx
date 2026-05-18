import { useState, useEffect , useRef} from "react";
import ReactMarkdown from "react-markdown";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [theme, setTheme] = useState("theme-default");
  const [isLoading, setIsLoading] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    document.documentElement.className = theme;
  }, [theme]);

  useEffect(() => {
    const el = textareaRef.current;
    if (!el) return;
    el.style.height = "auto";
    el.style.height = el.scrollHeight + "px";
  }, [message]);

  const sendMessage = async () => {
    if (!message.trim() || isLoading) return; // guard
    setIsLoading(true);
    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });
      const data = await res.json();
      setResponse(data.response);
      setMessage(""); // clear after send
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

      <div className="page-bottom">
        {/* replace <input> with <textarea> */}
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
        <ReactMarkdown>{response}</ReactMarkdown>
      </div>
    </div>
  );
}

export default App;