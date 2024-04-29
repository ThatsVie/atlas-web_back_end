// Define a function 'getBudgetObject' that accepts three parameters: income, gdp, and capita.
// This function is designed to create and return a budget object based on these parameters.
export default function getBudgetObject(income, gdp, capita) {
  // Construct an object 'budget' with three properties: income, gdp, and capita.
  // Each property uses ES6 property value shorthand to assign values,
  // which is used when the property name and the variable name are the same.
  const budget = {
    income,  // Shorthand for income, assigns the 'income' argument to the 'income' property.
    gdp,     // Shorthand for gdp, assigns the 'gdp' argument to the 'gdp' property.
    capita   // Shorthand for capita, assigns the 'capita' argument to the 'capita' property.
  };

  // Return the newly created budget object.
  // This object will have the structure { income: <value>, gdp: <value>, capita: <value> }
  return budget;
}
