class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if results:
            for contact in results:
                print(contact)
        else:
            print("No contact found.")

    def update_contact(self, search_term, new_contact):
        for idx, contact in enumerate(self.contacts):
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts[idx] = new_contact
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, search_term):
        for idx, contact in enumerate(self.contacts):
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                del self.contacts[idx]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            manager.add_contact(contact)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone to search: ")
            manager.search_contact(search_term)

        elif choice == '4':
            search_term = input("Enter name or phone to update: ")
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            new_contact = Contact(name, phone, email, address)
            manager.update_contact(search_term, new_contact)

        elif choice == '5':
            search_term = input("Enter name or phone to delete: ")
            manager.delete_contact(search_term)

        elif choice == '6':
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
