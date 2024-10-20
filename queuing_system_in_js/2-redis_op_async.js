import { createClient, print } from 'redis'; 
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Function to set a new key-value pair in Redis.
 * @param {string} schoolName - The name of the key to set in Redis.
 * @param {string} value - The value to associate with the key.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

/**
 * Function to retrieve and display the value of a key from Redis using async/await.
 * @param {string} schoolName - The name of the key to retrieve from Redis.
 */
async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client); // Convert client.get to a promise-based function
  try {
    const reply = await getAsync(schoolName);  // handle the retrieval
    console.log(reply);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}:`, err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
