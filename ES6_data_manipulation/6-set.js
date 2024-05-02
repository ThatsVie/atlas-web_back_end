export default function setFromArray(array) {
  // Create a new Set from the provided array
  // The Set constructor accepts an iterable, and an array is an example of an iterable
  // When a new Set is created from an array, all duplicate values in the array are automatically
  // removed since a Set in JavaScript is a collection of unique values only.
  return new Set(array);
}
