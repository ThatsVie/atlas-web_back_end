import Car from './10-car.';

// EVCar class that extends the Car class
export default class EVCar extends Car {
  // Constructor for EVCar with attributes
  constructor(brand, motor, color, range) {
    // Call the constructor of the parent class Car
    super(brand, motor, color);
    // initialize the _range property, stored privately within the class
    this._range = range;
  }

  // Override the cloneCar method for EVCar
  cloneCar() {
    // Return a new instance of the Car class instead of EVCar
    // makes sure that cloned object is a generic Car, not an EVCar providing privacy
    return new Car();
  }
}
