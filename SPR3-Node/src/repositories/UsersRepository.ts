// [REPOSITORY : RESPONSÁVEL PELO ACESSO AO B.D.]

import { User } from "../entities/User";
import { EntityRepository, Repository } from "typeorm";

@EntityRepository(User)
class UsersRepository extends Repository<User> {

}

export { UsersRepository }