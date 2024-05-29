import prompt from 'prompt'
import mainPrompt from './prompts/prompts-main.js'
import createQRCode from './services/qr-code/create.js'
import createPassword from './services/password/create.js'

(async function main() {
    prompt.get(mainPrompt, async (err, result) => {
        if (err) {
            console.error(err)
            return
        }
        if (result.select == 1) {
            await createQRCode()
        }
        if (result.select == 2) {
            console.log(await createPassword())
        }
    })

    prompt.start()

})()
