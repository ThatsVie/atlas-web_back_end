# ES6 Classes

This project covers ES6 classes including creating and managing different classes and subclasses, showcasing essential concepts like inheritance, method overriding, and data encapsulation. It also  covers static methods and metaprogramming with symbols to dynamically control how classes behave, especially when cloning objects. 

## Learning Objectives

### How to Define a Class

In JavaScript, a class is defined using the `class` keyword, followed by the class name and a pair of curly braces that encapsulate the class body. The constructor within a class initializes instance properties when new objects are created. Throughout the tasks, I defined various classes like `ClassRoom`, `HolbertonCourse`, and `Car`, each with a constructor that sets up initial state or properties like room size, course details, or car attributes.

### How to Add Methods to a Class

Methods are added to a class to define behaviors for its instances. These are placed within the class body and are defined like regular functions, but without the function keyword. Throughout these tasks, I added methods like `displayFullPrice` in the Pricing class, which utilizes other object properties to return formatted strings, demonstrating interaction with instance data.

### Why and How to Add a Static Method to a Class

Static methods are associated with the class itself rather than any instance. They are useful for utility functions that might be related to the class but do not operate on instance-specific data. A static method is defined using the `static` keyword. For example, in `Car` class, I used a static getter for Symbol.species to control which constructor is used when instances are cloned, showing how static methods can manage or alter class behavior.

### How to Extend a Class from Another

Extending a class allows a new class to inherit properties and methods from another class. This is done using the `extends` keyword. For example, I extended the `Building` class to create `SkyHighBuilding`, which inherits and can override properties and methods of `Building`. This allows for code reuse and for creating a class hierarchy where subclasses specialize or modify the behavior of their base class.

### Metaprogramming and Symbols

Metaprogramming involves techniques that allow a program to manipulate itself dynamically or provide ways to alter its behavior during runtime. In JavaScript, symbols are used as unique identifiers that can alter object properties in ways that are not possible with traditional strings or numbers. In task 10, I utilized Symbol.species in the `Car` class to customize the behavior of instance cloning. This ensures that the cloned object maintains the class type of the original, even when subclasses do not explicitly override the cloning method.

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

### Task 9
Fix the implementation of `HolbertonClass` and `StudentHolberton`:
- **HolbertonClass:** Manages year and location of the class with proper encapsulation.
- **StudentHolberton:** Manages student details and links to their respective `HolbertonClass`.
- **Functionality:** Ensure proper instantiation and access control with getters, and provide a detailed description of each student through getters.
- This task demonstrates fixing issues in class implementation, ensuring correct instantiation, and managing relationships between classes.

### Task 10
Implement the `Car` class with enhanced cloning capabilities:
- **Attributes**: The `Car` class is initialized with attributes `brand`, `motor`, and `color`, each stored privately.
- **Cloning**: Incorporate a `cloneCar` method that leverages `Symbol.species` to return a new, uninitialized instance of the same class, ensuring type preservation without copying initial attribute values.
- This task demonstrates class inheritance, symbol usage, and dynamic instance creation.

### Tak 11:
Implement `EVCar` class
-**Objective**: Extend the Car class to include an additional property, range, and override the cloneCar method.
-**Description**: Implement the `EVCar` class that extends from the `Car` class with extra attributes and modified cloning functionality. The `EVCar` includes all properties of `Car` plus a new attribute for the `range`. The `cloneCar` method should return an instance of `Car` instead of `EVCar` to ensure privacy.

## File Overview

### Task 0
- `0-classroom.js`: Contains the implementation of the `ClassRoom` class. This class accepts a `maxStudentsSize` parameter in its constructor and assigns it to a private property `_maxStudentsSize`.
- `0-main.js`: A testing script used to validate the functionality of the `ClassRoom` class by creating an instance and logging the `_maxStudentsSize` property.
- 
### Task 1
- `1-make_classrooms.js`: Contains the `initializeRooms` function which creates and returns an array of `ClassRoom` objects with predefined sizes.
- `1-main.js`: A testing script used to validate the functionality of the `initializeRooms` function by logging the array of `ClassRoom` objects.

### Task 2
- `2-hbtn_course.js`: Contains the `HolbertonCourse` class with getters and setters for name, length, and students.
- `2-main.js`: A testing script for `HolbertonCourse`.

### Task 3
- `3-currency.js`: Contains the `Currency` class with methods to handle currency attributes and display them.
- `3-main.js`: A testing script for `Currency`.

### Task 4
- `4-pricing.js`: Contains the `Pricing` class which deals with the pricing information, includes type checks, and methods for display and conversion.
- `4-main.js`: A testing script for `Pricing`.

### Task 5
- `5-building.js`: Defines the `Building` class, enforcing an abstract-like behavior for subclasses.
- `5-main.js`: A testing script for `Building`, demonstrating enforcement of subclass method implementation and error handling.

### Task 6
- `6-sky_high.js`: Defines the `SkyHighBuilding` class that extends `Building`.
- `6-main.js`: A testing script for `SkyHighBuilding`.

### Task 7
- `7-airport.js`: Defines the `Airport` class with customized toString method.
- `7-main.js`: A testing script for `Airport`.

### Task 8
- `8-hbtn_class.js`: Defines the `HolbertonClass` with customized type coercion.
- `8-main.js`: A testing script for `HolbertonClass`.

### Task 9
- `9-hoisting.js`: Corrects the implementation of `HolbertonClass` and `StudentHolberton`.
- `9-main.js`: Demonstrates and tests the corrected implementations.

### Task 10
- `10-car.js`: Implements the `Car` class with cloning functionality using `Symbol.species`.
- `10-main.js`: Tests the cloning method of the `Car` class.

### Task 11
- `100-evcar.js`: Contains the implementation of the `EVCar` class which extends the functionality of the `Car` class. It adds a new attribute- `range`, and modifies the `cloneCar` method to return a generic `Car` instance.
- `100-main.js`: A script to demonstrate creating an EVCar instance, showing its properties and the functionality of cloning that returns an instance of `Car` instead of `EVCar`.

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

To run the `9-main.js` script and test the corrected implementation of `HolbertonClass` and `StudentHolberton`, use the following command:
```
npm run dev 9-main.js
```


This script will:
- Instantiate `HolbertonClass` for the years 2019 and 2020 in San Francisco.
- Create five `StudentHolberton` instances with references to these `HolbertonClass` instances.
- Output the list of students and their detailed descriptions.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/b87ea8d1-3c20-48fb-a8ab-cf316cac908b)


This output confirms that the `HolbertonClass` and `StudentHolberton` classes are correctly implemented and interacting as expected, with each student linked to a specific class and providing a detailed description including the year and location of their class.

### Task 10
To test the implementation of the `Car` class and its cloning functionality, run the `10-main.js` script using the following command:
```
npm run dev 10-main.js
```

This script will:
- Create an instance of `TestCar`, a subclass of `Car`, initialized with specific attributes.
- Clone this `TestCar` instance using the `cloneCar` method, resulting in a new instance with type preservation but without attribute initialization.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/368cfbe2-012e-4b21-9cf8-6507a51863e5)


- The first `true` confirms that the original car (`tc1`) is an instance of `TestCar`.
- The second `true` confirms that the cloned car (`tc2`) is also an instance of `TestCar`.
- `false` indicates that the original and cloned cars are not the same object, demonstrating successful cloning with type preservation.

This setup ensures that the `Car` class correctly implements cloning in a way that can be extended and used in more complex class hierarchies.

### Task 11
To test the functionality of the EVCar class, you can use the following command:
```
npm run dev 100-main.js
```
This will execute the 100-main.js script, which imports the EVCar class, creates an instance of it, and tests its functionality including the overridden cloneCar method:

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/11744306-2b6f-46db-b5e4-7a01ddf23179)

An `EVCar` object is instantiated with properties `brand`, `motor`, `color`, and `range`.

It displays the properties of the EVCar instance.

It tests the `cloneCar` method to verify that it returns an instance of `Car` instead of `EVCar` for privacy reasons. The output shows the properties of a generic `Car` without the details set by the `EVCar` constructor, indicating the cloning process does not carry over specific properties or behaviors of the `EVCar` class.

This setup confirms that the EVCar class correctly inherits from the Car class and appropriately modifies the cloneCar method to enhance privacy by returning a generic Car instance.
