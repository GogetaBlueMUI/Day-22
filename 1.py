contacts = []

def add_contact():
    name = input("Enter contact name: ").strip()
    phone_number = input("Enter phone number: ").strip()
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print("Contact already exists.")
            return
    contacts.append((name, phone_number))
    print("Contact added successfully.")

def search_contact():
    name = input("Enter contact name to search: ").strip()
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print(f"Name: {contact[0]}, Phone Number: {contact[1]}")
            return
    print("Contact not found.")

def display_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for contact in contacts:
            print(f"Name: {contact[0]}, Phone Number: {contact[1]}")

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        display_contacts()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
