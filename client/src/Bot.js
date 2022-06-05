import React, { useEffect, useState } from "react";
import TextField from "@mui/material/TextField";

function Bot() {
  const [input, setInput] = useState();

  const handleChange = (e) => {
    console.log(e);
  };
  return <TextField onChange={handleChange}>{input}</TextField>;
}
export default Bot;
