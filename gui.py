import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import abstractions as a
import os


class HotelReservationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Reservation System")

        # Main Frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

        # Buttons
        tk.Button(self.main_frame, text="View Hotels", command=self.view_hotels).grid(row=0, column=0, padx=10)
        tk.Button(self.main_frame, text="View Customers", command=self.view_customers).grid(row=0, column=1, padx=10)
        tk.Button(self.main_frame, text="Add Hotel", command=self.add_hotel).grid(row=1, column=0, padx=10)
        tk.Button(self.main_frame, text="Add Customer", command=self.add_customer).grid(row=1, column=1, padx=10)
        tk.Button(self.main_frame, text="Modify Hotel", command=self.modify_hotel).grid(row=2, column=0, padx=10)
        tk.Button(self.main_frame, text="Modify Customer", command=self.modify_customer).grid(row=2, column=1, padx=10)
        tk.Button(self.main_frame, text="Delete Hotel", command=self.delete_hotel).grid(row=3, column=0, padx=10)
        tk.Button(self.main_frame, text="Delete Customer", command=self.delete_customer).grid(row=3, column=1, padx=10)
        tk.Button(self.main_frame, text="Make Reservation", command=self.make_reservation).grid(row=4, column=0, padx=10)
        tk.Button(self.main_frame, text="Cancel Reservation", command=self.cancel_reservation).grid(row=4, column=1, padx=10)

        # Output Area
        self.output_text = tk.Text(self.root, wrap=tk.WORD, width=80, height=20)
        self.output_text.pack(pady=20)

    def get_all_hotels(self):
        """Retrieve all hotel names from the system."""
        return [f[:-6] for f in os.listdir() if f.endswith('.hotel')]

    def get_all_customers(self):
        """Retrieve all customer names from the system."""
        return [f[:-9] for f in os.listdir() if f.endswith('.customer')]

    def get_hotels_with_available_rooms(self):
        """Retrieve hotels that have available rooms."""
        hotels = []
        for hotel_name in self.get_all_hotels():
            hotel = a.load_from_file(a.Hotel, f"{hotel_name}.hotel")
            if hotel.rooms > 0:
                hotels.append(hotel_name)
        return hotels

    def get_customers_without_reservation(self):
        """Retrieve customers who do not have a reservation."""
        customers = []
        for customer_name in self.get_all_customers():
            reserved = False
            for hotel_name in self.get_all_hotels():
                hotel = a.load_from_file(a.Hotel, f"{hotel_name}.hotel")
                if customer_name in hotel.reservations:
                    reserved = True
                    break
            if not reserved:
                customers.append(customer_name)
        return customers

    def get_hotels_with_reservations(self, customer_name):
        """Retrieve hotels where a specific customer has a reservation."""
        hotels = []
        for hotel_name in self.get_all_hotels():
            hotel = a.load_from_file(a.Hotel, f"{hotel_name}.hotel")
            if customer_name in hotel.reservations:
                hotels.append(hotel_name)
        return hotels

    def view_hotels(self):
        """Display all hotels."""
        self.output_text.delete(1.0, tk.END)
        hotel_files = self.get_all_hotels()
        if not hotel_files:
            self.output_text.insert(tk.END, "No hotels available.\n")
            return
        for hotel_name in hotel_files:
            hotel = a.load_from_file(a.Hotel, f'{hotel_name}.hotel')
            self.output_text.insert(tk.END, f"Hotel Name: {hotel.name}\n")
            self.output_text.insert(tk.END, f"Available Rooms: {hotel.rooms}\n")
            self.output_text.insert(tk.END, "Reservations:\n")
            for reservation in hotel.reservations:
                self.output_text.insert(tk.END, f" - {reservation}\n")
            self.output_text.insert(tk.END, "\n")

    def view_customers(self):
        """Display all customers."""
        self.output_text.delete(1.0, tk.END)
        customer_files = self.get_all_customers()
        if not customer_files:
            self.output_text.insert(tk.END, "No customers available.\n")
            return
        for customer_name in customer_files:
            customer = a.load_from_file(a.Customer, f'{customer_name}.customer')
            self.output_text.insert(tk.END, f"Customer Name: {customer.name}\n")
        self.output_text.insert(tk.END, "\n")

    def add_hotel(self):
        """Add a new hotel."""
        name = simpledialog.askstring("Add Hotel", "Enter hotel name:")
        if not name:
            return
        rooms = simpledialog.askinteger("Add Hotel", "Enter number of rooms:")
        if not rooms:
            return
        a.create_hotel(name, rooms)
        messagebox.showinfo("Success", f"Hotel '{name}' added with {rooms} rooms!")

    def add_customer(self):
        """Add a new customer."""
        name = simpledialog.askstring("Add Customer", "Enter customer name:")
        if not name:
            return
        a.create_customer(name)
        messagebox.showinfo("Success", f"Customer '{name}' added!")

    def modify_hotel(self):
        """Modify hotel attributes like name or room count."""
        hotels = self.get_all_hotels()
        if not hotels:
            messagebox.showwarning("Error", "No hotels available!")
            return

        modify_window = tk.Toplevel(self.root)
        modify_window.title("Modify Hotel")

        tk.Label(modify_window, text="Select Hotel:").pack(pady=10)
        hotel_var = tk.StringVar()
        hotel_dropdown = ttk.Combobox(modify_window, textvariable=hotel_var)
        hotel_dropdown['values'] = hotels
        hotel_dropdown.pack(pady=10)

        tk.Label(modify_window, text="New Hotel Name:").pack(pady=10)
        new_name_var = tk.StringVar()
        new_name_entry = tk.Entry(modify_window, textvariable=new_name_var)
        new_name_entry.pack(pady=10)

        tk.Label(modify_window, text="New Room Count:").pack(pady=10)
        new_room_var = tk.IntVar()
        new_room_entry = tk.Entry(modify_window, textvariable=new_room_var)
        new_room_entry.pack(pady=10)

        def confirm_modification():
            selected_hotel = hotel_var.get()
            new_name = new_name_var.get()
            new_rooms = new_room_var.get()

            if not selected_hotel or not new_name or not new_rooms:
                messagebox.showerror("Error", "Please fill all fields!")
                return

            a.modify_hotel(selected_hotel, new_rooms)
            if selected_hotel != new_name:
                os.rename(f"{selected_hotel}.hotel", f"{new_name}.hotel")
            messagebox.showinfo("Success", f"Hotel '{selected_hotel}' modified!")
            modify_window.destroy()

        tk.Button(modify_window, text="Confirm Modification", command=confirm_modification).pack(pady=20)

    def modify_customer(self):
        """Modify customer name."""
        customers = self.get_all_customers()
        if not customers:
            messagebox.showwarning("Error", "No customers available!")
            return

        modify_window = tk.Toplevel(self.root)
        modify_window.title("Modify Customer")

        tk.Label(modify_window, text="Select Customer:").pack(pady=10)
        customer_var = tk.StringVar()
        customer_dropdown = ttk.Combobox(modify_window, textvariable=customer_var)
        customer_dropdown['values'] = customers
        customer_dropdown.pack(pady=10)

        tk.Label(modify_window, text="New Customer Name:").pack(pady=10)
        new_name_var = tk.StringVar()
        new_name_entry = tk.Entry(modify_window, textvariable=new_name_var)
        new_name_entry.pack(pady=10)

        def confirm_modification():
            selected_customer = customer_var.get()
            new_name = new_name_var.get()

            if not selected_customer or not new_name:
                messagebox.showerror("Error", "Please fill all fields!")
                return

            a.modify_customer(selected_customer, new_name)
            messagebox.showinfo("Success", f"Customer '{selected_customer}' renamed to '{new_name}'!")
            modify_window.destroy()

        tk.Button(modify_window, text="Confirm Modification", command=confirm_modification).pack(pady=20)

    def delete_hotel(self):
        """Delete a hotel."""
        hotels = self.get_all_hotels()
        if not hotels:
            messagebox.showwarning("Error", "No hotels available!")
            return

        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Hotel")

        tk.Label(delete_window, text="Select Hotel to Delete:").pack(pady=10)
        hotel_var = tk.StringVar()
        hotel_dropdown = ttk.Combobox(delete_window, textvariable=hotel_var)
        hotel_dropdown['values'] = hotels
        hotel_dropdown.pack(pady=10)

        def confirm_deletion():
            selected_hotel = hotel_var.get()
            if not selected_hotel:
                messagebox.showerror("Error", "Please select a hotel to delete.")
                return

            a.delete_hotel(selected_hotel)
            messagebox.showinfo("Success", f"Hotel '{selected_hotel}' deleted!")
            delete_window.destroy()

        tk.Button(delete_window, text="Confirm Deletion", command=confirm_deletion).pack(pady=20)

    def delete_customer(self):
        """Delete a customer."""
        customers = self.get_all_customers()
        if not customers:
            messagebox.showwarning("Error", "No customers available!")
            return

        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Customer")

        tk.Label(delete_window, text="Select Customer to Delete:").pack(pady=10)
        customer_var = tk.StringVar()
        customer_dropdown = ttk.Combobox(delete_window, textvariable=customer_var)
        customer_dropdown['values'] = customers
        customer_dropdown.pack(pady=10)

        def confirm_deletion():
            selected_customer = customer_var.get()
            if not selected_customer:
                messagebox.showerror("Error", "Please select a customer to delete.")
                return

            a.delete_customer(selected_customer)
            messagebox.showinfo("Success", f"Customer '{selected_customer}' deleted!")
            delete_window.destroy()

        tk.Button(delete_window, text="Confirm Deletion", command=confirm_deletion).pack(pady=20)

    def make_reservation(self):
        """Make a reservation."""
        customer_names = self.get_customers_without_reservation()
        if not customer_names:
            messagebox.showwarning("Error", "All customers already have reservations!")
            return

        hotel_names = self.get_hotels_with_available_rooms()
        if not hotel_names:
            messagebox.showwarning("Error", "No hotels with available rooms!")
            return

        reservation_window = tk.Toplevel(self.root)
        reservation_window.title("Make Reservation")

        tk.Label(reservation_window, text="Select Customer:").pack(pady=10)
        customer_var = tk.StringVar()
        customer_dropdown = ttk.Combobox(reservation_window, textvariable=customer_var)
        customer_dropdown['values'] = customer_names
        customer_dropdown.pack(pady=10)

        tk.Label(reservation_window, text="Select Hotel:").pack(pady=10)
        hotel_var = tk.StringVar()
        hotel_dropdown = ttk.Combobox(reservation_window, textvariable=hotel_var)
        hotel_dropdown['values'] = hotel_names
        hotel_dropdown.pack(pady=10)

        def confirm_reservation():
            customer_name = customer_var.get()
            hotel_name = hotel_var.get()
            if not customer_name or not hotel_name:
                messagebox.showerror("Error", "Please select both a customer and a hotel.")
                return

            a.create_reservation(customer_name, hotel_name)
            messagebox.showinfo("Success", f"Reservation made for '{customer_name}' at '{hotel_name}'!")
            reservation_window.destroy()

        tk.Button(reservation_window, text="Confirm Reservation", command=confirm_reservation).pack(pady=20)

    def cancel_reservation(self):
        """Cancel a reservation."""
        customer_names = self.get_all_customers()
        if not customer_names:
            messagebox.showwarning("Error", "No customers available!")
            return

        cancel_window = tk.Toplevel(self.root)
        cancel_window.title("Cancel Reservation")

        tk.Label(cancel_window, text="Select Customer:").pack(pady=10)
        customer_var = tk.StringVar()
        customer_dropdown = ttk.Combobox(cancel_window, textvariable=customer_var)
        customer_dropdown['values'] = customer_names
        customer_dropdown.pack(pady=10)

        def update_hotels(*args):
            selected_customer = customer_var.get()
            if selected_customer:
                hotels = self.get_hotels_with_reservations(selected_customer)
                hotel_dropdown['values'] = hotels

        customer_var.trace('w', update_hotels)

        tk.Label(cancel_window, text="Select Hotel:").pack(pady=10)
        hotel_var = tk.StringVar()
        hotel_dropdown = ttk.Combobox(cancel_window, textvariable=hotel_var)
        hotel_dropdown.pack(pady=10)

        def confirm_cancellation():
            customer_name = customer_var.get()
            hotel_name = hotel_var.get()
            if not customer_name or not hotel_name:
                messagebox.showerror("Error", "Please select both a customer and a hotel.")
                return

            a.cancel_reservation(customer_name, hotel_name)
            messagebox.showinfo("Success", f"Reservation for '{customer_name}' at '{hotel_name}' canceled!")
            cancel_window.destroy()

        tk.Button(cancel_window, text="Confirm Cancellation", command=confirm_cancellation).pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = HotelReservationGUI(root)
    root.mainloop()