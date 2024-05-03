export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      // If boolean input is true resolve promise with an object with status and body
      resolve({ status: 200, body: 'Success' });
    } else {
      // If the boolean input is false, reject the promise with an error message
      reject(new Error('The fake API is not working currently'));
    }
  });
}
