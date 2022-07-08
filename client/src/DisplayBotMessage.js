import React, { useState, useEffect } from "react";
import { Paper } from "@mui/material";
import "./App.css";
function DisplayBotMessage({
  messageFlag,
  botMessage,
  botAnalysis,
  allConvoInputs,
}) {
  const [allBotInputs, setAllBotInpues] = useState([]);

  useEffect(() => {
    setAllBotInpues(botMessage);
  }, [botMessage]);

  return (
    <div className="botmessages">
      {Object.entries(allConvoInputs).map((key, value) => {
        console.log(allConvoInputs[key[0]]);
        if (key[0] === "Bot") {
          return allConvoInputs[key[0]].map((botMessage, index) => {
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
                {botMessage}
              </Paper>
            );
          });
        }
      })}
    </div>
  );
}
export default DisplayBotMessage;
