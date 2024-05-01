// Define the HolbertonClass with a constructor and getters.
export class HolbertonClass {
  // Constructor initializes each instance with a year and a location.
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }

  // Getter for year allows external access to the _year property
  get year() {
    return this._year;
  }

  // Getter for location allows external access to the _location property
  get location() {
    return this._location;
  }
}

// Create instances of HolbertonClass for the years 2019 and 2020.
const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

// Define the StudentHolberton class which also includes a constructor and getters.
export class StudentHolberton {
  constructor(firstName, lastName, holbertonClass) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
  }

  // Getter that combines the first and last names into a full name.
  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  // Getter to access the student's class instance.
  get holbertonClass() {
    return this._holbertonClass;
  }

  // Getter to provide a full description of the student including their class year and location.
  get fullStudentDescription() {
    return `${this._firstName} ${this._lastName} - ${this._holbertonClass.year} - ${this._holbertonClass.location}`;
  }
}

// Create instances of StudentHolberton with references to instances of HolbertonClass.
const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

// An array to hold all student instances.
const listOfStudents = [student1, student2, student3, student4, student5];

// Export the array of students as the default export of the module.
export default listOfStudents;
