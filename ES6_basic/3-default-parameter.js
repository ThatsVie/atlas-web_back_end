// This function 'getSumOfHoods' demonstrates the condensation of function internals to one line
// by employing default parameters. This approach simplifies the function body while preserving
// the functionality of handling different amounts of input data.
export default function getSumOfHoods(initialNumber, expansion1989 = 89, expansion2019 = 19) {
  // the function's logic is condensed into a single line of code by using default parameters.
  // 'expansion1989' and 'expansion2019' are set to default to 89 and 19, respectively
  // This single return line replaces multiple lines of conditional checks that would otherwise
  // be necessary to assign these default values inside the function body.
  return initialNumber + expansion1989 + expansion2019;
}
