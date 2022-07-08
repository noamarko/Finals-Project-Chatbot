import React, { useState, useEffect } from "react";
import { Paper } from "@mui/material";
import "./App.css";
function DisplayMessage({
  input,
  messageFlag,
  botMessage,
  botAnalysis,
  allConvoInputs,
}) {


  return (
    <div className="messages">
      {Object.entries(allConvoInputs).map((key, value) => {
        console.log(allConvoInputs[key[0]]);
        if (key[0] === "User") {
          return allConvoInputs[key[0]].map((userMessage, index) => {
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
                  top: index * 30,
                }}
              >
                {userMessage}
              </Paper>
            );
          });
        }
      })}
    </div>
  );
}
export default DisplayMessage;
