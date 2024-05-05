// Define the function with the rest parameter to accept any number of arguments.
export default function returnHowManyArguments(...args) {
  // args variable represents an array containing all arguments passed to the function.
  // Return the number of arguments by returning the length of the args array.
  return args.length;
}
