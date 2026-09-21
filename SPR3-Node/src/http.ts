import path from "path";
import express from "express";
import { createServer } from "http";
import { Server, Socket } from "socket.io";

import "./database";
import { routes } from "./routes";

const app = express();
app.use(express.static(path.join(__dirname, "..", "public")));
app.set("views", path.join(__dirname, "..", "public"));
app.engine("html", require("ejs").renderFile);
app.set("view engine", "html");

app.get("/pages/client", (request, response) => {
    return response.render("html/client.html")
});


const http = createServer(app); // protocolo HTTP
const io = new Server(http);    // protocolo WS - Web Socket

io.on("connection", (socket: Socket) => {
    console.log("IO connection established ", socket.id);
}); 

app.use(express.json());
app.use(routes);

export { http, io };