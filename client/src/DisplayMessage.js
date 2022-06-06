import React, { useState, useEffect } from "react";
import { Paper } from "@mui/material";
function DisplayMessage({ input, messageFlag, botMessage, botAnalysis }) {
  const [allInputs, setAllInputs] = useState([]);

  useEffect(() => {
    setAllInputs(input);
  }, [input]);

  return (
    <Paper sx={{ height: 300 }}>
      <Paper
        sx={{
          height: "fit-content",
          float: "left",
          backgroundColor: "blue",
          color: "white",
          margin: 2,
          padding: 3,
          borderRadius: "20px",
          position: "absolute",
          left: 100,
        }}
      >
        {allInputs}
      </Paper>

      <Paper
        sx={{
          height: "fit-content",
          float: "right",
          backgroundColor: "green",
          color: "white",
          margin: 2,
          padding: 3,
          borderRadius: "20px",
          position: "absolute",
          right: 100,
          top: 50,
        }}
      >
        {botMessage}
      </Paper>
      <Paper
        sx={{
          height: "fit-content",
          float: "right",
          backgroundColor: "green",
          color: "white",
          margin: 2,
          padding: 3,
          borderRadius: "20px",
          position: "absolute",
          right: 100,
          top: 120,
        }}
      >
        {botAnalysis}
      </Paper>
    </Paper>
  );
}
export default DisplayMessage;
