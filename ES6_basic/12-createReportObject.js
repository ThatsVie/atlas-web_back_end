// Define a function named 'createReportObject' that accepts 'employeesList' as an argument.
// 'employeesList' is an object, keys are department names and values are arrays of employee names.
export default function createReportObject(employeesList) {
  return {
    // 'allEmployees' key contains a copy of the 'employeesList'.
    // spread syntax to include all existing properties of 'employeesList' into 'allEmployees',
    // maintaining original structure but within scope of object that provides additional methods.
    allEmployees: {
      ...employeesList,
    },

    // method 'getNumberOfDepartments' calculates number of departments in 'allEmployees' object.
    // doesnt take parameters, enhancing encapsulation by using 'this' to refer to current object.
    // using 'this.allEmployees', ensures method operates solely on internal state of the object,
    // which encapsulates the functionality within the object itself.
    getNumberOfDepartments() {
      // Use 'Object.keys' to extract the keys from 'this.allEmployees' and return their count.
      // computes the length of the keys array, which corresponds to the number of departments.
      // use of 'this' ensures that method remains functional and correct irrespective of how
      // external state changes,as it relies only on its own internal state.
      return Object.keys(this.allEmployees).length;
    },
  };
}
