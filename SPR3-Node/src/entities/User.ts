// FLUXO:
// http => controller => service => repository => database

import { Entity, PrimaryColumn, Column, CreateDateColumn } from "typeorm"
import { v4 as uuid } from "uuid";

@Entity("users")
class User {

    // DECORATORS => transformar classe em tabela no B.D.
    @PrimaryColumn() 
    id: string;

    @Column()
    email: string;

    @CreateDateColumn()
    createdAt: Date;

    constructor() {
        if (!this.id) {
            this.id = uuid();
        }
    }

}

export { User }