import { Request, Response } from "express"
import { UsersServices } from "../services/UsersServices"

// CONTROLLER => Lida com o HTTP, recebe a requisição e passa para service

class UsersController {
    async create(request: Request, response: Response): Promise<Response> {

        const { email } = request.body;
        const usersServices = new UsersServices();
        const user = await usersServices.create(email);

        return response.json(user);
    }
}

export { UsersController };