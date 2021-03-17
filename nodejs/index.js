const express = require("express");
const app = express();

app.get("/staj", (req, res) => {
  res.send("Hello World from Node.js!\n");
});

app.listen(3000, () => console.log(`running on 3000`));
