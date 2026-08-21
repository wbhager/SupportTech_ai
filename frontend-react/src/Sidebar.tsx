import type { Conversation } from "./types";

type SidebarProps = {
  isOpen: boolean;
  onToggle: () => void;
  onNewConversation: () => void;
  conversations: Conversation[];
  onSelectConversation: (convId: string) => void;
  onDeleteConversation: (convId: string) => void;
};

export function Sidebar({
  isOpen,
  onToggle,
  onNewConversation,
  conversations,
  onSelectConversation,
  onDeleteConversation,
}: SidebarProps) {
  return (
    <div className="sidebar-container">
      <div className="sidebar-buttons">
        <button className="sidebar-toggle" onClick={onToggle}>
          {isOpen ? "✕" : "💬"}
        </button>
        <button
          className={`new-conv-btn ${isOpen ? "new-conv-btn-visible" : ""}`}
          onClick={onNewConversation}
        >
          +
        </button>
      </div>
      {isOpen && (
        <div className="sidebar-panel">
          {conversations.map((conv, index) => (
            <div
              key={conv.conv_id}
              className="sidebar-item"
              style={{ animationDelay: `${0.05 + index * 0.1}s` }}
            >
              <span onClick={() => onSelectConversation(conv.conv_id)}>
                {conv.title}
              </span>
              <button onClick={() => onDeleteConversation(conv.conv_id)}>✕</button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
