// Define a function 'getBudgetObject' that accepts three parameters: income, gdp, and capita.
// This function is designed to create and return a budget object based on these parameters.
export default function getBudgetObject(income, gdp, capita) {
  // Construct an object 'budget' with three properties: income, gdp, and capita.
  // Each property uses ES6 property value shorthand to assign values,
  // which is used when the property name and the variable name are the same.
  const budget = {
    income,
    gdp,
    capita,
  };

  // Return the newly created budget object.
  // This object will have the structure { income: <value>, gdp: <value>, capita: <value> }
  return budget;
}

