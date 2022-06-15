import React, { useState, useEffect } from "react";
import { Paper } from "@mui/material";
import "./App.css";
function DisplayBotMessage({ messageFlag, botMessage, botAnalysis }) {
  const [allBotInputs, setAllBotInpues] = useState([[]]);
  useEffect(() => {
    // if (allInputs.length > 5) {
    //   allInputs.shift();
    // }
    // if (botMessage.length > 5) {
    //   botMessage.shift();
    // }
    setAllBotInpues([...allBotInputs, botMessage]);
  }, [botMessage]);
  

  return (
    <div className="botmessages">
      {botMessage.map((message, index) => {
        return (
          <Paper
            sx={{
              height: "fit-content",
              float: "right",
              backgroundColor: "green",
              color: "white",
              margin: 2,
              padding: 3,
              width: "fit-content",
              borderRadius: "20px",
              position: "relative",
              left: 250,
              top: 30 + index * 30,
            }}
          >
            {message}
          </Paper>
        );
      })}
    </div>
  );
}
export default DisplayBotMessage;
