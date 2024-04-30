// Define the HolbertonCourse class with type validation on its properties
export default class HolbertonCourse {
  // Constructor to initialize the HolbertonCourse object
  constructor(name, length, students) {
    // Assign properties using setters to enforce type checks
    this.name = name; // Set the name via the setter to validate type
    this.length = length; // Set the length via the setter to validate type
    this.students = students; // Set the students via the setter to validate type
  }

  // Getter for the name property
  get name() {
    // Return the private name property
    return this._name;
  }

  // Setter for the name property
  set name(newName) {
    // Check if newName is a string; throw error if not
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    // Assign the new name to the private name property
    this._name = newName;
  }

  // Getter for the length property
  get length() {
    // Return the private length property
    return this._length;
  }

  // Setter for the length property
  set length(newLength) {
    // Check if newLength is a number; throw error if not
    if (typeof newLength !== 'number') {
      throw new TypeError('Length must be a number');
    }
    // Assign the new length to the private length property
    this._length = newLength;
  }

  // Getter for the students property
  get students() {
    // Return the private students property
    return this._students;
  }

  // Setter for the students property
  set students(newStudents) {
    // Check if newStudents is an array of strings; throw error if not
    if (!Array.isArray(newStudents) || newStudents.some((s) => typeof s !== 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    // Assign the new list of students to the private students property
    this._students = newStudents;
  }
}
