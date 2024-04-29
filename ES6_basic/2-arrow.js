// Defines a constructor function called 'getNeighborhoodsList' for creating an object.
export default function getNeighborhoodsList() {
  // Initializes a property 'sanFranciscoNeighborhoods' on the object being created.
  // This property is an array of string names representing neighborhoods in San Francisco.
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  // Defines a method 'addNeighborhood' on the object using ES6 arrow syntax.
  // Arrow functions capture the 'this' value of the function in which they are defined,
  // which in this case is the 'getNeighborhoodsList' function.
  // 'this' inside the arrow function refers to the object being created by 'getNeighborhoodsList'.
  this.addNeighborhood = (newNeighborhood) => {
    // Pushes a new neighborhood name to the 'sanFranciscoNeighborhoods' array.
    // 'this' correctly refers to the object instance and its 'sanFranciscoNeighborhoods' property
    // because of the lexical binding of 'this' in arrow functions.
    this.sanFranciscoNeighborhoods.push(newNeighborhood);

    // Returns the updated array of neighborhood names.
    return this.sanFranciscoNeighborhoods;
  };
}
