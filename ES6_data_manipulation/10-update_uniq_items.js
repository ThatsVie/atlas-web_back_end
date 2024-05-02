export default function updateUniqueItems(map) {
  // Verify that the provided argument is a Map instance
  if (!(map instanceof Map)) {
    throw new Error('Cannot process'); // Throw an error if not to prevent further execution
  }

  // Loop through each entry in the map
  for (const [key, value] of map) {
    // Check if the current entry's value is 1
    if (value === 1) {
      map.set(key, 100); // Update the value to 100 if condition is met
    }
  }

  // Return the updated map (although the original map is modified directly)
  return map;
}
