// Defines a function 'concatArrays' that takes three parameters: two arrays and one string.
export default function concatArrays(array1, array2, string) {
  // Return a new array combining:
  // ...array1: Spread all elements of the first array into the new array.
  // ...array2: Spread all elements of the second array into the new array.
  // ...string: Spread each character of the string into the new array.
  // This concatenates the elements of both arrays and the characters of the string into an array.
  return [...array1, ...array2, ...string];
}
