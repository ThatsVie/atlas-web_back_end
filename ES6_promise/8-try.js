export default function divideFunction(numerator, denominator) {
  // See if the denominator is zero
  if (denominator === 0) {
    // Throw an error if the denominator is zero
    throw new Error('cannot divide by 0');
  }
  // If the denominator is not zero, return result of division
  return numerator / denominator;
}
