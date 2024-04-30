// Define a helper function that retrieves the current year.
// This function creates a new Date object, extracts, and returns the year.
function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

// Define the main function that takes three parameters: income, gdp, and capita.
// This function constructs an object with dynamic keys based on the current year and returns it.
export default function getBudgetForCurrentYear(income, gdp, capita) {
  // Create an object 'budget' with keys that are dynamically computed using template literals.
  // The keys include the category name (income, gdp, capita) followed by the current year.
  // This allows the keys to reflect the year automatically at the time of function execution.
  // Each key is mapped to the corresponding parameter value passed to the function.
  const budget = {
    [`income-${getCurrentYear()}`]: income,
    [`gdp-${getCurrentYear()}`]: gdp,
    [`capita-${getCurrentYear()}`]: capita,
  };

  // Return the constructed object. The keys of this object will be in the format:
  // 'income-YYYY', 'gdp-YYYY', 'capita-YYYY', where 'YYYY' represents the current year.
  return budget;
}
