import React, { useEffect, useState, useRef } from "react";
import TextField from "@mui/material/TextField";
import "./App.css";
import Bot from "./Bot";
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

  const messagesRef = useRef(null);

  const sendMessageToBot = async () => {
    try {
      let response = await api.get(`/?input=${input}`);
      console.log(response);
      if (response.status === 200) {
        setMessageFlag(false);
        setBotMessage([...botMessage, response.data]);
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
        console.log(analyze);
        if (analyze.status === 200) {
          setMessageFlag(false);
          setBotAnalysis([...botAnalysis, analyze.data]);
        }
      } catch (e) {
        console.log(e);
      }
    }, 15000);
    return () => clearInterval(interval);
  }, [input, botAnalysis]);

  return (
    <>
      <div className="convo-handler">
        <div ref={messagesRef} style={{ height: "0px" }} />

        {input.length > 0 && (
          <DisplayMessage
            input={input}
            botMessage={botMessage}
            // botAnalysis={botAnalysis}
            messageFlag={messageFlag}
          />
        )}
        {/* || botAnalysis.length > 0 */}
        {botMessage.length > 0 && (
          <DisplayBotMessage
            botMessage={botMessage}
            botAnalysis={botAnalysis}
            messageFlag={messageFlag}
          />
        )}
      </div>
      <User setInput={setInput} setMessageFlag={setMessageFlag} />
    </>
  );
};

export default App;
