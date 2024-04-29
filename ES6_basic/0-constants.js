// Modify function taskFirst to instantiate using const
// function taskNext to instantiate using let

// This function demonstrates the use of 'const' for declaring constants.
// 'const' is used because the value of 'task' does not change once assigned.
export function taskFirst() {
  const task = 'I prefer const when I can.';  // Declare 'task' with 'const' as it remains constant.
  return task;  // Return the constant value.
}

// This function returns a string part that will be appended in 'taskNext' function.
export function getLast() {
  return ' is okay';  // Returns a string that complements the sentence in 'taskNext'.
}

// This function demonstrates the use of 'let'  that might change.
// 'let' is used because 'combination' is reassigned with additional content.
export function taskNext() {
  let combination = 'But sometimes let';  // Declare 'combination' with 'let' as its value will change.
  combination += getLast();  // Append the result of 'getLast()' to 'combination'.

  return combination;  // Return the modified combination string.
}
