// Define the function getSanFranciscoDescription, which does not take any parameters.
export default function getSanFranciscoDescription() {
  // Declare a constant 'year' and initialize it with the value 2017.
  const year = 2017;

  // Declare a constant 'budget' and initialize it as an object with three properties:
  // 'income', 'gdp', and 'capita', each set to a string representing financial figures.
  const budget = {
    income: '$119,868',
    gdp: '$154.2 billion',
    capita: '$178,479',
  };

  // Return a formatted string using a template literal.
  // The template literal allows embedding expressions directly within the string,
  // making it easy to incorporate variables and expressions.
  // The backslashes at the end of lines are used to continue the template literal
  // across multiple lines in the source code without adding newlines to the string itself.
  return `As of ${year}, it was the seventh-highest income county in the United States,\
 with a per capita personal income of ${budget.income}. As of 2015, San Francisco\
 proper had a GDP of ${budget.gdp}, and a GDP per capita of ${budget.capita}.`;
}
