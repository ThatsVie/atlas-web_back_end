// Use export default so this class can be imported in other files.
export default class ClassRoom {
  // Constructor method initializes a new instance of the ClassRoom class.
  constructor(maxStudentsSize) {
    // The constructor accepts maxStudentsSize as a parameter.
    // This value is assigned to the _maxStudentsSize property of the class.
    // The underscore (_) before maxStudentsSize indicates that it's a private property
    this._maxStudentsSize = maxStudentsSize;
  }
}
