import { Router } from "express";
import { UsersController } from "./controller/UsersController";
import { SettingsController } from "./controller/SettingsController";
import { MessagesController } from "./controller/MessagesController";

const routes = Router();

const settingsController = new SettingsController();
const usersController = new UsersController();
const messagesController = new MessagesController();

routes.post("/users", usersController.create);
routes.get("/settings/:username", settingsController.findByUsername);
routes.put("/settings/:username", settingsController.update);

routes.post("/messages", messagesController.create);
routes.get("/messages/:id", messagesController.showByUser);

export { routes };