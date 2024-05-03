import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  // Promise.all is used to handle multiple promises at once. Takes an array of promises.
  return Promise.all([uploadPhoto(), createUser()])
    .then(([uploadPhoto, createUser]) => {
      // executes if all promises resolve successfully.
      // The results of the promises are destructured from the array.
      // uploadPhoto and createUser are expected to be objects with properties outlined.
      console.log(`${uploadPhoto.body} ${createUser.firstName} ${createUser.lastName}`);
      // console logs a string that combines the body of the uploadPhoto response
      // and the firstName and lastName from the createUser response.
    })
    .catch(() => {
      // catch block handles any errors from either promise.
      // If any fails, catches the error and logs Signup system offline
      console.log('Signup system offline');
    });
}
