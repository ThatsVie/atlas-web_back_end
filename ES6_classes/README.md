# ES6 Classes

## Learning Objectives

## Task Overview

### Task 0
Implement the `ClassRoom` class:
- **Constructor Attribute:** Initialize with `maxStudentsSize` (Number), stored as `_maxStudentsSize`.
- It creates an instance that tracks the maximum size of students that can be accommodated.

### Task 1
Implement the `initializeRooms` function:
- **Functionality:** Returns an array of three `ClassRoom` objects with sizes 19, 20, and 34, showcasing different room capacities.

### Task 2
Implement the `HolbertonCourse` class:
- **Constructor Attributes:** Initialize with `name` (String), `length` (Number), and `students` (array of Strings), each stored with underscore prefixes (e.g., `_name`).
- **Accessors:** Provide getters and setters for each attribute to manage data access and validation.
- It handles course information and enforces attribute type during object creation.

### Task 3
Implement the `Currency` class:
- **Constructor Attributes:** Initialize with `code` (String) and `name` (String), stored as `_code` and `_name`.
- **Accessors:** Provide getters and setters for each attribute.
- **Display Method:** `displayFullCurrency()` returns the format "name (code)".
- Manages currency details and provides formatted currency display.

### Task 4
Implement the `Pricing` class:
- **Constructor Attributes:** Initialize with `amount` (Number) and `currency` (instance of Currency), stored as `_amount` and `_currency`.
- **Accessors:** Provide getters and setters for both attributes to manage data access and validation.
- **Display Method:** `displayFullPrice()` returns the format "amount currency_name (currency_code)".
- **Static Method:** `convertPrice(amount, conversionRate)` returns the product of the amount and conversion rate.
- This class uses the `Currency` class to manage currency details.

### Task 5
Implement the `Building` base class:
- **Constructor Attribute:** Initialize with `sqft` (Number), stored as `_sqft`.
- **Abstract Enforcement:** Ensure any subclass implements `evacuationWarningMessage`. If not implemented, throw an error.
- **Accessors:** Provide a getter and setter for `sqft` to manage data access and validate data type.
- The class acts as a base for other building types, enforcing specific subclass behaviors.

### Task 6
Implement the `SkyHighBuilding` class that extends the `Building` base class:
- **Constructor Attributes:** Inherits `sqft` from `Building` and introduces `floors` (Number), both stored privately as `_sqft` and `_floors`.
- **Getters:** Implement getters for both `sqft` and `floors` to provide external access.
- **Method Override:** Overrides `evacuationWarningMessage` to provide a custom evacuation message specific to the number of floors.
- This subclass demonstrates how to extend a base class with additional properties and customized behavior.

### Task 7
Implement the `Airport` class:
- **Constructor Attributes:** Initialize with `name` (String) and `code` (String), stored as `_name` and `_code` to ensure privacy.
- **Getters:** Implement getters for `name` and `code` to safely access these private attributes.
- **Custom String Representation:** Override the `toString()` method to return the airport code when the class instance is converted to a string.
- This class demonstrates encapsulation and custom object representation in JavaScript.

### Task 8
Implement the `HolbertonClass`:
- **Constructor Attributes:** Initialize with `size` (Number) and `location` (String), each stored as a private property ( `_size` and `_location`).
- **Type Coercion:** Customize type conversion so that when instances are cast to a Number, they return `size`, and when cast to a String, they return `location`.
- This class demonstrates how to manage private properties and customize object representation in JavaScript.

## File Overview
- `0-classroom.js`: Contains the implementation of the `ClassRoom` class. This class accepts a `maxStudentsSize` parameter in its constructor and assigns it to a private property `_maxStudentsSize`.
- `0-main.js`: A testing script used to validate the functionality of the `ClassRoom` class by creating an instance and logging the `_maxStudentsSize` property.

- `1-make_classrooms.js`: Contains the `initializeRooms` function which creates and returns an array of `ClassRoom` objects with predefined sizes.
- `1-main.js`: A testing script used to validate the functionality of the `initializeRooms` function by logging the array of `ClassRoom` objects.

- `2-hbtn_course.js`: Contains the `HolbertonCourse` class with getters and setters for name, length, and students.
- `2-main.js`: A testing script for `HolbertonCourse`.

- `3-currency.js`: Contains the `Currency` class with methods to handle currency attributes and display them.
- `3-main.js`: A testing script for `Currency`.

- `4-pricing.js`: Contains the `Pricing` class which deals with the pricing information, includes type checks, and methods for display and conversion.
- `4-main.js`: A testing script for `Pricing`.

- `5-building.js`: Defines the `Building` class, enforcing an abstract-like behavior for subclasses.
- `5-main.js`: A testing script for `Building`, demonstrating enforcement of subclass method implementation and error handling.

- `6-sky_high.js`: Defines the `SkyHighBuilding` class that extends `Building`.
- `6-main.js`: A testing script for `SkyHighBuilding`.

- `7-airport.js`: Defines the `Airport` class with customized toString method.
- `7-main.js`: A testing script for `Airport`.

- `8-hbtn_class.js`: Defines the `HolbertonClass` with customized type coercion.
- `8-main.js`: A testing script for `HolbertonClass`.


## Installation
Clone this repository and navigate to the project directory.

```
git clone https://github.com/ThatsVie/atlas-web_back_end.git
```

```
cd ES6_classes
```

## Setup
Ensure you have Node.js installed on your system. [ Visit this site for details about which version may be appropriate for you ](https://github.com/nodejs/Release)

**Install Jest**

Jest is used for running tests. Install Jest using npm by running:
```
npm install --save-dev jest
```

**Install Babel**

Babel is used for compiling ES6+ JavaScript to backwards-compatible versions. Install Babel along with necessary presets:
```
npm install --save-dev babel-jest @babel/core @babel/preset-env
```

**Install ESLint**

ESLint is used to ensure code quality and consistency. Install ESLint with:
```
npm install --save-dev eslint
```
## Usage

### Task 0

To run the 0-main.js script and test the implementation, use the following command:
```
npm run dev 0-main.js
```
When you run the above command, it executes the script 0-main.js, which imports the ClassRoom class and creates an instance with a maxStudentsSize of 10. The script then logs the value of _maxStudentsSize:

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/f1ec5473-d1e4-4db6-9a23-26de6ba07482)


This output confirms that the ClassRoom instance has been successfully created with a maximum student size of 10, and that the _maxStudentsSize property is correctly storing and retrieving this value.

### Task 1

To run the `1-main.js` script and test the implementation, use the following command:
```
npm run dev 1-main.js
```
When you run the above command for Task 1, it executes the script `1-main.js`, which imports and calls the `initializeRooms` function. The output should be an array of `ClassRoom` objects with the specified sizes:

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/6f88425f-ae43-47d3-8ae8-4371ccf7411c)


This confirms that the `initializeRooms` function correctly creates and returns an array of `ClassRoom` instances with the correct sizes.


### Task 2

To run the `2-main.js` script and test the implementation, use the following command:
```
npm run dev 2-main.js
```

This command executes the `2-main.js` script, which tests various functionalities of the `HolbertonCourse` class:
- It first creates an instance of `HolbertonCourse` with valid initial values and prints the course name ("ES6").
- It then updates the course name to "Python 101" and prints the entire object.
- The script attempts to set the course name to a non-string value (`12`), which triggers a type error because the setter enforces string-only assignments.
- It tries to instantiate a new `HolbertonCourse` with a non-number type for the `length` attribute, again triggering a type error.

The output should look like this:

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/770513cc-8e55-4453-ba55-da12ba1b2dcd)


These outputs confirm that the class correctly handles type validation and showcases the use of getters and setters to manage class properties.

**Note on Output Abbreviation:**
The ellipsis (`...`) in the output represents truncated stack trace details. These details are typically long error messages and paths which have been shortened here for clarity and brevity in the README.


### Task 3

To run the `3-main.js` script and test the implementation of the `Currency` class, use the following command:
```
npm run dev 3-main.js
```

When you run the above command for Task 3, it executes the script `3-main.js`, which tests the `Currency` class by creating an instance and using the `displayFullCurrency` method. The output should display the currency in the format "Dollars ($)".

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/baf63517-dea6-468a-9699-1f057e0ed61b)


This output demonstrates that the `Currency` class correctly formats and displays currency details using the `displayFullCurrency` method, which concatenates the currency name and code in the specified format. This confirms that getters are working as intended and that the class correctly manages and displays currency information.


### Task 4

To run the `4-main.js` script and test the implementation of the `Pricing` class, use the following command:
```
npm run dev 4-main.js
```

When you run the above command, it executes the script `4-main.js`, which tests the `Pricing` class by creating an instance with an `amount` of 100 and a `currency` of Euro (`EUR`). Here's the output demonstrating the instantiated object and the formatted display of the price:

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/f63a6d20-5548-43ce-8dbb-81b55919d8eb)


This output confirms that the `Pricing` class correctly manages and displays pricing information, including the currency details. It also shows that the class can format and present the full price as specified.


### Task 5

To run the `5-main.js` script and test the implementation of the `Building` class, use the following command:
```
npm run dev 5-main.js
```


When executed, this script does the following:
- It attempts to create an instance of `Building`, which should be permissible only if `Building` is not meant to be fully abstract.
- It then attempts to instantiate `TestBuilding`, a subclass that does not implement the required `evacuationWarningMessage` method, triggering an error.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/1a4b338f-3f5b-4d72-b229-2f2bf5fb7655)


This demonstrates that the `Building` class effectively enforces a rule requiring subclasses to implement the evacuationWarningMessage method.

### Task 6

To run the `6-main.js` script and test the implementation of the `SkyHighBuilding` class, use the following command:

```
npm run dev 6-main.js
```

When executed, this script demonstrates:
- Creating an instance of `SkyHighBuilding` with specified square footage (140) and number of floors (60).
- Accessing and displaying the `sqft` and `floors` properties via their respective getters.
- Displaying the custom evacuation message tailored to the building's floor count.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/fec9e361-8dc1-497e-80e9-50aeb81cc0ed)

This confirms that the SkyHighBuilding class properly handles both its inherited and new properties, and it effectively provides a tailored evacuation message as required.


### Task 7

To run the `7-main.js` script and test the implementation of the `Airport` class, use the following command:
```
npm run dev 7-main.js
```

This script demonstrates:
- Creating an instance of `Airport` with a name "San Francisco Airport" and a code "SFO".
- Displaying the default object representation and the custom string via the overridden `toString()` method.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/9f42ec47-70f2-4f37-98a5-375ac264fc8a)


The output confirms that the `Airport` class manages its properties securely through encapsulation and modifies the default object-to-string conversion to display the airport code.

### Task 8

To run the `8-main.js` script and test the implementation of the `HolbertonClass`, use the following command:
```
npm run dev 8-main.js
```

This script demonstrates:
- Creating an instance of `HolbertonClass` with a size of 12 and a location named "Mezzanine".
- Showing how the class handles type coercion by converting an instance to a Number and a String.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/e8a97da3-241a-4964-adc1-bdcc29878ae6)


This confirms that the `HolbertonClass` correctly handles and returns its properties when coerced to a number or string


### Task 9


### Task 10
