const http = require('http');
const url = require('url');
const countStudents = require('./3-read_file_async');

// HTTP server listening on port 1245
const app = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);

  // Handle root endpoint
  if (parsedUrl.pathname === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  }

  // Handle /students
  else if (parsedUrl.pathname === '/students') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.write('This is the list of our students\n');

    // Get the database path from the arguments
    const databasePath = process.argv[2];

    if (!databasePath) {
      res.end('Cannot load the database');
      return;
    }

    // Call the countStudents function to process the CSV file
    countStudents(databasePath)
      .then((output) => {
        res.write(`${output}\n`);
        res.end();
      })
      .catch((err) => {
        res.end(err.message);
      });
  }

  // Handle any other path
  else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
