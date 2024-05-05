export default function createInt8TypedArray(length, position, value) {
  // Check if the position is within the range of the array buffer
  if (position < 0 || position >= length) {
    // Throw an error if the position is outside the allowable range
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  // Create a DataView for the buffer to manipulate its contents
  const dataView = new DataView(buffer);

  // Use the DataView to set an 8-bit integer (Int8) at the specified position
  dataView.setInt8(position, value);
  // Return the DataView object which provides a view on the ArrayBuffer
  return dataView;
}
