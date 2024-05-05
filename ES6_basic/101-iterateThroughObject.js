export default function iterateThroughObject(reportWithIterator) {
  // empty string to hold the concatenated names.
  let employeeNames = '';

  // Iterate through the reportWithIterator object.
  for (const employee of reportWithIterator) {
    // append each employee's name followed by a pipe | separator to the string.
    employeeNames += `${employee} |`;
  }

  // Remove the last pipe from the string and return the result
  // so that the string does not end with an unnecessary separator.
  return employeeNames.slice(0, -1);
}
