export default function cleanSet(set, startString) {
  // Check if 'startString' is empty or not a string, and return an empty string if true
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  // Convert the set to an array using Array.from, to use array methods like filter and map
  return Array.from(set)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');
  // Use the 'startsWith' method to filter out the values that begin with 'startString'
  // For each filtered value, slice off 'startString' part to keep the remainder of the string
  // Join all the strings with a dash ('-') to form a single string
}
