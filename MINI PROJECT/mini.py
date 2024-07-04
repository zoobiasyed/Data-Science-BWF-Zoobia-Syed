# Define the ContactManager class
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {
            'name': name,
            'phone': phone,
            'email': email
        }
        self.contacts.append(contact)
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the list.")
        else:
            for idx, contact in enumerate(self.contacts):
                print(f"{idx + 1}. {contact['name']} - {contact['phone']} - {contact['email']}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                print(f"Found contact: {contact['name']} - {contact['phone']} - {contact['email']}")
                return
        print(f"No contact found with name '{name}'.")

    def update_contact(self, name, new_name=None, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                if new_name:
                    contact['name'] = new_name
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                print(f"Contact '{name}' updated.")
                return
        print(f"No contact found with name '{name}'.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' removed.")
                return
        print(f"No contact found with name '{name}'.")

# Main function to interact with the contact manager
def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Update Contact Information")
        print("5. Delete a Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            name = input("Enter contact name to search: ")
            manager.search_contact(name)

        elif choice == '4':
            name = input("Enter contact name to update: ")
            new_name = input("Enter new name (leave blank to keep unchanged): ")
            new_phone = input("Enter new phone number (leave blank to keep unchanged): ")
            new_email = input("Enter new email (leave blank to keep unchanged): ")
            manager.update_contact(name, new_name or None, new_phone or None, new_email or None)

        elif choice == '5':
            name = input("Enter contact name to delete: ")
            manager.delete_contact(name)

        elif choice == '6':
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
