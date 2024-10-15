const fs = require('fs').promises;

// Read the database asynchronously
async function readDatabase(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf-8');
    const lines = data.trim().split('\n');
    const fields = {};

    lines.slice(1).forEach((line) => {
      const [firstname, lastname, age, field] = line.split(',');
      if (field && firstname) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
    });

    return fields;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = readDatabase;
