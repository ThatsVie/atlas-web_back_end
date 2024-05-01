// Export the Building class as a module to be imported in 5-main.js
export default class Building {
  // Constructor takes argument for square footage
  constructor(sqft) {
    // Check if the current instance isnt directly of Building and
    // doesnt implement evacuationWarningMessage
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      // Throw an error if a subclass doesnt implement evacuationWarningMessage
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    // Initialize the _sqft property with the value provided to the constructor
    this._sqft = sqft;
  }

  // Getter for sqft to allow external access to the value of _sqft
  get sqft() {
    return this._sqft;
  }

  // Setter for sqft to allow the value of _sqft to be updated after object creation
  // and make sure the new value is of the correct type
  set sqft(newSqft) {
    // Check if the new square footage is a number
    if (typeof newSqft !== 'number') {
      // Throw an error if newSqft is not a number to enforce data type integrity
      throw new TypeError('sqft must be a number');
    }
    // Update the _sqft property with the new value
    this._sqft = newSqft;
  }
}
