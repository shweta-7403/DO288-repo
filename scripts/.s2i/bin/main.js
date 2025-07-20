const http = require('http');
const port = process.env.SERVER_PORT || 8081;

const server = http.createServer((req, res) => {
  res.end("✅ App Running on PORT: " + port);
});

server.listen(port, () => {
  console.log(`🚀 Server running on http://0.0.0.0:${port}`);
});

