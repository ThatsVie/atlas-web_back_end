export default function appendToEachArrayValue(array, appendString) {
  // Using const for block scope and because the reference to newArray isn't reassigned
  const newArray = []; //  new array to store modified values

  for (const value of array) {
    // Directly iterate over the values of the array using const since value
    // isn't reassigned within the loop
    newArray.push(appendString + value); // Append the string and push to new array
  }

  return newArray; // Return the newly constructed array
}
