const mainPrompts = [
    {
        name: "select",
        description: "Escolha a ferramenta (1 - QRCODE) ou (2 - PASSWORD) ",
        pattern: /^[1-2]$/,
        message: 'Selecione 1 ou 2',
        required: true
    }

];

export default mainPrompts;
