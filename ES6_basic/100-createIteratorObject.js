export default function createIteratorObject(report) {
  // Create an iterator object
  const iterator = {
    // Symbol.iterator method returns the iterator object
    [Symbol.iterator]() {
      let index = 0; // track the current index of the employee array
      const allEmployees = []; // array to store all employees from each department

      // make the list of employees from each department into a single array
      Object.values(report.allEmployees).forEach((department) => {
        allEmployees.push(...department);
      });

      return {
        // next method defines how to traverse through the iterator
        next() {
          if (index < allEmployees.length) {
            const employee = allEmployees[index]; // Get the employee at the current index
            index += 1; // Increment the index to move to the next employee
            return { value: employee, done: false };
          }
          // When all employees are traversed, mark the iterator as complete
          return { done: true };
        },
      };
    },
  };

  return iterator;
}
