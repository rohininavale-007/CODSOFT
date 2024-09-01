# Make a contact list application using python.
import tkinter as tk
from tkinter import messagebox

# Dictionary to store contacts
contacts = {}

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        # Create the main menu
        self.create_main_menu()

    def create_main_menu(self):
        self.main_menu = tk.Frame(self.root)
        self.main_menu.pack(fill='both', expand=True)

        # Add Contact
        add_contact_btn = tk.Button(self.main_menu, text="Add Contact", command=self.show_add_contact)
        add_contact_btn.pack(pady=10)

        # View Contacts
        view_contacts_btn = tk.Button(self.main_menu, text="View Contacts", command=self.show_view_contacts)
        view_contacts_btn.pack(pady=10)

        # Search Contact
        search_contact_btn = tk.Button(self.main_menu, text="Search Contact", command=self.show_search_contact)
        search_contact_btn.pack(pady=10)

        # Update Contact
        update_contact_btn = tk.Button(self.main_menu, text="Update Contact", command=self.show_update_contact)
        update_contact_btn.pack(pady=10)

        # Delete Contact
        delete_contact_btn = tk.Button(self.main_menu, text="Delete Contact", command=self.show_delete_contact)
        delete_contact_btn.pack(pady=10)

    def clear_main_menu(self):
        self.main_menu.pack_forget()

    def show_add_contact(self):
        self.clear_main_menu()
        self.add_contact_frame = tk.Frame(self.root)
        self.add_contact_frame.pack(fill='both', expand=True)

        tk.Label(self.add_contact_frame, text="Name").pack(pady=5)
        self.name_entry = tk.Entry(self.add_contact_frame)
        self.name_entry.pack(pady=5)

        tk.Label(self.add_contact_frame, text="Phone Number").pack(pady=5)
        self.phone_entry = tk.Entry(self.add_contact_frame)
        self.phone_entry.pack(pady=5)

        tk.Label(self.add_contact_frame, text="Email").pack(pady=5)
        self.email_entry = tk.Entry(self.add_contact_frame)
        self.email_entry.pack(pady=5)

        tk.Label(self.add_contact_frame, text="Address").pack(pady=5)
        self.address_entry = tk.Entry(self.add_contact_frame)
        self.address_entry.pack(pady=5)

        tk.Button(self.add_contact_frame, text="Save", command=self.add_contact).pack(pady=10)
        tk.Button(self.add_contact_frame, text="Back", command=self.go_back).pack(pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name in contacts:
            messagebox.showerror("Error", "Contact already exists.")
            return

        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        messagebox.showinfo("Success", "Contact added successfully!")
        self.go_back()

    def show_view_contacts(self):
        self.clear_main_menu()
        self.view_contacts_frame = tk.Frame(self.root)
        self.view_contacts_frame.pack(fill='both', expand=True)

        self.contacts_listbox = tk.Listbox(self.view_contacts_frame, width=50)
        self.contacts_listbox.pack(pady=10)

        for name in contacts:
            self.contacts_listbox.insert(tk.END, f"{name}: {contacts[name]['phone']}")

        tk.Button(self.view_contacts_frame, text="Back", command=self.go_back).pack(pady=10)

    def show_search_contact(self):
        self.clear_main_menu()
        self.search_contact_frame = tk.Frame(self.root)
        self.search_contact_frame.pack(fill='both', expand=True)

        tk.Label(self.search_contact_frame, text="Search by Name or Phone").pack(pady=5)
        self.search_entry = tk.Entry(self.search_contact_frame)
        self.search_entry.pack(pady=5)

        tk.Button(self.search_contact_frame, text="Search", command=self.search_contact).pack(pady=10)
        tk.Button(self.search_contact_frame, text="Back", command=self.go_back).pack(pady=10)

    def search_contact(self):
        search_term = self.search_entry.get()
        results = [f"{name}: {contacts[name]['phone']}" for name in contacts if search_term.lower() in name.lower() or search_term in contacts[name]['phone']]

        if not results:
            messagebox.showinfo("Search Result", "No contacts found.")
            return

        result_str = "\n".join(results)
        messagebox.showinfo("Search Result", result_str)

    def show_update_contact(self):
        self.clear_main_menu()
        self.update_contact_frame = tk.Frame(self.root)
        self.update_contact_frame.pack(fill='both', expand=True)

        tk.Label(self.update_contact_frame, text="Name of Contact to Update").pack(pady=5)
        self.update_name_entry = tk.Entry(self.update_contact_frame)
        self.update_name_entry.pack(pady=5)

        tk.Button(self.update_contact_frame, text="Find", command=self.find_contact_for_update).pack(pady=10)
        tk.Button(self.update_contact_frame, text="Back", command=self.go_back).pack(pady=10)

    def find_contact_for_update(self):
        name = self.update_name_entry.get()
        if name not in contacts:
            messagebox.showerror("Error", "Contact not found.")
            return

        self.clear_main_menu()
        self.update_details_frame = tk.Frame(self.root)
        self.update_details_frame.pack(fill='both', expand=True)

        tk.Label(self.update_details_frame, text="Phone Number").pack(pady=5)
        self.update_phone_entry = tk.Entry(self.update_details_frame)
        self.update_phone_entry.insert(0, contacts[name]['phone'])
        self.update_phone_entry.pack(pady=5)

        tk.Label(self.update_details_frame, text="Email").pack(pady=5)
        self.update_email_entry = tk.Entry(self.update_details_frame)
        self.update_email_entry.insert(0, contacts[name]['email'])
        self.update_email_entry.pack(pady=5)

        tk.Label(self.update_details_frame, text="Address").pack(pady=5)
        self.update_address_entry = tk.Entry(self.update_details_frame)
        self.update_address_entry.insert(0, contacts[name]['address'])
        self.update_address_entry.pack(pady=5)

        tk.Button(self.update_details_frame, text="Update", command=lambda: self.update_contact(name)).pack(pady=10)
        tk.Button(self.update_details_frame, text="Back", command=self.go_back).pack(pady=10)

    def update_contact(self, name):
        contacts[name] = {
            'phone': self.update_phone_entry.get(),
            'email': self.update_email_entry.get(),
            'address': self.update_address_entry.get()
        }
        messagebox.showinfo("Success", "Contact updated successfully!")
        self.go_back()

    def show_delete_contact(self):
        self.clear_main_menu()
        self.delete_contact_frame = tk.Frame(self.root)
        self.delete_contact_frame.pack(fill='both', expand=True)

        tk.Label(self.delete_contact_frame, text="Name of Contact to Delete").pack(pady=5)
        self.delete_name_entry = tk.Entry(self.delete_contact_frame)
        self.delete_name_entry.pack(pady=5)

        tk.Button(self.delete_contact_frame, text="Delete", command=self.delete_contact).pack(pady=10)
        tk.Button(self.delete_contact_frame, text="Back", command=self.go_back).pack(pady=10)

    def delete_contact(self):
        name = self.delete_name_entry.get()
        if name not in contacts:
            messagebox.showerror("Error", "Contact not found.")
            return

        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        self.go_back()

    def go_back(self):
        self.clear_main_menu()
        self.create_main_menu()

    def clear_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

