import React, { useEffect, useState, useRef } from "react";
import TextField from "@mui/material/TextField";
import "./App.css";
import User from "./User";
import DisplayMessage from "./DisplayMessage";
import DisplayBotMessage from "./DisplayBotMessage";
import api from "./api";
import { inputUnstyledClasses } from "@mui/base";
const App = () => {
  const [input, setInput] = useState("");
  const [messageFlag, setMessageFlag] = useState(false);
  const [botMessage, setBotMessage] = useState([]);
  const [botAnalysis, setBotAnalysis] = useState([]);
  const [allConvoInputs, setAllConvoInputs] = useState({ User: [], Bot: [] });
  
  const messagesRef = useRef(null);

  const sendMessageToBot = async () => {
    try {
      let response = await api.get(`/?input=${input}`);

      if (response.status === 200) {
        setMessageFlag(false);

        allConvoInputs["Bot"].push(response.data);
      }
    } catch (e) {
      console.log(e);
    }
  };

  const scrollToBottom = () => {
    if (messagesRef) messagesRef.current.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    if (messageFlag) sendMessageToBot();
    scrollToBottom();
    const interval = setInterval(async () => {
      try {
        let analyze = await api.get("/analyze");
        if (analyze.status === 200) {
          setMessageFlag(false);
          allConvoInputs["Bot"].push(analyze.data);
          setAllConvoInputs((prevConvo) => ({
            ...prevConvo,
            Bot: allConvoInputs["Bot"],
          }));
        }
      } catch (e) {
        console.log(e);
      }
    }, 15000);
    return () => clearInterval(interval);
  }, [input]);

  return (
    <>
      <div className="convo-handler">
        <div ref={messagesRef} style={{ height: "0px" }} />

        {allConvoInputs["User"].length > 0 && (
          <DisplayMessage
            input={input}
            botMessage={botMessage}
            messageFlag={messageFlag}
            allConvoInputs={allConvoInputs}
          />
        )}
        {allConvoInputs["Bot"].length > 0 && (
          <DisplayBotMessage
            botMessage={botMessage}
            botAnalysis={botAnalysis}
            messageFlag={messageFlag}
            allConvoInputs={allConvoInputs}
          />
        )}
      </div>
      <User
        allConvoInputs={allConvoInputs}
        setInput={setInput}
        setMessageFlag={setMessageFlag}
      />
    </>
  );
};

export default App;
