export default function hasValuesFromArray(set, array) {
  // Use the every method on the array to test whether all elements pass the test
  return array.every((value) => set.has(value));
  // For each element in the array check if the set contains this element
  // The has method of Set checks for the presence of an element and returns
  // true if the element is found in the Set
}
