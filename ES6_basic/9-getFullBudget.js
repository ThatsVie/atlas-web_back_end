// Import the getBudgetObject function from another module.
import getBudgetObject from './7-getBudgetObject';

// Define a function to extend basic budget object with additional methods for currency formatting.
export default function getFullBudgetObject(income, gdp, capita) {
  // Retrieve the basic budget object with specified income, gdp, and capita values.
  const budget = getBudgetObject(income, gdp, capita);

  // Extend the basic budget object with additional methods using ES6 method shorthand syntax.
  const fullBudget = {
    ...budget, // Spread syntax to copy properties from the basic budget object into the fullBudget.

    // Define a method to format the income as a dollar value.
    // The ES6 method shorthand is used here instead of the 'function' keyword.
    getIncomeInDollars(income) {
      return `$${income}`; // Return the income prefixed with a dollar sign, indicating US currency.
    },

    // Define a method to format the income as a euro value.
    // This also uses ES6 method shorthand for more concise function declaration.
    getIncomeInEuros(income) {
      return `${income} euros`; // Return the income followed by the word "euros"
    },
  };

  return fullBudget;
}
