/**
 * Defines function countStudents that reads a CSV file,
 * counts the total number of students, and logs the number of students 
 * in each field. If the file cannot be loaded, 
 * it throws an error with the message "Cannot load the database."
 */
const fs = require('fs');

// Function to count students from a CSV file
function countStudents(path) {
  try {
    // Read file synchronously
    const data = fs.readFileSync(path, 'utf-8').trim();
    const lines = data.split('\n');

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
  } catch (error) {
    // If an error occurs (file not found), throw an error
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
