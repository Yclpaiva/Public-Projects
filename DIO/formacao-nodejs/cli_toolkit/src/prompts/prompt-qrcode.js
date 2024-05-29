
const promptQRCode = [
    {
        name: "link",
        description: "Enter the link to the QR code",

    },
    {
        name: "type",
        description: "Enter the type of the QR code (1- NORMAL ou (2- CLI",
        pattern: /^[1-2]*$/,
        mmessage: "Please enter 1 or 2",
        required: true
    },
];


export default promptQRCode;
