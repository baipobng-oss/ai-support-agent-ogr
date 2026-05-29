import { useState } from "react";
import API from "./api";

function App() {
  const [reply, setReply] = useState("");

  const askAI = async () => {
    try {
      const res = await API.get("/chat");
      setReply(res.data.reply);
    } catch (err) {
      console.error(err);
      setReply("Error connecting to backend");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>AI Support Agent</h1>

      <button onClick={askAI}>
        Ask AI
      </button>

      <p>{reply}</p>
    </div>
  );
}

export default App;