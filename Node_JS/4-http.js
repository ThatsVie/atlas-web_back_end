const http = require('http');

// HTTP server listening on port 1245
const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;
