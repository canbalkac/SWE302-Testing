import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
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
        tk.Button(self.main_frame, text="Make Reservation", command=self.make_reservation).grid(row=2, column=0, padx=10)
        tk.Button(self.main_frame, text="Cancel Reservation", command=self.cancel_reservation).grid(row=2, column=1, padx=10)

        # Output Area
        self.output_text = tk.Text(self.root, wrap=tk.WORD, width=80, height=20)
        self.output_text.pack(pady=20)

    def get_all_hotels(self):
        """Retrieve all hotel names from the system."""
        return [f[:-6] for f in os.listdir() if f.endswith('.hotel')]

    def get_all_customers(self):
        """Retrieve all customer names from the system."""
        return [f[:-9] for f in os.listdir() if f.endswith('.customer')]

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

    def make_reservation(self):
        """Make a reservation."""
        customer_names = self.get_all_customers()
        if not customer_names:
            messagebox.showwarning("Error", "No customers available!")
            return

        hotel_names = self.get_all_hotels()
        if not hotel_names:
            messagebox.showwarning("Error", "No hotels available!")
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
                messagebox.showwarning("Error", "Please select both a customer and a hotel.")
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

        hotel_names = self.get_all_hotels()
        if not hotel_names:
            messagebox.showwarning("Error", "No hotels available!")
            return

        cancel_window = tk.Toplevel(self.root)
        cancel_window.title("Cancel Reservation")

        tk.Label(cancel_window, text="Select Customer:").pack(pady=10)
        customer_var = tk.StringVar()
        customer_dropdown = ttk.Combobox(cancel_window, textvariable=customer_var)
        customer_dropdown['values'] = customer_names
        customer_dropdown.pack(pady=10)

        tk.Label(cancel_window, text="Select Hotel:").pack(pady=10)
        hotel_var = tk.StringVar()
        hotel_dropdown = ttk.Combobox(cancel_window, textvariable=hotel_var)
        hotel_dropdown['values'] = hotel_names
        hotel_dropdown.pack(pady=10)

        def confirm_cancellation():
            customer_name = customer_var.get()
            hotel_name = hotel_var.get()
            if not customer_name or not hotel_name:
                messagebox.showwarning("Error", "Please select both a customer and a hotel.")
                return
            a.cancel_reservation(customer_name, hotel_name)
            messagebox.showinfo("Success", f"Reservation for '{customer_name}' at '{hotel_name}' canceled!")
            cancel_window.destroy()

        tk.Button(cancel_window, text="Confirm Cancellation", command=confirm_cancellation).pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = HotelReservationGUI(root)
    root.mainloop()
