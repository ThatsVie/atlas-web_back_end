export default class Car {
  // Constructor initializes a new Car instance with specified brand, motor, and color
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Static getter for Symbol.species defines constructor function used for creating new instances
  static get [Symbol.species]() {
    return this; // Returns the current class (Car or a subclass)
  }

  // Method to clone the car, creating a new instance of the class
  cloneCar() {
    // Retrieve the constructor function defined by Symbol.species
    const Species = this.constructor[Symbol.species];
    // Create a new instance without passing the current properties
    return new Species();
  }
}
