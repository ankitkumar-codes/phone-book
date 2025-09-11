import json
import os


# Contat class using Object-oriented programming


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dic(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

 # Contact book class for


class ContactBook:
    def __init__(self, fileName="contacts.json"):
        self.contacts = []
        self.fileName = fileName
        self.load_contacts()

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added: ", contact.name)

    def view_contacts(self):
        if not self.contacts:
            print("No contact found")
            return
        print("\n All Contacts")
        for idx, c in enumerate(self.contacts, 1):
            print(f"{idx}. Name: {c.name}, Phone: {c.phone}, Email: {c.email}")

    def search_contact(self, name):
        found = [c for c in self.contacts if c.name.lower() == name.lower()]
        if found:
            for c in found:
                print(
                    f"Found- Name: {c.name}, Phone: {c.phone}, Email: {c.email}")
        else:
            print("No contact found with that name")

    def delete_contact(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                self.contacts.remove(c)
                print(f"Contact '{name}' deleted.")
                return
        print("Contact not found.")

    def update_contact(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                new_phone = input("Enter new Phone: ")
                new_email = input("Enter new email: ")
                c.phone = new_phone
                c.email = new_email
                print("Contact updated.")
                return
        print("Contact not found.")

    def save_contacts(self):
        try:
            with open(self.fileName, "w") as f:
                json.dump([c.to_dic() for c in self.contacts], f, indent=4)
            print("Contact saved successfully")
        except Exception as e:
            print("Error in saving contacts", e)

    def load_contacts(self):
        if os.path.exists(self.fileName):
            try:
                with open(self.fileName, "r") as f:
                    contacts_list = json.load(f)
                    for c in contacts_list:
                        contact = Contact(c['name'], c['phone'], c['email'])
                        self.contacts.append(contact)
                print("Contacts loaded.")
            except Exception as e:
                print("Error loading contacts!")


# Function to display the main menu


def show_menu():
    print("\n Contact menu")
    print("1. Add contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Save and exit")


# Main program flow


def main():
    cb = ContactBook()
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a no.")
            continue

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            c = Contact(name, phone, email)
            cb.add_contact(c)

        elif choice == 2:
            cb.view_contacts()

        elif choice == 3:
            name = input("Enter a name to search: ")
            cb.search_contact(name)

        elif choice == 4:
            name = input("Enter a name to update: ")
            cb.update_contact(name)

        elif choice == 5:
            name = input("Enter a name to delete: ")
            cb.delete_contact(name)

        elif choice == 6:
            cb.save_contacts()
            print("Exiting contact book, GoodBye")
            break

        else:
            print("Invalid choice, Please try again")


if __name__ == "__main__":
    main()
