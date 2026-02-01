contacts = [
    {"name": "Suzune", "phone": "+254798890865"},
    {"name": "Twilight", "phone": "+0115674538"}
]

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    contacts.append({"name": name, "phone": phone})
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("Contact list is empty.")
        return
    
    print("\nYour Contacts: ")
    sorted_contacts = [contact for contact in sorted(contacts, key=lambda c: c["name"].lower())]

    for i, c in enumerate(sorted_contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")

def search_contact():
    word = input("Search name: ").lower()

    matches = [contact for contact in contacts if word in contact["name"].lower()]

    if not matches:
        print("No matches found.")
        return
    
    for contact in matches:
        print(f"{contact['name']} - {contact['phone']}")

def remove_contact():
    name = input("Name to remove: ").lower()

    for contact in contacts[:]:
        if name in contact["name"].lower():
            contacts.remove(contact)
            print(f"Contact '{contact['name']}' deleted.")
            return
    
    print("Contact not found.")

def show_phone_numbers():
    phones = [contact["phone"] for contact in contacts]
    print(f"Phone numbers: {phones}")

def main():
    while True:
        print("\n1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Remove contact")
        print("5. Show phone numbers")
        print("6. Exit")

        choice = input("Enter a choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            remove_contact()
        elif choice == "5":
            show_phone_numbers()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()