const express = require('express');

const app = express();
const PORT = process.env.PORT || 3000;
const NAME = process.env.NAME || "Usuario";

app.get('/', (req, res) => {
    res.send(`¡Hola ${NAME} desde Express.js!`);
});

app.listen(PORT, () => {
    console.log(`${NAME} Servidor corriendo en http://localhost:${PORT}`);
});