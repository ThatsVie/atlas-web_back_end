export default function getStudentIdsSum(studentList) {
  // reduce method to calculate the sum of all student IDs
  // reduce method takes parameter sum and student
  return studentList.reduce((sum, student) => sum + student.id, 0);
  // Initialize the sum with 0 to handle the case where the array is empty
}
