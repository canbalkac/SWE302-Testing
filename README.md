# Overview

This system provides an extensible hotel reservation platform implemented in Python. It includes a robust set of features to manage hotels, customers, and their reservations. The system consists of three main modules:

1. **abstraction.py**: Defines core classes and functions for the system.
2. **test_abstractions.py**: Contains unit tests for validating the functionality of the abstraction.py module.
3. **gui.py**: Provides a graphical user interface (GUI) for user-friendly interaction with the system.

---

# Module Description

### 1. abstraction.py

This module forms the backbone of the hotel reservation system. It provides:

- **Classes**:

  - **Hotel**: Represents a hotel with attributes for name, number of rooms, and reservations.
  - **Customer**: Represents a customer with a name.

- **Functions**:
  - `create_hotel`, `delete_hotel`, `modify_hotel`: Manage hotel creation, deletion, and modification.
  - `create_customer`, `delete_customer`, `modify_customer`: Manage customer creation, deletion, and modification.
  - `create_reservation`, `cancel_reservation`: Handle the creation and cancellation of reservations.
  - `display_hotel`, `display_customer`: Display detailed information about hotels and customers.
  - Utility functions for saving and loading objects in JSON format.

The data is stored in `.hotel` and `.customer` files, making it persistent across runs.

---

### 2. test_abstractions.py

This module ensures the reliability of the abstraction.py functions through comprehensive unit testing using Python's `unittest` framework. Key highlights:

- **Test Structure**:

  - `TestHotel`: Tests the Hotel class.
  - `TestCustomer`: Tests the Customer class.
  - `TestFunctions`: Verifies the core functions for creating, deleting, and managing hotels and customers.
  - `TestDisplayFunctions`: Tests the output of display functions using `unittest.mock`.

- **Key Features**:

  - Validates reservation creation and cancellation.
  - Ensures correct JSON serialization/deserialization.
  - Mocks printing to verify display functions without actual console output.

- **How to Run**:
  Execute the script directly to run the tests:
  ```bash
  python test_abstractions.py
  ```

---

### 3. gui.py

This module provides a graphical user interface (GUI) for interacting with the hotel reservation system. It allows users to perform key operations through an intuitive interface:

- **Features**:

  - **Hotel and Customer Management**:
    - View hotels and customers.
    - Add new hotels and customers.
  - **Reservation Management**:
    - Create reservations by selecting customers without existing reservations and hotels with available rooms.
    - Cancel reservations by selecting customers with active reservations and their associated hotels.

- **How to Run**:
  Execute the script to start the GUI:

  ```bash
  python gui.py
  ```

---

# How to Use

1. **Setup**:

   - Ensure all modules are in the same directory.
   - Install Python (3.6 or higher).

2. **Run the Tests**:
   Execute `test_abstractions.py` to verify functionality:

   ```bash
   python test_abstractions.py
   ```

3. **Run the GUI**:
   Start the graphical user interface:
   ```bash
   python gui.py
   ```

---

# Key Features and Functional Highlights

- **Hotel and Customer Management**:

  - Persistent data storage in JSON files.
  - Modular and reusable class design.

- **Reservation Management**:

  - Robust validation for room availability.
  - Seamless update and cancellation of reservations.
  - User-friendly GUI for easy interaction.

- **Testing**:
  - Comprehensive coverage with unit tests for all key functionalities.

---

This system is now easier to use and more interactive, offering a reliable and robust hotel reservation experience.
