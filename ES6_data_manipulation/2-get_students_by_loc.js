// Export the function using ES6 default export syntax
export default function getStudentsByLocation(studentList, city) {
  // Check if 'studentList' is actually an array using the prototype comparison
  if (!Array.isArray(studentList)) {
    // Return an empty array if 'studentList' is not an array
    return [];
  }

  // Use 'filter' method to create a new array containing students who are in the specified city
  return studentList.filter((student) => student.location === city);
  // The 'filter' method iterates over each student in 'studentList',
  // and includes them in the new array only if their 'location' matches the 'city' parameter
}
