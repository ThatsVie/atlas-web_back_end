export default function groceriesList() {
  // Start by creating a Map to store grocery items with their associated quantities
  const groceries = new Map([
    ['Apples', 10],
    ['Tomatoes', 10],
    ['Pasta', 1],
    ['Rice', 1],
    ['Banana', 5],
  ]);

  // Return the fully initialized Map containing the list of groceries
  return groceries;
}
