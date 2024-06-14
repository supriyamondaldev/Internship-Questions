def display_menu():
    print("\nContact Book Menu:")
    print("1. Add a new contact")
    print("2. Show all contacts")
    print("3. Search for a contact")
    print("4. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added successfully.")
def show_all_contacts(contacts):
    if not contacts:
        print("\n No contacts available.")
    else:
        print("\nContacts:")
        for name , contacts in enumerate(contacts, start=1):
            print(f"{name}. {contacts}")

def search_contact(contacts):
    name = input("Enter the name to search for: ")
    if name in contacts:
        print(f"Contact found: {name} - {contacts[name]}")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '2':
            show_all_contacts(contacts)
        elif choice == '1':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            print("Exiting the Contact Book application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
