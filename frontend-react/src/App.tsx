import { useState, useEffect } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [theme, setTheme] = useState("theme-default");

  useEffect(() => {
    document.documentElement.className = theme;
  }, [theme]);

  const sendMessage = async () => {
    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div className = "page">
      <div className = "page-top">
        <div className= "theme-switcher">
          <button onClick={() => setTheme("theme-default")}>Default</button>
          <button onClick={() => setTheme("theme-dark")}>Dark</button>
        </div>
      </div>

      <div className = "page-bottom">
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button onClick={sendMessage}>Send</button>
        <p>{response}</p>
      </div>
    </div>
  );
}

export default App;