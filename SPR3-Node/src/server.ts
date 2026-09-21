import "./websocket/client";
import { http } from "./http";

http.listen(3333, () => console.log("Server running on port 3333"));

