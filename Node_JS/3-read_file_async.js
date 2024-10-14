const fs = require('fs').promises;

// Asynchronous function to count students from a CSV file
function countStudents(path) {
  return fs.readFile(path, 'utf-8')
    .then((data) => {
      const lines = data.trim().split('\n');

      // Remove empty lines and the header
      const students = lines.filter((line, index) => line.trim() !== '' && index > 0);

      console.log(`Number of students: ${students.length}`);

      const fields = {};

      // Process each student line
      students.forEach((student) => {
        const [firstname, lastname, age, field] = student.split(',');

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      // Log the number of students in each field and their names
      for (const [field, names] of Object.entries(fields)) {
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
