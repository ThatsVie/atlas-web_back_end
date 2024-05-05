// Defines Currency class
export default class Currency {
  // Constructor to initialize the Currency object with code and name attributes
  constructor(code, name) {
    this.code = code; // Assign the code using the setter to ensure it's a string
    this.name = name;
  }

  // Getter for the code attribute
  // Allows external access to the private _code attribute
  get code() {
    return this._code;
  }

  // Setter for the code attribute
  // Ensures that only string values are assigned to _code
  // If a non-string value is assigned, it throws a TypeError
  set code(newCode) {
    if (typeof newCode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = newCode; // Store value in the private _code attribute if it passes type check
  }

  // Getter for the name attribute
  // Allows external access to the private _name attribute
  get name() {
    return this._name;
  }

  // Setter for the name attribute
  // ensures that only string values are assigned to _name
  // If a non-string value is assigned it throws a TypeError
  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName; // Store value in the private _name attribute if it passes type check
  }

  // Method to display the full currency information in a specific format "name (code)"
  // Combines the name and code using a template literal
  displayFullCurrency() {
    return `${this.name} (${this.code})`; // Returns the formatted string
  }
}
