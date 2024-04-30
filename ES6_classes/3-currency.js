// Defines the Currency class
export default class Currency {
  // Constructor to initialize the Currency object with code and name attributes
  constructor(code, name) {
    this.code = code; // Assign the code using the setter to ensure it's a string
    this.name = name; // Assign the name using the setter to ensure it's a string
  }

  // Getter for the code attribute
  // This method allows external access to the private _code attribute in a controlled manner
  get code() {
    return this._code;
  }

  // Setter for the code attribute
  // This method ensures that only string values are assigned to _code
  // If a non-string value is assigned, it throws a TypeError
  set code(newCode) {
    if (typeof newCode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = newCode; // Store value in the private _code attribute if it passes type check
  }

  // Getter for the name attribute
  // This method allows external access to the private _name attribute in a controlled manner
  get name() {
    return this._name;
  }

  // Setter for the name attribute
  // This method ensures that only string values are assigned to _name
  // If a non-string value is assigned, it throws a TypeError
  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName; // Store value in the private _name attribute if it passes type check
  }

  // Method to display the full currency information in a specific format "name (code)"
  // This method combines the name and code using a template literal for easy reading
  displayFullCurrency() {
    return `${this.name} (${this.code})`; // Returns the formatted string
  }
}
