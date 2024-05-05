// This function uses default parameters to simplify its logic into a single line
export default function getSumOfHoods(initialNumber, expansion1989 = 89, expansion2019 = 19) {
  // This single return line replaces multiple lines of conditional checks that would otherwise
  // be necessary to assign these default values inside the function body.
  return initialNumber + expansion1989 + expansion2019;
}
