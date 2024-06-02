//libs
import express from 'express';

//routes
import { router } from './routes';


const server = express();
const PORT = process.env.PORT;

server.use(express.json());
server.use(router);

server.listen(PORT, () => {
    console.log('Server is running on port 3000');
}
);
