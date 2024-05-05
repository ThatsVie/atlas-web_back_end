// Import the getBudgetObject function
import getBudgetObject from './7-getBudgetObject';

// function to extend basic budget object with additional methods 
export default function getFullBudgetObject(income, gdp, capita) {
  // retrieve the basic budget object
  const budget = getBudgetObject(income, gdp, capita);

  // Extend the basic budget object with additional methods using ES6 method shorthand syntax.
  const fullBudget = {
    ...budget, // Spread syntax to copy properties from the basic budget object into fullBudget

    // Method to format the income as a dollar value.
    // The ES6 method shorthand is used here instead of the function keyword
    getIncomeInDollars(income) {
      return `$${income}`; // Return the income prefixed with a dollar sign for  US currency.
    },

    // Method to format the income as a euro value.
    // This also uses ES6 method shorthand
    getIncomeInEuros(income) {
      return `${income} euros`; // Return the income followed by the word "euros"
    },
  };

  return fullBudget;
}
