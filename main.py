"""
This main module provides a simple command-line interface to the hotel
reservation system.
"""
import abstractions as a


def main():
    """Run the main command-line interface for the hotel reservation system."""
    # Create 3 hotels
    list_of_hotels = ['Hotel California', 'Hotel Dusk', 'Hotel Transylvania']
    list_of_rooms = [100, 50, 150]
    for hotel, rooms in zip(list_of_hotels, list_of_rooms):
        a.create_hotel(hotel, rooms)

    # Display all hotels
    print('Displaying all hotels...')
    for hotel in list_of_hotels:
        a.display_hotel(hotel)
    print()

    # Create 9 customers
    list_of_customers = ['John Doe', 'Jane Doe', 'James Doe', 'Jill Doe',
                         'Jack Doe', 'Jenny Doe', 'Jared Doe', 'Jasmine Doe',
                         'Jade Doe']
    for customer in list_of_customers:
        a.create_customer(customer)

    # Display all customers
    print('Displaying all customers...')
    for customer in list_of_customers:
        a.display_customer(customer)
    print()

    # Create 9 reservations
    a.create_reservation('John Doe', 'Hotel California')
    a.create_reservation('Jane Doe', 'Hotel California')
    a.create_reservation('James Doe', 'Hotel California')
    a.create_reservation('Jill Doe', 'Hotel Dusk')
    a.create_reservation('Jack Doe', 'Hotel Dusk')
    a.create_reservation('Jenny Doe', 'Hotel Dusk')
    a.create_reservation('Jared Doe', 'Hotel Transylvania')
    a.create_reservation('Jasmine Doe', 'Hotel Transylvania')
    a.create_reservation('Jade Doe', 'Hotel Transylvania')

    # Display all hotels
    print('Displaying all hotels with new reservations...')
    for hotel in list_of_hotels:
        a.display_hotel(hotel)
    print()

    # Modify hotel
    a.modify_hotel('Hotel California', 200)
    a.modify_hotel('Hotel Dusk', 100)
    a.modify_hotel('Hotel Transylvania', 300)

    # Display all hotels
    print('Displaying all hotels with modified available rooms...')
    for hotel in list_of_hotels:
        a.display_hotel(hotel)
    print()

    # Modify 6 customers
    old_names = ['John Doe', 'Jane Doe', 'Jill Doe', 'Jack Doe', 'Jared Doe',
                 'Jasmine Doe']
    new_names = ['John Smith', 'Jane Smith', 'Jill Smith', 'Jack Smith',
                 'Jared Smith', 'Jasmine Smith']
    for old, new in zip(old_names, new_names):
        a.modify_customer(old, new)

    # Display all customers
    print('Displaying all customers with modified names...')
    list_of_customers = ['John Smith', 'Jane Smith', 'James Doe', 'Jill Smith',
                         'Jack Smith', 'Jenny Doe', 'Jared Smith',
                         'Jasmine Smith', 'Jade Doe']
    for customer in list_of_customers:
        a.display_customer(customer)
    print()

    # Display all hotels
    print('Displaying all hotels with modified reservations...')
    for hotel in list_of_hotels:
        a.display_hotel(hotel)
    print()

    # Cancel 6 reservations
    a.cancel_reservation('John Smith', 'Hotel California')
    a.cancel_reservation('Jane Smith', 'Hotel California')
    a.cancel_reservation('Jill Smith', 'Hotel Dusk')
    a.cancel_reservation('Jack Smith', 'Hotel Dusk')
    a.cancel_reservation('Jared Smith', 'Hotel Transylvania')
    a.cancel_reservation('Jasmine Smith', 'Hotel Transylvania')

    # Display all hotels
    print('Displaying all hotels with cancelled reservations...')
    for hotel in list_of_hotels:
        a.display_hotel(hotel)


if __name__ == "__main__":
    main()
