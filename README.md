# Overview

This system provides an extensible hotel reservation platform implemented in Python. It includes a robust set of features to manage hotels, customers, and their reservations. The system consists of three main modules:

1. abstraction.py : Defines core classes and functions for the system.
2. test_abstractions.py : Contains unit tests for validating the functionality of the abstactions.py module.
3. main.py : Provides a command-line interface for the system.

# Module Description

1. abstraction.py
   This module forms the backbone of the hotel reservation system. It provide:

- Classes

  - Hotel : Represents a hotel with attributes for name, number of rooms, and reservations.
  - Customer : Respresents a customer with a name.

- Functions - create_hotel, delete_hotel, modify_hotel : Manage hotel creation, deletion, and modification. - create_customer, delete_customer, modify_customer : Manage customer creation, deletion, and modification. - create_reservation, cancel_reservation : Handle the creation and cancellation of reservations. - display_hotel, display_customer : Display detailed information abaout hotels and customer. - Utility functions for saving and loading objects in JSON format.
  The data is stored in .hotel and .customer files, making it persistent across runs.

2. test_abstractions.py
   This module ensures the reliability of the abstractions.py functions through comprehensive unit testing using Python's unittest framework. Key highlights:

- Test Structure
  - TestHotel : Tests the Hotel class.
  - Test Customer : Test the Customer class.
  - TestFunctions : Verifies the core functions for creating, deleting, and managing hotels and customer.
  - TestDisplayFunctions : Tests the output of display functions using unittest.mock.
- Key Features:
  - Validates reservation creation and cancellation
  - Ensures correct JSON serialization/deserialization
  - Mocks printing to verify display functions without actual console outpu.
- How to Run : Execute the script directly to run the tests.

3. main.py
   This script provides a command-line interface to interact with the hotel reservation system. Key operations:

- Initialization :
  - Creates three sample hotels and nine customer.
- Core Operations :
  - Creates reservations, modifies hotel and customer data, and displays results.
- Demonstrates : - How to interact with the API. - A workflow for managing hotels, customers, and reservations step-by-steo.
  The main() function integrates all the features into a comprehensive demonstration of the system's capabilities.

# How to Use

1. Setup :
   - Ensure all modules are in the same directory.
   - Install Python (3.6 or higher).
2. Run the Test : Execure text_abstractions.py to verify functionality:
   - python test_abstractions.py
3. Run the System : Execute main.py for an interactive demo:
   - python main.py

# Key Features and Functional Highlights

- Hotel and Customer Management :
  - Persistent data storage in JSON files.
  - Modular and reusable class design.
- Reservation Management :
  - Robust valdiation for room availability.
  - Seamless update and cancellation of reservations.
- Testing :
  - Compregensive coverage with unit tests for all key functionalities.
