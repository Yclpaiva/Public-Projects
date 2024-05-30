import { IncomingMessage, ServerResponse } from "http";
import { serviceListIndustries } from '../services/listIndustries';

export const getListIndustries = async (request: IncomingMessage, response: ServerResponse) => {
    const content = await serviceListIndustries();
    response.writeHead(200, { 'Content-Type': 'application/json' });
    response.end(JSON.stringify(content));
}
