import { makeMockResponse } from "../__mocks__/mockResponse";
import UserController from "../controllers/UserController";
import UserService from "../services/UserService";
import { Request } from "express";


describe('UserController', () => {
    const mockUserService: Partial<UserService> = new UserService();
    const userController: UserController = new UserController(mockUserService as UserService);

    it('deve adicionar um usuário', async () => {
        const mockRequest = {
            body: {
                name: 'John Doe',
                email: 'johndoe@john.com',
                password: '123456'
            }
        } as Request;
        const mockResponse = makeMockResponse();
        const response = await userController.createUser(mockRequest, mockResponse);
        expect(response.state?.status).toBe(200);
    });

    it('deve retornar todos os usuários', async () => {
        const mockRequest = {} as Request;

        const mockResponse = makeMockResponse();
        const response = await userController.getAllUsers(mockRequest, mockResponse);
        expect(response.state?.status).toBe(200);
    })

});
