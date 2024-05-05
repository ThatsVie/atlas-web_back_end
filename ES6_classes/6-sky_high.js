import Building from './5-building';

// Define class that extends from Building
export default class SkyHighBuilding extends Building {
  // Constructor takes parameters sqft and floors
  constructor(sqft, floors) {
    super(sqft); // Call superclass constructor with sqft to handle the Building setup
    this._floors = floors; // Initialize  _floors property, storing it privately
  }

  // Getter for sqft inherited from the Building class
  // Provides read access to the sqft property which is managed by the superclass
  get sqft() {
    return this._sqft; // Return value of private _sqft property inherited from Building
  }

  // Getter for floors to provide external access to the _floors property
  get floors() {
    return this._floors; // Return the private _floors property's value
  }

  // Override the evacuationWarningMessage method to provide a custom message
  evacuationWarningMessage() {
    // Return a string that includes the number of floors in the evacuation message
    // Using template literals to embed the _floors variable value within the string
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
