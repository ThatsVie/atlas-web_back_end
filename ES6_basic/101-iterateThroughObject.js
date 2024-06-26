export default function iterateThroughObject(report) {
  // empty string to hold the concatenated names.
  let employeeNames = '';

  for (const employee of report) {
    // append each employee's name followed by a pipe | separator to the string.
    employeeNames += ` ${employee} |`;
  }
  // Remove the last pipe from the string and return the result
  // so that the string does not end with an unnecessary separator.
  return employeeNames.substring(1, employeeNames.length - 2);
}
