import { Request, Response } from 'express';
import UserService from '../services/UserService';


interface stateResponse {
    status?: number;
    json?: object;
}
interface ResponseState {
    state?: stateResponse;
    status?: any;
    json?: object;
}

class UserController {

    userService: UserService;

    constructor(usrService: UserService = new UserService()) {
        this.userService = usrService;
    }

    createUser = async (req: Request, res: Response): Promise<ResponseState> => {
        console.log(req.body);
        if (!req.body.name || !req.body.email) {
            return res.status(400).json({ message: 'Missing fields' });
        }
        console.log(await this.userService.create(req.body));
        return res.status(200).json({ message: 'User created' });
    }

    getAllUsers = async (_: Request, res: Response): Promise<ResponseState> => {
        return res.status(200).json(await this.userService.getAllUsers());
    }

    removeUser = async (req: Request, res: Response): Promise<ResponseState> => {
        if (!req.body.email) {
            return res.status(400).json({ message: 'Missing fields' });
        }
        if (await this.userService.removeUser(req.body.email)) {
            return res.status(200).json({ message: 'User removed' });
        }
        return res.status(404).json({ message: 'User not found' });
    }

}

export default UserController;
