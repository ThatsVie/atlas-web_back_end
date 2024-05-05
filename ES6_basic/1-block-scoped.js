// This function demonstrates handling variable scoping properly to avoid issues
// caused by hoisting mechanism when using var
export default function taskBlock(trueOrFalse) {
  // Declare variables task and task2 with const at the function scope.
  // const ensures these variables cannot be reassigned within the same scope
  // and they are initialized immediately with their respective values.
  const task = false;
  const task2 = true;

  // A conditional block that checks the value of trueOrFalse
  if (trueOrFalse) {
    // Inside the if block, new variables task and task2 are declared with const
    // These are entirely new variables scoped only within this if block.
    // They do not affect the task and task2 declared at the function level because
    // each const declaration is confined to the block in which it is declared.
    const task = true;
    const task2 = false;
    // Logs the values of task and task2 within the if block to the console.
    // If trueOrFalse is true, this will output true, false
    console.log(task, task2);
  }

  // Returns the values of the task and task2 variables declared at the function scope.
  // Since task and task2 inside the if block are scoped only to that block
  // these will return false, true regardless of the input trueOrFalse
  return [task, task2];
}
