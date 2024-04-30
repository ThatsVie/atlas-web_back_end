export default function createEmployeesObject(departmentName, employees) {
  // Return an object with a dynamic key using computed property names.
  // The key is the department name, and the value is the array of employees.
  return {
    [departmentName]: employees,
  };
}
