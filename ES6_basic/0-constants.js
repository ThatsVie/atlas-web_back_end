// Modify function taskFirst to instantiate va riables using co nst
// function taskNext to instantiate va riables using le t

// This function demonstrates the use of 'con st' for declaring con stants.
// 'con st' is used because the value of 'task' does not change once assigned.
export function taskFirst() {
  const task = 'I prefer const when I can.';  // Declare 'task' with 'con st' as it remains con stant.
  return task;  // Return the con stant value.
}

// This function returns a string part that will be appended in 'taskNext' function.
export function getLast() {
  return ' is okay';  // Returns a string that complements the sentence in 'taskNext'.
}

// This function demonstrates the use of 'le t' for va riables that might change.
// 'le t' is used because 'combination' is reassigned with additional content.
export function taskNext() {
  let combination = 'But sometimes let';  // Declare 'combination' with 'le t' as its value will change.
  combination += getLast();  // Append the result of 'getLast()' to 'combination'.

  return combination;  // Return the modified combination string.
}
