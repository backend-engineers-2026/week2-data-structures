
# Initialize contact list
contacts = [
    {"name": "Eric Muthui", "phone": "07123456578"},
    {"name": "Emily Blunt", "phone": "0724681012"},
    {"name": "sylvester stallone", "phone": "0787654321"},
    {"name": "Celine Dion", "phone": "0784561232"},
]

def add_contact():
    """Add a new contact to the list"""
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip()
    
    if not name:
        print(" Error: Name cannot be empty!")
        return
    
    # Check if contact already exists
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f" Error: Contact '{name}' already exists!")
            return
    
    phone = input("Enter phone number: ").strip()
    
    if not phone:
        print(" Error: Phone number cannot be empty!")
        return
    
    # Add contact
    contacts.append({"name": name, "phone": phone})
    print(f" Contact '{name}' added successfully!")

    # Remove a contact from the list
def remove_contact():
    print("\n--- Remove Contact ---")
    
    if not contacts:
        print(" Contact list is empty!")
        return
    
    name = input("Enter name to remove: ").strip()
    
    if not name:
        print(" Error: Name cannot be empty!")
        return
    
    # Search for contact
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            removed = contacts.pop(i)
            print(f" Contact '{removed['name']}' removed successfully!")
            return
    
    print(f" Contact '{name}' not found!")

    # Search for a contact by name
def search_contact():
    print("\n--- Search Contact ---")
    
    if not contacts:
        print(" Contact list is empty!")
        return
    
    search_term = input("Enter name to search: ").strip().lower()
    
    if not search_term:
        print(" Error: Search term cannot be empty!")
        return
    
    # Find matching contacts
    results = [c for c in contacts if search_term in c["name"].lower()]
    
    if results:
        print(f"\n Found {len(results)} result(s):")
        print("-" * 40)
        for contact in results:
            print(f"Name:  {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print("-" * 40)
    else:
        print(f" No contacts found matching '{search_term}'")

    # Display all contacts sorted alphabetically by name
def display_all_contacts():
    print("\n--- All Contacts ---")
    
    if not contacts:
        print(" Contact list is empty!")
        return
    
    # Sort contacts alphabetically by name (case-insensitive)
    sorted_contacts = sorted(contacts, key=lambda x: x["name"].lower())
    
    print(f"\n Total Contacts: {len(sorted_contacts)}")
    print("=" * 40)
    
    for i, contact in enumerate(sorted_contacts, 1):
        print(f"{i}. {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print("-" * 40)

    # Display the main menu options
def main():
    while True:
        print("\n" + "=" * 50)
        print(" CONTACT LIST MANAGER")
        print("=" * 50)
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        print("=" * 50)
            
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            remove_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            display_all_contacts()
        elif choice == "5":
            print("\n Thank you for using Contact List Manager!")
            print("Goodbye!\n")
            break
        else:
            print(" Invalid choice! Please enter a number between 1 and 5.")
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()