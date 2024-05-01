// Export the Airport class so it can be imported and used in 7-main.js
export default class Airport {
  // Constructor for the Airport class takes parameters name and code
  constructor(name, code) {
    // Initialize private variables _name and _code with the provided arguments
    // prefixed with an underscore to indicate that they are private
    // and should not be accessed directly outside of this class.
    this._name = name; // Store the name of the airport
    this._code = code; // Store the code of the airport
  }

  // Getter for the name property
  // This provides safe read access to the _name private variable
  // Getters allow encapsulation of the internal state of the object,
  // enabling only controlled access to the private variable.
  get name() {
    return this._name;
  }

  // Getter for the code property
  // provides read access to the private variable _code
  // encapsulating the code property allows it to be read without direct access
  get code() {
    return this._code;
  }

  // Override the default toString() method
  // customizes the default string representation of objects of this class
  // useful for debugging and logging, providing a clear and concise description of an object.
  // Instead of returning a generic object description, returns airport code
  toString() {
    return `[object ${this._code}]`; // Customize the output to show the airport code
  }
}
