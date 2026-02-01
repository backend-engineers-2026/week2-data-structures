# Contact list manager (CLI)
contact = []  # stores the contacts as a list of dictionaries.


# - Add contact (name, phone)
def add_contact(name, phone):
    # Use list of dictionaries: [{"name": "John", "phone": "123"}]
    contact.append({"name": name, "phone": phone})


# - Remove contact
def remove_contact(name):
    global contact
    contact = [c for c in contact if c["name"] != name]


# - Search by name
def search_contact(name):
    for c in contact:
        if c["name"] == name:
            return c
    return None


# - Display all sorted alphabetically
def display_contacts():
    sorted_contacts = sorted(contact, key=lambda item: item["name"])
    for c in sorted_contacts:
        print(f"Name: {c['name']}, Phone: {c['phone']}")


# Main loop
while True:
    print(
        "1. Add Contact\n2. Remove Contact\n3. Search Contact\n4. Display Contacts\n5. Exit"
    )
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter Contact name: ")
        phone = input("Enter Phone number: ")
        add_contact(name, phone)
    elif choice == "2":
        name = input("Enter Contact name to remove: ")
        remove_contact(name)
    elif choice == "3":
        name = input("Enter Contact name to search: ")
        contact_info = search_contact(name)
        if contact_info:
            print(
                f"Found: Name: {contact_info['name']}, Phone: {contact_info['phone']}"
            )
        else:
            print("Contact not found.")
    elif choice == "4":
        display_contacts()
    elif choice == "5":
        break
    else:
        print("Invalid option. Please try again.")
