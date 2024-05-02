// Export the function using ES6 default export syntax
export default function getListStudentIds(list) {
  // Check if the provided argument 'list' is an array
  if (!Array.isArray(list)) {
    // If 'list' is not an array, return an empty array
    return [];
  }
  // If 'list' is an array, use the map function to transform each student object in the array
  return list.map((student) => student.id);
  // The map function iterates over each element in the array, accessing the 'id' property of
  // each 'student' object and returns a new array containing only the ids
}
