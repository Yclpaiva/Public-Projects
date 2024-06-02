import { Router } from "express";


export const router = Router();

const userController = new UserController();
import UserController from './controllers/UserController';

router.get('/user', userController.getAllUsers)
router.post('/user', userController.createUser)
router.delete('/user', userController.removeUser)

