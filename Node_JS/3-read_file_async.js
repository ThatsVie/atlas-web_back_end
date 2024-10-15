const fs = require('fs').promises;

// Asynchronous function to count students from a CSV file
function countStudents(path) {
  return fs.readFile(path, 'utf-8')
    .then((data) => {
      const lines = data.trim().split('\n');

      // Remove empty lines and the header
      const students = lines.filter((line, index) => line.trim() !== '' && index > 0);

      let result = `Number of students: ${students.length}\n`;
      const fields = {};

      // Process each student line
      students.forEach((student) => {
        const [firstname, lastname, age, field] = student.split(',');

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      // Prepare the output for each field
      for (const [field, names] of Object.entries(fields)) {
        result += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      }

      // Return the formatted result as a string
      console.log(result.trim());
      return result.trim();
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
