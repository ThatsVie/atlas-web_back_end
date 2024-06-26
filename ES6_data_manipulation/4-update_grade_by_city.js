export default function updateStudentGradeByCity(students, city, updatedGrades) {
  // Check that students parameter is an array
  if (!Array.isArray(students)) {
    // If students is not an array, return empty array to handle errors
    return [];
  }

  // Filter the list of students to include only those who are located in the specific city
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      // For each student in the filtered list, find a matching grade object
      const studentGrade = updatedGrades.find((grade) => grade.studentId === student.id);

      // Construct a new student object that includes all properties of the original student
      // and adds a grade property. If no matching grade is found, assign 'N/A' as the grade
      return {
        ...student,
        grade: studentGrade ? studentGrade.grade : 'N/A',
      };
    });
}
