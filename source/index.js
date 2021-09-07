const { readFileSync } = require("fs");

const data = readFileSync("../secrets.txt").toString("utf-8");
let [username, password] = data.split("\n");

username = username.split("=")[1];
password = password.split("=")[1];