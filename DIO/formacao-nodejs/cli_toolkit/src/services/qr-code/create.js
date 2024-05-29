import prompt from 'prompt';
import promptQRCode from "../../prompts/prompt-qrcode.js";
import handler from './handle.js';

async function createQRCode() {
    prompt.get(promptQRCode, async (err, result) => {
        if (err) {
            console.error(err);
            return;
        }
        handler(err, result);
    });

    prompt.start();

}


export default createQRCode;
