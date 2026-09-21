import { io } from "../http";
import { UsersServices } from "../services/UsersServices";
import { MessagesService } from "../services/MessagesServices";
import { ConnectionsService } from "../services/ConnectionsService";

interface IParams {
    text: "string",
    email: "string"
}

io.on("connection", (socket) => {
    const usersService = new UsersServices();
    const messagesService = new MessagesService();
    const connectionsService = new ConnectionsService();

    socket.on("client_first_access", async (params, callback) => {
        console.log("CLIENT_FIRST_ACCESS:", params);
        const socket_id = socket.id;
        const { text, email } = params;
        let user_id: string;

        console.log("ANTES DO FIND BY EMAIL");

        const userExists = await usersService.findByEmail(email);

        console.log("DEPOIS DO FIND BY EMAIL:", userExists);

        if (!userExists) {
            const user = await usersService.create(email);

            await connectionsService.create({
                socket_id,
                user_id: user.id
            });
            user_id = user.id;

        } else {

            user_id = userExists.id;
            const connection = await connectionsService.findUserById(userExists.id);
            if (!connection) {

                await connectionsService.create({
                    socket_id, 
                    user_id: userExists.id
                });
                

            } else {

                connection.socket_id = socket_id;
                await connectionsService.create(connection);
                
            }
        }

        await messagesService.create({
            admin_id: null,
            text,
            user_id
        });

    });
});