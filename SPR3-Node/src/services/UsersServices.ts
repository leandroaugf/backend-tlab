import { User } from "../entities/User";
import { getCustomRepository, Repository } from "typeorm"
import { UsersRepository } from "../repositories/UsersRepository"

// [REGRAS DA APLICAÇÃO]
// EXEMPLO: Criar um usuário - O que é necessário para um user ser criado
class UsersServices {
    
    private usersRepository : Repository<User>;

    constructor() {
        this.usersRepository = getCustomRepository(UsersRepository);
    }

    async findByEmail(email: string) {
        const user = await this.usersRepository.findOne({
            email
        });

        return user;
    }

    async create(email: string) {

        // Se já existe => retorna o user
        const userExists = await this.usersRepository.findOne({
            email
        });
        if (userExists) return userExists;
        
        // Se não existe => salva no B.D.
        const user = this.usersRepository.create({
            email
        })
        await this.usersRepository.save(user)
        return user;
    }
}

export { UsersServices }