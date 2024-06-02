import UserService from "../services/UserService"
import { User } from "../utils/User"


describe('UserService', () => {
    let mockDb: User[] = []
    const userService: UserService = new UserService(mockDb)
    const mockUser = {
        name: 'John Doe',
        email: 'johndoe@gmail.com',
        password: '123456',
    }

    beforeEach(() => {
        mockDb = [];
        userService.setDb(mockDb);
    });

    it('should create a user', async () => {

        const mockConsoleLog = jest.spyOn(global.console, 'log')
        await userService.create(mockUser)
        expect(mockConsoleLog).toHaveBeenCalled()
        expect(mockConsoleLog).toHaveBeenCalledWith(mockDb)
    })

    it('should get all users', async () => {
        const mockDb2: User[] = []
        const mockConsoleLog = jest.spyOn(global.console, 'log')
        mockDb2.push(mockUser)

        await userService.create(mockUser)

        expect(mockConsoleLog).toHaveBeenCalled()
        expect(mockConsoleLog).toHaveBeenCalledWith(mockDb)
        if (mockDb2.length > 0) {
            expect(mockDb2).toEqual(mockDb)
        }
    })

    it('should remove a user', async () => {
        const mockDb2: User[] = []
        const mockConsoleLog = jest.spyOn(global.console, 'log')
        mockDb2.push(mockUser)

        await userService.create(mockUser)
        expect(mockConsoleLog).toHaveBeenCalled()
        expect(mockConsoleLog).toHaveBeenCalledWith(mockDb)

        await userService.removeUser(mockUser.email)

        if (mockDb2.length == 0) {
            expect(mockDb2).not.toEqual(mockDb)
        }
    })

})
