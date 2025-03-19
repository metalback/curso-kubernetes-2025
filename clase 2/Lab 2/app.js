require('dotenv').config();

const http = require("http");
const nombre = process.env.NOMBRE || "Usuario";
const server = http.createServer((req, res) => {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end(`Hola, ${nombre}!`);
});
server.listen(3000, () => {
    console.log("Server running at http://localhost:3000/");
});