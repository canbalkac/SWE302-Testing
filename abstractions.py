"""
This module provides a simple hotel reservation system.

It includes two main classes: Hotel and Customer. The Hotel class represents a
hotel with a certain number of rooms and a list of reservations. The Customer
class represents a customer with a name.

The module also provides several functions to interact with hotels and
customers, including creating, deleting, displaying, and modifying hotels and
customers, as well as creating and cancelling reservations.

The data for hotels and customers is stored in JSON format in separate files
for each hotel and customer. The filename for a hotel or customer is its name
with the extension '.hotel' or '.customer', respectively.
"""
import json
import os
import locale


class Hotel:
    """
    A class used to represent a Hotel.

    ...

    Attributes
    ----------
    name : str
        the name of the hotel
    rooms : int
        the number of rooms in the hotel
    reservations : list
        the list of reservations in the hotel

    Methods
    -------
    reserve_room(customer)
        Reserves a room for a customer
    cancel_reservation(customer)
        Cancels a reservation for a customer
    update_reservation(old_name, new_name)
        Updates a reservation with a new customer name
    to_json()
        Returns a JSON string representation of the hotel
    from_json(json_str)
        Returns a Hotel object from a JSON string representation
    """

    def __init__(self, name, rooms):
        """Initializes Hotel with a name and number of rooms."""
        self.name = name
        self.rooms = rooms
        self.reservations = []

    def reserve_room(self, customer):
        """Reserves a room for a customer if rooms are available."""
        if self.rooms > 0:
            self.rooms -= 1
            self.reservations.append(customer.name)
            return True
        return False

    def cancel_reservation(self, customer):
        """Cancels a reservation for a customer if it exists."""
        if customer.name in self.reservations:
            self.rooms += 1
            self.reservations.remove(customer.name)
            return True
        return False

    def update_reservation(self, old_name, new_name):
        """Updates a reservation with a new customer name if it exists."""
        if old_name in self.reservations:
            self.reservations.remove(old_name)
            self.reservations.append(new_name)
            return True
        return False

    def to_json(self):
        """Returns a JSON string representation of the hotel."""
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        """Returns a Hotel object from a JSON string representation."""
        data = json.loads(json_str)
        hotel = cls(data['name'], data['rooms'])
        hotel.reservations = data['reservations']
        return hotel


class Customer:
    """
    A class used to represent a Customer.

    ...

    Attributes
    ----------
    name : str
        the name of the customer

    Methods
    -------
    to_json()
        Returns a JSON string representation of the customer
    from_json(json_str)
        Returns a Customer object from a JSON string representation
    """

    def __init__(self, name):
        """Initializes Customer with a name."""
        self.name = name

    def to_json(self):
        """Returns a JSON string representation of the customer."""
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        """Returns a Customer object from a JSON string representation."""
        data = json.loads(json_str)
        return cls(data['name'])


def save_to_file(obj, filename):
    """Saves an object to a file in JSON format."""
    with open(filename, 'w', encoding=locale.getencoding()) as file:
        file.write(obj.to_json())


def load_from_file(cls, filename):
    """Loads an object from a file in JSON format."""
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding=locale.getencoding()) as file:
                return cls.from_json(file.read())
        else:
            return None
    except json.JSONDecodeError as e:
        print(f"Error loading data from {filename}: Invalid JSON data. {e}")
        return None
    except FileNotFoundError:
        print(f"Error loading data from {filename}: File not found.")
        return None


def create_hotel(name, rooms):
    """Creates a new hotel and saves it to a file."""
    hotel = Hotel(name, rooms)
    save_to_file(hotel, f'{name}.hotel')


def delete_hotel(name):
    """Deletes a hotel by removing its file."""
    if os.path.exists(f'{name}.hotel'):
        os.remove(f'{name}.hotel')


def display_hotel(name):
    """Displays the details of a hotel."""
    hotel = load_from_file(Hotel, f'{name}.hotel')
    if hotel:
        print(f'Hotel Name: {hotel.name}')
        print(f'Available Rooms: {hotel.rooms}')
        print('Reservations:')
        for customer in hotel.reservations:
            print(f' - {customer}')


def modify_hotel(name, new_rooms):
    """Modifies the number of rooms in a hotel."""
    hotel = load_from_file(Hotel, f'{name}.hotel')
    if hotel and new_rooms is not None:
        # Calculate the difference between the old and new total
        # number of rooms
        room_difference = new_rooms - (hotel.rooms + len(hotel.reservations))
        # Adjust the number of available rooms based on the difference
        hotel.rooms += room_difference
        # Ensure that the number of available rooms does not become negative
        hotel.rooms = max(hotel.rooms, 0)
        save_to_file(hotel, f'{name}.hotel')


def create_customer(name):
    """Creates a new customer and saves it to a file."""
    customer = Customer(name)
    save_to_file(customer, f'{name}.customer')


def delete_customer(name):
    """Deletes a customer by removing its file."""
    if os.path.exists(f'{name}.customer'):
        os.remove(f'{name}.customer')


def display_customer(name):
    """Displays the details of a customer."""
    customer = load_from_file(Customer, f'{name}.customer')
    if customer:
        print(f'Customer Name: {customer.name}')


def modify_customer(old_name, new_name):
    """Modifies the name of a customer."""
    customer = load_from_file(Customer, f'{old_name}.customer')
    if customer:
        customer.name = new_name
        save_to_file(customer, f'{new_name}.customer')
        if old_name != new_name:
            os.remove(f'{old_name}.customer')
            # Update customer name in all hotels
            for hotel_file in os.listdir():
                if hotel_file.endswith('.hotel'):
                    hotel = load_from_file(Hotel, hotel_file)
                    if hotel.update_reservation(old_name, new_name):
                        save_to_file(hotel, hotel_file)


def create_reservation(customer_name, hotel_name):
    """Creates a reservation for a customer in a hotel."""
    customer = load_from_file(Customer, f'{customer_name}.customer')
    hotel = load_from_file(Hotel, f'{hotel_name}.hotel')
    if customer and hotel:
        if hotel.reserve_room(customer):
            save_to_file(hotel, f'{hotel_name}.hotel')


def cancel_reservation(customer_name, hotel_name):
    """Cancels a reservation for a customer in a hotel."""
    customer = load_from_file(Customer, f'{customer_name}.customer')
    hotel = load_from_file(Hotel, f'{hotel_name}.hotel')
    if customer and hotel:
        if hotel.cancel_reservation(customer):
            save_to_file(hotel, f'{hotel_name}.hotel')
