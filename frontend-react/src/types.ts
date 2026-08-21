export type Message = {
  id: number;
  text: string;
  role: "user" | "assistant";
  popped: boolean;
};

export type FlyingBubble = {
  id: number;
  role: "user" | "assistant";
  startX: number;
  startY: number;
  endX: number;
  endY: number;
};

export type Conversation = {
  conv_id: string;
  title: string;
};
