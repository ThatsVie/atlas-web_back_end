export const weakMap = new WeakMap();

// function queryAPI to track API endpoint queries
export function queryAPI(endpoint) {
  // check if the endpoint is already in the weakMap
  let count = weakMap.get(endpoint) || 0;

  // Increment the count of queries for the given endpoint
  count += 1;

  // Update the weakMap with new count for endpoint
  weakMap.set(endpoint, count);

  // Check if the count has reached the limit of 5 queries
  if (count >= 5) {
    // Throw an error if the endpoint has been queried 5 or more times
    throw new Error('Endpoint load is high');
  }
}
