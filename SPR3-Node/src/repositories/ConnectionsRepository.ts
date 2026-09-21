import { Connection } from "../entities/Connection";
import { Repository, EntityRepository } from "typeorm";

@EntityRepository(Connection)
class ConnectionsRepository extends Repository<Connection> {

}

export { ConnectionsRepository };