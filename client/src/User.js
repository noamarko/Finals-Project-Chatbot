import React, { useEffect, useState } from "react";
import TextField from "@mui/material/TextField";
import "./App.css";

function User({ setInput, setMessageFlag, allConvoInputs }) {
  const [message, setMessage] = useState("");
  const handleChange = (e) => {
    setMessage(e.target.value);
  };

  const onKeyPress = (e) => {
    if (e.key === "Enter") {
      if (/^[a-zA-Z, ?!']+$/.test(message)) {
        setInput(message);
        allConvoInputs["User"].push(message);
        setMessageFlag(true);
        setMessage("");
      } //print on user screen that the input is invalid
      else console.log("Input invalid");
    }
  };

  return (
    <TextField
      className="inputRounded"
      placeholder="Send a message"
      variant="outlined"
      size="large"
      sx={{ width: "100%", top: -5 }}
      onChange={handleChange}
      onKeyPress={onKeyPress}
      value={message}
    />
  );
}
export default User;
