import { User } from '../utils/User'

let dbProd: User[] = []


export default class UserService {

    private db: User[]

    constructor(database: User[] = dbProd) {
        this.db = database
    }

    setDb(database: User[]) {
        this.db = database
    }

    async create(user: User): Promise<boolean> {
        console.log(user)
        this.db.push(user)
        console.log(this.db)
        return true
    }

    async getAllUsers(): Promise<User[]> {
        return this.db
    }

    async removeUser(email: string): Promise<boolean> {
        for (let i = 0; i < this.db.length; i++) {
            if (this.db[i].email === email) {
                this.db.splice(i, 1)
                return true
            }
        }
        return false
    }

}
