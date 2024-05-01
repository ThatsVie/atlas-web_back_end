// Import the Currency class from '3-currency.js'
import Currency from './3-currency';

// Define Pricing class which handles values associated with currency
export default class Pricing {
  // Constructor initializes Pricing object with amount and currency
  constructor(amount, currency) {
    this._amount = amount; // Store the amount privately to encapsulate the data
    this._currency = currency; // Store the currency object privately to encapsulate the data
  }

  // Getter for amount returns the private _amount variable
  get amount() {
    return this._amount;
  }

  // Getter for currency returns the private _currency object
  get currency() {
    return this._currency;
  }

  // Setter for amount sets the private _amount variable after type checking
  set amount(newAmount) {
    if (typeof newAmount !== 'number') { // Ensure the new amount is a number
      throw new TypeError('Amount must be a number.'); // Throw an error if not
    }
    this._amount = newAmount; // Assign the new value if it passes the type check
  }

  // Setter for currency sets the private _currency object after checking its type
  set currency(newCurrency) {
    if (!(newCurrency instanceof Currency)) { // Ensure new currency is an instance of Currency
      throw new TypeError('Currency must be a currency.'); // Throw an error if not
    } else {
      this._currency = newCurrency; // Assign the new object if it is a valid Currency
    }
  }

  // Method to display the full price as a formatted string
  displayFullPrice() {
    // Returns a string combining amount, currency name, and currency code
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  // Static method to convert price using a given conversion rate
  static convertPrice(amount, conversionRate) {
    // Calculates and returns the converted amount
    return amount * conversionRate; // Multiplies the amount by the conversion rate
  }
}
