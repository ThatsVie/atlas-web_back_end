export default class HolbertonClass {
  constructor(size, location) {
    this._size = size; // Store size privately
    this._location = location; // Store location privately
  }

  // When the class instance is cast to a Number, return the size
  valueOf() {
    return this._size;
  }

  // When the class instance is cast to a String, return the location
  toString() {
    return this._location;
  }
}
