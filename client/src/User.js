import React, { useEffect, useState } from "react";
import TextField from "@mui/material/TextField";
import "./App.css";

function User({ setInput, setMessageFlag }) {
  //   const [messageAmount, setMessageAmount] = useState(userMessages + count);
  const [message, setMessage] = useState("");
  const handleChange = (e) => {
    setMessage(e.target.value);
  };

  const onKeyPress = (e) => {
    if (e.key === "Enter") {
      setInput(message);
      setMessageFlag(true);
      setMessage("");
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
