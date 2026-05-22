import os
import json
import sys
sys.stdout.reconfigure( encoding='utf-8')

print(" Welcome to Contact Book!")
print("="*40)

#Files where contacts will be saved 
CONTACTS_FILE = "contacts.json"

#Load Contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return {}

#Save contacts to File
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

#Add contacts to File
def add_contacts(contacts):
    print("\n➕ ADD NEW CONTACTS")
    print("="*40)
    name = input("Enter Name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    save_contacts(contacts)
    print(f"✅ {name} added successfully!")

#View contacts in File
def view_contacts(contacts):
    print("\n📋 ALL CONTACTS")
    print("="*40)

    if len(contacts) == 0:
        print("❌ No contacts yet!")
        return
    for name, details in contacts.items():
        print(f"👤 Name: {name}")
        print(f"📞 Phone: {details['phone']}")
        print(f"📧 Email: {details['email']}")
        print("-"*40)

#Search contacts in file 
def search_contact(contacts):
    print("\n🔍 SEARCH CONTACT")
    print("="*40)
    name = input("Enter name to search: ")
    
    if name in contacts:
        print(f"👤 Name: {name}")
        print(f"📞 Phone: {contacts[name]['phone']}")
        print(f"📧 Email: {contacts[name]['email']}")
    else:
        print(f"❌ {name} not found!")

#Delete contacts in file
def delete_contact(contacts):
    print("\n🗑️ DELETE CONTACT")
    print("="*40)
    name = input("Enter name to delete: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"✅ {name} deleted successfully!")
    else:
        print(f"❌ {name} not found!")

#Main Menu
contacts = load_contacts()

while True:
    print("\n📒 CONTACT BOOK MENU")
    print("="*40)
    print("1 → Add Contact")
    print("2 → View Contacts")
    print("3 → Search Contact")
    print("4 → Delete Contact")
    print("5 → Exit")
    print("="*40)
    choice = input("Enter Choice (1/2/3): ")
    if choice == "1":
        add_contacts(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        search_contact(contacts)
    elif choice == "4":
        delete_contact(contacts)
    elif choice == "5":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice!")

