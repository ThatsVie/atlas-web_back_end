import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  // Array of promises from signUpUser and uploadPhoto functions
  const promises = [signUpUser(firstName, lastName), uploadPhoto(fileName)];
  // handle both promises together
  return Promise.allSettled(promises).then((results) => results.map((result) => ({
    // Each result is processed to format the output
    status: result.status,
    // Check status to decide what to display- the result value or an error message
    value: result.status === 'fulfilled' ? result.value : `Error: ${result.reason.message}`,
  })));
}
