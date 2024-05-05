// Import the ClassRoom class from the file where it's defined
import ClassRoom from './0-classroom';

// Function creates and returns an array of ClassRoom instances
function initializeRooms() {
  // Create an array of ClassRoom instances with specified sizes
  const rooms = [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34),
  ];
    // Return the array of instances
  return rooms;
}

// Export the initializeRooms function so it can be imported elsewhere
export default initializeRooms;
