async function createPassword() {
    const password_lenght = process.env.LENGHT_INPUT;
    const include_lowercase = process.env.LOWER_CHECKBOX;
    const include_uppercase = process.env.UPPER_CHECKBOX;
    const include_symbols = process.env.SYMBOLS_CHECKBOX;
    const include_numbers = process.env.NUMBERS_CHECKBOX;

    const LOWER = "abcdefghijklmnopqrstuvwxyz"; //26
    const UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; //26
    const SYMBOLS = `!@#$%&_*=-+><?,.`; //16
    const NUMBERS = `0123456789`; //10
    let i = 0;
    let password = "";
    if ((include_numbers || include_symbols || include_lowercase || include_uppercase) && password_lenght > 0) {
        while (i < password_lenght) {
            let random_number = randomizer(4);
            //lowercase condition
            if (random_number == 0 && include_lowercase) {
                let selection = randomizer(LOWER.length);
                password += LOWER[selection];
                i += 1;
            }
            //uppercase condition
            if (random_number == 1 && include_uppercase) {
                let selection = randomizer(UPPER.length);
                password += UPPER[selection];
                i += 1;
            }
            //symbols condition
            if (random_number == 2 && include_symbols) {
                let selection = randomizer(SYMBOLS.length);
                password += SYMBOLS[selection];
                i += 1;
            }
            //numbers condition
            if (random_number == 3 && include_numbers) {
                let selection = randomizer(NUMBERS.length);
                password += NUMBERS[selection];
                i += 1;
            }

        }
    } else {
        return "";
    }
    return password;


    function randomizer(scale) {
        let number = Math.floor(Math.random() * scale);
        return number;
    }

}


export default createPassword;
