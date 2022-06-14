import React, { useState, useEffect } from "react";
import { Paper } from "@mui/material";
import "./App.css";
function DisplayMessage({ input, messageFlag, botMessage, botAnalysis }) {
  const [allInputs, setAllInputs] = useState([]);
  const [allBotInputs, setAllBotInpues] = useState([[]]);
  useEffect(() => {
    // if (allInputs.length > 5) {
    //   allInputs.shift();
    // }
    // if (botMessage.length > 5) {
    //   botMessage.shift();
    // }

    setAllInputs([...allInputs, input]);
    // setAllBotInpues([...allBotInputs, botMessage]);
  }, [input]);

  return (
    <div className="messages">
      {allInputs.map((userInput, index) => {
        return (
          <Paper
            sx={{
              height: "fit-content",
              float: "left",
              backgroundColor: "blue",
              color: "white",
              margin: 2,
              padding: 3,
              width: "fit-content",
              borderRadius: "20px",
              position: "relative",
              left: 60,
              top: 0 + index * 30,
            }}
          >
            {userInput}
          </Paper>
        );
      })}

      {/* {botMessage.map((message, index) => {
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
              left: 450,
              top: 50 + index * 110,
            }}
          >
            {message}
          </Paper>
        );
      })} */}
    </div>
  );
}
export default DisplayMessage;
