"""
====================================================
Complaint Management System
====================================================
A menu-driven terminal application using Python,
File Handling (.txt), and Data Structures & Algorithms
(Lists, Dictionaries, Linear Search, Bubble Sort).
====================================================
"""

import os

# File paths for data storage
USERS_FILE = "users.txt"
COMPLAINTS_FILE = "complaints.txt"


# --------------------------------------------------
# File I/O & Initialization Functions
# --------------------------------------------------

def initialize_files():
    """Ensures necessary storage files exist with default admin if empty."""
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            f.write("admin|1234|Admin\n")
    if not os.path.exists(COMPLAINTS_FILE):
        with open(COMPLAINTS_FILE, "w") as f:
            pass


def load_users():
    """Reads users from users.txt into a list of user dictionaries."""
    initialize_files()
    users_list = []
    try:
        with open(USERS_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 3:
                        users_list.append({
                            "username": parts[0],
                            "password": parts[1],
                            "role": parts[2]
                        })
    except Exception as e:
        print(f"[Error reading users file: {e}]")
    return users_list


def save_user(username, password, role="Student"):
    """Appends a new user account to users.txt."""
    try:
        with open(USERS_FILE, "a") as file:
            file.write(f"{username}|{password}|{role}\n")
        return True
    except Exception as e:
        print(f"[Error saving user: {e}]")
        return False


def load_complaints():
    """Reads complaints from complaints.txt into a list of complaint dictionaries."""
    initialize_files()
    complaints_list = []
    try:
        with open(COMPLAINTS_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 6:
                        complaints_list.append({
                            "id": parts[0],
                            "username": parts[1],
                            "department": parts[2],
                            "type": parts[3],
                            "description": parts[4],
                            "status": parts[5]
                        })
    except Exception as e:
        print(f"[Error reading complaints file: {e}]")
    return complaints_list


def save_all_complaints(complaints_list):
    """Overwrites complaints.txt with the current list of complaint dictionaries."""
    try:
        with open(COMPLAINTS_FILE, "w") as file:
            for c in complaints_list:
                file.write(f"{c['id']}|{c['username']}|{c['department']}|{c['type']}|{c['description']}|{c['status']}\n")
        return True
    except Exception as e:
        print(f"[Error saving complaints: {e}]")
        return False


def generate_complaint_id():
    """Generates an automatic unique Complaint ID (starts at 101)."""
    complaints = load_complaints()
    if not complaints:
        return "101"
    max_id = 100
    for c in complaints:
        try:
            current_id = int(c["id"])
            if current_id > max_id:
                max_id = current_id
        except ValueError:
            continue
    return str(max_id + 1)


# --------------------------------------------------
# Validation Functions
# --------------------------------------------------

def validate_student_username(username):
    """Validates that username contains only alphabetic characters."""
    if not username:
        return False, "Username cannot be empty."
    if not username.isalpha():
        return False, "Username must contain ONLY alphabets (no numbers, spaces, or special characters)."
    return True, ""


def validate_student_password(password):
    """Validates that password contains only numbers and is at least 4 digits long."""
    if not password:
        return False, "Password cannot be empty."
    if not password.isdigit():
        return False, "Password must contain ONLY numbers."
    if len(password) < 4:
        return False, "Password must be at least 4 digits long."
    return True, ""


# --------------------------------------------------
# Data Structures & Algorithms (DSA) Core Functions
# --------------------------------------------------

def linear_search_complaint(complaints_list, target_id):
    """
    Performs Linear Search on a list of complaint dictionaries to find a complaint by ID.
    Returns the complaint dictionary if found, otherwise returns None.
    """
    for complaint in complaints_list:
        if str(complaint["id"]) == str(target_id):
            return complaint
    return None


def bubble_sort_complaints(complaints_list):
    """
    Sorts a list of complaint dictionaries by Complaint ID in ascending order using Bubble Sort.
    Returns a new sorted list of complaints.
    """
    sorted_list = list(complaints_list)
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            try:
                id_a = int(sorted_list[j]["id"])
                id_b = int(sorted_list[j + 1]["id"])
            except ValueError:
                id_a = sorted_list[j]["id"]
                id_b = sorted_list[j + 1]["id"]
                
            if id_a > id_b:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list


# --------------------------------------------------
# UI Display Helpers
# --------------------------------------------------

def display_complaint_table(complaints_list):
    """Prints a formatted table displaying complaint records."""
    if not complaints_list:
        print("\n--> No complaints found.")
        return
    
    print("\n" + "=" * 85)
    print(f"{'ID':<6} | {'Username':<12} | {'Department':<12} | {'Type':<15} | {'Status':<12} | {'Description'}")
    print("-" * 85)
    for c in complaints_list:
        desc = c['description']
        if len(desc) > 20:
            desc = desc[:17] + "..."
        print(f"{c['id']:<6} | {c['username']:<12} | {c['department']:<12} | {c['type']:<15} | {c['status']:<12} | {desc}")
    print("=" * 85)


def display_complaint_details(complaint):
    """Prints full details of a single complaint record."""
    print("\n" + "-" * 40)
    print("      COMPLAINT DETAILS")
    print("-" * 40)
    print(f"  Complaint ID : {complaint['id']}")
    print(f"  Username     : {complaint['username']}")
    print(f"  Department   : {complaint['department']}")
    print(f"  ComplaintType: {complaint['type']}")
    print(f"  Description  : {complaint['description']}")
    print(f"  Status       : {complaint['status']}")
    print("-" * 40)


# --------------------------------------------------
# Student Menu Features
# --------------------------------------------------

def add_complaint_feature(username):
    """Prompts student for details and saves a new complaint with Pending status."""
    print("\n--- Add New Complaint ---")
    department = input("Enter Department (e.g., Hostel, Academic, Sanitation): ").strip()
    c_type = input("Enter Complaint Type (e.g., Electricity, Water, Internet): ").strip()
    description = input("Enter Detailed Description: ").strip()
    
    if not department or not c_type or not description:
        print("[!] All fields are required. Complaint creation canceled.")
        return

    new_id = generate_complaint_id()
    new_complaint = {
        "id": new_id,
        "username": username,
        "department": department,
        "type": c_type,
        "description": description,
        "status": "Pending"
    }
    
    complaints = load_complaints()
    complaints.append(new_complaint)
    if save_all_complaints(complaints):
        print(f"\n[SUCCESS] Complaint submitted successfully! Assigned Complaint ID: {new_id}")


def view_my_complaints_feature(username):
    """Displays only the complaints filed by the logged-in student."""
    print(f"\n--- My Complaints ({username}) ---")
    all_complaints = load_complaints()
    student_complaints = [c for c in all_complaints if c["username"].lower() == username.lower()]
    display_complaint_table(student_complaints)


def search_student_complaint_feature(username):
    """Searches for a specific complaint of the student using Linear Search."""
    print("\n--- Search Complaint (Linear Search) ---")
    target_id = input("Enter Complaint ID to search: ").strip()
    
    all_complaints = load_complaints()
    student_complaints = [c for c in all_complaints if c["username"].lower() == username.lower()]
    
    result = linear_search_complaint(student_complaints, target_id)
    if result:
        print("\n[Match Found via Linear Search]")
        display_complaint_details(result)
    else:
        print(f"\n[!] Complaint ID '{target_id}' not found among your complaints.")


def delete_student_complaint_feature(username):
    """Deletes a complaint owned by the student by Complaint ID."""
    print("\n--- Delete Complaint ---")
    target_id = input("Enter Complaint ID to delete: ").strip()
    
    all_complaints = load_complaints()
    target_complaint = linear_search_complaint(all_complaints, target_id)
    
    if not target_complaint:
        print(f"\n[!] Complaint ID '{target_id}' does not exist.")
        return
        
    if target_complaint["username"].lower() != username.lower():
        print("\n[!] Access Denied: You can only delete your own complaints.")
        return

    updated_list = [c for c in all_complaints if str(c["id"]) != str(target_id)]
    if save_all_complaints(updated_list):
        print(f"\n[SUCCESS] Complaint ID '{target_id}' deleted successfully.")


def sort_student_complaints_feature(username):
    """Sorts the student's complaints by Complaint ID using Bubble Sort."""
    print("\n--- Sort My Complaints (Bubble Sort) ---")
    all_complaints = load_complaints()
    student_complaints = [c for c in all_complaints if c["username"].lower() == username.lower()]
    
    if not student_complaints:
        print("\n--> No complaints to sort.")
        return
        
    sorted_complaints = bubble_sort_complaints(student_complaints)
    print("\n[Complaints Sorted by Complaint ID using Bubble Sort]")
    display_complaint_table(sorted_complaints)


def student_menu(username):
    """Displays the student dashboard and handles menu options."""
    while True:
        print(f"\n==========================================")
        print(f"      STUDENT MENU - Welcome, {username}!")
        print(f"==========================================")
        print("1. Add Complaint")
        print("2. View My Complaints")
        print("3. Search Complaint by ID (Linear Search)")
        print("4. Delete Complaint")
        print("5. Sort My Complaints by ID (Bubble Sort)")
        print("6. Logout")
        print("==========================================")
        
        choice = input("Enter option (1-6): ").strip()
        if choice == "1":
            add_complaint_feature(username)
        elif choice == "2":
            view_my_complaints_feature(username)
        elif choice == "3":
            search_student_complaint_feature(username)
        elif choice == "4":
            delete_student_complaint_feature(username)
        elif choice == "5":
            sort_student_complaints_feature(username)
        elif choice == "6":
            print("\nLogging out from Student account...")
            break
        else:
            print("\n[!] Invalid selection. Please enter a number between 1 and 6.")


# --------------------------------------------------
# Admin Menu Features
# --------------------------------------------------

def view_all_complaints_feature():
    """Displays all complaints stored in complaints.txt."""
    print("\n--- All System Complaints ---")
    complaints = load_complaints()
    display_complaint_table(complaints)


def search_admin_complaint_feature():
    """Searches any complaint in the system using Linear Search."""
    print("\n--- Admin Search Complaint (Linear Search) ---")
    target_id = input("Enter Complaint ID to search: ").strip()
    
    complaints = load_complaints()
    result = linear_search_complaint(complaints, target_id)
    
    if result:
        print("\n[Match Found via Linear Search]")
        display_complaint_details(result)
    else:
        print(f"\n[!] Complaint ID '{target_id}' not found.")


def update_complaint_status_feature():
    """Allows Admin to update complaint status (Pending, In Progress, Resolved)."""
    print("\n--- Update Complaint Status ---")
    target_id = input("Enter Complaint ID to update: ").strip()
    
    complaints = load_complaints()
    complaint = linear_search_complaint(complaints, target_id)
    
    if not complaint:
        print(f"\n[!] Complaint ID '{target_id}' not found.")
        return
        
    display_complaint_details(complaint)
    print("\nSelect New Status:")
    print("1. Pending")
    print("2. In Progress")
    print("3. Resolved")
    
    status_choice = input("Enter choice (1-3): ").strip()
    new_status = ""
    if status_choice == "1":
        new_status = "Pending"
    elif status_choice == "2":
        new_status = "In Progress"
    elif status_choice == "3":
        new_status = "Resolved"
    else:
        print("[!] Invalid status choice. Operation canceled.")
        return
        
    complaint["status"] = new_status
    if save_all_complaints(complaints):
        print(f"\n[SUCCESS] Status for Complaint ID '{target_id}' updated to '{new_status}'.")


def sort_all_complaints_feature():
    """Sorts all system complaints by Complaint ID using Bubble Sort."""
    print("\n--- Sort All Complaints (Bubble Sort) ---")
    complaints = load_complaints()
    if not complaints:
        print("\n--> No complaints to sort.")
        return
        
    sorted_complaints = bubble_sort_complaints(complaints)
    print("\n[All Complaints Sorted by Complaint ID using Bubble Sort]")
    display_complaint_table(sorted_complaints)


def admin_menu(username):
    """Displays the admin dashboard and handles menu options."""
    while True:
        print(f"\n==========================================")
        print(f"        ADMIN MENU - Welcome, {username}!")
        print(f"==========================================")
        print("1. View All Complaints")
        print("2. Search Complaint by ID (Linear Search)")
        print("3. Update Complaint Status")
        print("4. Sort All Complaints by ID (Bubble Sort)")
        print("5. Logout")
        print("==========================================")
        
        choice = input("Enter option (1-5): ").strip()
        if choice == "1":
            view_all_complaints_feature()
        elif choice == "2":
            search_admin_complaint_feature()
        elif choice == "3":
            update_complaint_status_feature()
        elif choice == "4":
            sort_all_complaints_feature()
        elif choice == "5":
            print("\nLogging out from Admin account...")
            break
        else:
            print("\n[!] Invalid selection. Please enter a number between 1 and 5.")


# --------------------------------------------------
# Auth & Registration
# --------------------------------------------------

def register_student():
    """Handles student registration with input validation."""
    print("\n--- Student Registration ---")
    users = load_users()
    
    username = input("Enter Username (Alphabets only): ").strip()
    valid, msg = validate_student_username(username)
    if not valid:
        print(f"[!] Validation Error: {msg}")
        return
        
    # Check if username exists
    for u in users:
        if u["username"].lower() == username.lower():
            print("[!] Username already exists. Please choose another username.")
            return

    password = input("Enter Password (Digits only, min 4 characters): ").strip()
    valid, msg = validate_student_password(password)
    if not valid:
        print(f"[!] Validation Error: {msg}")
        return

    if save_user(username, password, role="Student"):
        print(f"\n[SUCCESS] Registration successful! You can now log in as '{username}'.")


def login_system():
    """Handles user login for both Student and Admin roles."""
    print("\n--- User Login ---")
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()
    
    users = load_users()
    user_found = None
    
    for u in users:
        if u["username"].lower() == username.lower() and u["password"] == password:
            user_found = u
            break
            
    if user_found:
        print(f"\n[SUCCESS] Login successful! Role: {user_found['role']}")
        if user_found['role'].lower() == "admin":
            admin_menu(user_found['username'])
        else:
            student_menu(user_found['username'])
    else:
        print("\n[!] Invalid username or password.")


# --------------------------------------------------
# Main Application Loop
# --------------------------------------------------

def main():
    """Main application entry point."""
    initialize_files()
    while True:
        print("\n==========================================")
        print("      COMPLAINT MANAGEMENT SYSTEM         ")
        print("==========================================")
        print("1. Login")
        print("2. Register as Student")
        print("3. Exit Application")
        print("==========================================")
        
        choice = input("Enter choice (1-3): ").strip()
        try:
            if choice == "1":
                login_system()
            elif choice == "2":
                register_student()
            elif choice == "3":
                print("\nThank you for using Complaint Management System. Goodbye!")
                break
            else:
                print("\n[!] Invalid option. Please enter 1, 2, or 3.")
        except Exception as e:
            print(f"\n[!] An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
