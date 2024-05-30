import * as http from 'http';
import { getListIndustries } from './controllers/mainController';

const server = http.createServer(async (req: http.IncomingMessage, res: http.ServerResponse) => {
    if (req.method === 'GET') {
        await getListIndustries(req, res);
    }
});

const PORT = process.env.PORT;
server.listen(PORT, async () => {
    console.log(`Server is running on port ${PORT}`);

})

