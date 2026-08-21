import type { Conversation } from "./types";

const BASE_URL = "http://localhost:8000";

export async function sendChatMessage(convId: string, message: string): Promise<string> {
  const res = await fetch(`${BASE_URL}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ conv_id: convId, message }),
  });
  const data = await res.json();
  return data.response;
}

export async function fetchConversations(): Promise<Conversation[]> {
  const res = await fetch(`${BASE_URL}/conversations`);
  const data = await res.json();
  return data.conversations;
}

export async function deleteConversation(convId: string): Promise<void> {
  await fetch(`${BASE_URL}/conversations/${convId}`, { method: "DELETE" });
}

export async function fetchConversationMessages(
  convId: string
): Promise<{ role: string; content: string }[]> {
  const res = await fetch(`${BASE_URL}/conversations/${convId}/messages`);
  const data = await res.json();
  return data.messages;
}
