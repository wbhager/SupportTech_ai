import type { RefObject } from "react";
import ReactMarkdown from "react-markdown";
import type { Message } from "./types";

type MessagesFeedProps = {
  messages: Message[];
  isLoading: boolean;
  feedRef: RefObject<HTMLDivElement | null>;
  messagesEndRef: RefObject<HTMLDivElement | null>;
};

export function MessagesFeed({
  messages,
  isLoading,
  feedRef,
  messagesEndRef,
}: MessagesFeedProps) {
  return (
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
  );
}
