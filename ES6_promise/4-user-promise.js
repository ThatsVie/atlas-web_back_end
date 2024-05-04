export default function signUpUser(firstName, lastName) {
  // return resolved Promise immediately
  return Promise.resolve({
    firstName, // shorthand property
    lastName, // shorthand property
  });
}
