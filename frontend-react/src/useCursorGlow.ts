import { useEffect, useRef } from "react";

export function useCursorGlow() {
  const cursorRef = useRef<HTMLDivElement>(null);

  // ── custom cursor + mouse-following glow
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      document.documentElement.style.setProperty("--x", `${e.clientX}px`);
      document.documentElement.style.setProperty("--y", `${e.clientY}px`);
    };
    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, []);

  const setCursorMode = (mode: "button" | "text" | null) => {
    const el = cursorRef.current;
    if (!el) return;
    el.classList.remove("mode-button", "mode-text");
    if (mode) el.classList.add(`mode-${mode}`);
  };

  return { cursorRef, setCursorMode };
}
