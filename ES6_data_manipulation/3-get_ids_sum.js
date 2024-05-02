// Export the function using ES6 default export syntax
export default function getStudentIdsSum(studentList) {
  // Use the 'reduce' method to calculate the sum of all student IDs
  // The 'reduce' method takes parameter 'sum' and the current element 'student'
  return studentList.reduce((sum, student) => sum + student.id, 0);
  // Initialize the sum with 0 to handle the case where the array is empty
}
