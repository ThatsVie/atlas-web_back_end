export default function handleResponseFromAPI(promise) {
  // then and catch handlers to the promise
  return promise.then(() => {
    // executes if the promise resolves successfully
    console.log('Got a response from the API');
    // Return an object with status and body attributes
    return ({ status: 200, body: 'success' });
  }).catch(() => {
    // This block executes if the promise is rejected
    console.log('Got a response from the API');
    // Instead of returning new Error(), it should return an object
    // or throw an Error
    throw new Error('The fake API is not working currently');
  });
}
