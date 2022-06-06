import React, { useEffect, useState } from "react";
import TextField from "@mui/material/TextField";
import "./App.css";
import Bot from "./Bot";
import User from "./User";
import DisplayMessage from "./DisplayMessage";
import api from "./api";
import { inputUnstyledClasses } from "@mui/base";
const App = () => {
  const [input, setInput] = useState("");
  const [messageFlag, setMessageFlag] = useState(false);
  const [botMessage, setBotMessage] = useState();
  const [botAnalysis, setBotAnalysis] = useState();
  const sendMessageToBot = async () => {
    try {
      let response = await api.get(`/?input=${input}`);
      console.log(response);
      if (response.status === 200) {
        setMessageFlag(false);
        setBotMessage(response.data);
      }
    } catch (e) {
      console.log(e);
    }
  };


  useEffect(() => {
    if (input.length > 1) sendMessageToBot();

    const interval =  setInterval( async () => {
      try{
      let analyze = await api.get("/analyze");
      console.log(analyze);
      if (analyze.status === 200) {
        setMessageFlag(false);
        setBotAnalysis(analyze.data);
      }
    }
    catch(e){
      console.log(e)
    }
    }, 15000);
    return () => clearInterval(interval);
  }, [input]);

  return (
    <>
      <div
      // style={{
      //   height: 1000,
      // }}
      >
        <DisplayMessage
          input={input}
          botMessage={botMessage}
          botAnalysis={botAnalysis}
          messageFlag={messageFlag}
        />
      </div>
      <div
        style={{
          float: "left",
          position: "absolute",
          bottom: 10,
          width: "100%",
        }}
      >
        <User setInput={setInput} setMessageFlag={setMessageFlag} />
      </div>
      {/* <div style={{ float: "left", backgroundColor: "green" }}>
        <Bot />
      </div> */}
    </>
  );
};

export default App;
