const express = require("express");
const app = express();

app.use("/", express.static("/home/bone/Downloads/")); // replace ./files with the path to the directory holding the file/files you want to make available

app.listen(80);
