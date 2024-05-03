import Car from './10-car';

// EVCar class that extends the Car class
export default class EVCar extends Car {
  // Constructor for creating a new EVCar instance
  constructor(brand, motor, color, range) {
    // Call the constructor of the parent Car class.
    super(brand, motor, color);
    // unique to EVCar, storing the range as a private variable.
    this._range = range;
  }

  // Override cloneCar to return an instance of Car instead of EVCar.
  // This prevents the special properties and methods of EVCar from being copied.
  // Disable ESLint warning about the this keyword not being used in the method.
  // eslint-disable-next-line class-methods-use-this
  cloneCar() {
    // Return a new Car instance-cloned objects are generic Cars.
    return new Car();
  }

  // Getter for brand. read-only access to  _brand property inherited from Car.
  get brand() {
    return this._brand;
  }

  // Getter for motor. read-only access to  _motor property inherited from Car.
  get motor() {
    return this._motor;
  }

  // Getter for color. read-only access to  _color property inherited from Car.
  get color() {
    return this._color;
  }

  // Getter for rang. read-only access to _range property specific to EVCar.
  get range() {
    return this._range;
  }
}
