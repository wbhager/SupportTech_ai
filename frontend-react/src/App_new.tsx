import { useState, useEffect, useRef } from "react";
import type { Message, FlyingBubble, Conversation } from "./types";
import {
  sendChatMessage,
  fetchConversations,
  deleteConversation as deleteConversationApi,
  fetchConversationMessages,
} from "./api";
import { FlyingBubbleEl } from "./FlyingBubbleEl";
import { Sidebar } from "./Sidebar";
import { ChatInput } from "./ChatInput";
import { MessagesFeed } from "./MessagesFeed";
import { useCursorGlow } from "./useCursorGlow";

function App() {
  const [convId, setConvId] = useState<string>(() => crypto.randomUUID());
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [flyingBubbles, setFlyingBubbles] = useState<FlyingBubble[]>([]);
  const [theme, setTheme] = useState("theme-default");
  const [isLoading, setIsLoading] = useState(false);
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [bgMode, setBgMode] = useState<"reveal" | "colorSpot">("reveal");

  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const feedRef = useRef<HTMLDivElement>(null);
  const inputRectRef = useRef<DOMRect | null>(null);

  const { cursorRef, setCursorMode } = useCursorGlow();

  useEffect(() => {
    document.documentElement.className = theme;
  }, [theme]);

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
      fetchConversations()
        .then(setConversations)
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
      const response = await sendChatMessage(convId, userText);
      launchBubble(response, "assistant");
    } finally {
      setIsLoading(false);
    }
  };

  const handleDeleteConversation = async (targetConvId: string) => {
    await deleteConversationApi(targetConvId);
    setConversations((prev) => prev.filter((c) => c.conv_id !== targetConvId));
  };

  const handleLoadConversation = async (targetConvId: string) => {
    setConvId(targetConvId);
    const rawMessages = await fetchConversationMessages(targetConvId);
    setMessages(
      rawMessages.map((msg, index) => ({
        id: index,
        text: msg.content,
        role: msg.role as "user" | "assistant",
        popped: true,
      }))
    );
  };

  const newConversation = () => {
    setConvId(crypto.randomUUID());
    setMessages([]);
    setSidebarOpen(false);
  };

  return (
    <>
      {bgMode === "reveal" && <div className="hidden-reveal-layer" />}
      {bgMode === "colorSpot" && (
        <>
          <div className="grayscale-layer" />
          <div className="color-spot-layer" />
        </>
      )}
      <div className="glow" />
      <div ref={cursorRef} className="cursor" />
      <div className="page">
        {/* flying bubbles overlay */}
        {flyingBubbles.map((b) => (
          <FlyingBubbleEl key={b.id} bubble={b} />
        ))}

        <div className="page-top">
          <button
            onClick={() => setBgMode(bgMode === "reveal" ? "colorSpot" : "reveal")}
            onMouseEnter={() => setCursorMode("button")}
            onMouseLeave={() => setCursorMode(null)}
          >
            {bgMode === "reveal" ? "Switch to Color Spotlight" : "Switch to Hidden Reveal"}
          </button>
          <div className="theme-switcher">
            <span className="theme-label"> Apply New Color Theme </span>
            <div className="theme-options">
              <button
                className="btn-default"
                onClick={() => setTheme("theme-default")}
                onMouseEnter={() => setCursorMode("button")}
                onMouseLeave={() => setCursorMode(null)}
              >
                Default
              </button>
              <button
                className="btn-dark"
                onClick={() => setTheme("theme-dark")}
                onMouseEnter={() => setCursorMode("button")}
                onMouseLeave={() => setCursorMode(null)}
              >
                Dark
              </button>
            </div>
          </div>
        </div>

        <MessagesFeed
          messages={messages}
          isLoading={isLoading}
          feedRef={feedRef}
          messagesEndRef={messagesEndRef}
        />

        <ChatInput
          value={message}
          onChange={setMessage}
          onSend={sendMessage}
          isLoading={isLoading}
          textareaRef={textareaRef}
          setCursorMode={setCursorMode}
        />
      </div>

      <Sidebar
        isOpen={sidebarOpen}
        onToggle={() => setSidebarOpen(!sidebarOpen)}
        onNewConversation={newConversation}
        conversations={conversations}
        onSelectConversation={handleLoadConversation}
        onDeleteConversation={handleDeleteConversation}
      />
    </>
  );
}

export default App;
