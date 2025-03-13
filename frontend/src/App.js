import React, { useState } from "react";
import axios from "axios";

function App() {
  const [userInput, setUserInput] = useState("");
  const [story, setStory] = useState("");

  const generateStory = async () => {
    const response = await axios.get(`http://127.0.0.1:8000/api/generate_story/?user_input=${userInput}`);
    setStory(response.data.story);
  };

  return (
    <div>
      <h1>AI Interactive Story</h1>
      <input type="text" value={userInput} onChange={(e) => setUserInput(e.target.value)} />
      <button onClick={generateStory}>Continue Story</button>
      <p>{story}</p>
    </div>
  );
}

export default App;