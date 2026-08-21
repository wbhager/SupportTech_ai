import type { RefObject } from "react";
import { useAutoResizeTextarea } from "./useAutoResizeTextarea";

type ChatInputProps = {
  value: string;
  onChange: (value: string) => void;
  onSend: () => void;
  isLoading: boolean;
  textareaRef: RefObject<HTMLTextAreaElement | null>;
  setCursorMode: (mode: "button" | "text" | null) => void;
};

export function ChatInput({
  value,
  onChange,
  onSend,
  isLoading,
  textareaRef,
  setCursorMode,
}: ChatInputProps) {
  useAutoResizeTextarea(textareaRef, value);

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      onSend();
    }
  };

  return (
    <div className="page-bottom">
      <textarea
        ref={textareaRef}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={isLoading}
        placeholder="Type a message… (Enter to send, Shift+Enter for newline)"
        rows={1}
        className="chat-input"
        onMouseEnter={() => setCursorMode("text")}
        onMouseLeave={() => setCursorMode(null)}
      />
      <span
        onMouseEnter={() => setCursorMode("button")}
        onMouseLeave={() => setCursorMode(null)}
      >
        <button onClick={onSend} disabled={isLoading} className="send-btn">
          {isLoading ? "Sending…" : "Send"}
        </button>
      </span>
    </div>
  );
}
