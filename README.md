# Complaint Management System (Python + DSA Mini Project)

A menu-driven, console-based **Complaint Management System** built with **Python** and fundamental **Data Structures & Algorithms (DSA)**. It uses flat text files (`.txt`) for persistent data storage without any external database or JSON libraries.

---

## 📁 Folder Structure

```text
Complaint_Management_System/
│
├── main.py          # Main application code (menu system, DSA functions, file operations)
├── users.txt         # File storing user accounts (pipe-separated: Username|Password|Role)
├── complaints.txt    # File storing complaints (pipe-separated: ComplaintID|Username|Department|Type|Description|Status)
└── README.md        # Project documentation
```

---

## 🛠️ Technology Stack & DSA Concepts

- **Language:** Python 3.x
- **Data Storage:** Custom text file handling (`.txt` files with `|` delimiters)
- **Data Structures:**
  - **Lists:** Store records dynamically in memory.
  - **Dictionaries:** Structure individual user and complaint records with key-value pairs (`id`, `username`, `department`, `type`, `description`, `status`).
- **Algorithms:**
  - **Linear Search (`O(n)`):** Sequentially traverses complaints list to find a complaint matching a given Complaint ID.
  - **Bubble Sort (`O(n²)`):** Iteratively compares and swaps adjacent complaint records to sort them by Complaint ID in ascending order.
- **Programming Concepts:** Functions, Exception Handling, Modular Menu-Driven Flow, Input Validation.

---

## 🔐 Data Storage Format

### `users.txt`
```text
admin|1234|Admin
mohamed|1111|Student
john|2222|Student
```

### `complaints.txt`
```text
101|mohamed|Hostel|Electricity|Fan Not Working|Pending
102|john|Academic|Library|Books Not Available|In Progress
103|mohamed|Sanitation|Cleanliness|Washroom Cleaning Required|Resolved
```

---

## 🌟 Key Features

### 👤 Student Login & Features
- **Validation Rules:**
  - Username: Alphabets only (`.isalpha()`), no spaces/numbers/symbols.
  - Password: Numbers only (`.isdigit()`), minimum length of 4 digits.
- **Features:**
  1. **Add Complaint:** Automatically assigns a unique Complaint ID (starts at 101) and sets status to `Pending`.
  2. **View My Complaints:** Filters and displays complaints belonging only to the logged-in student.
  3. **Search Complaint (Linear Search):** Finds a specific complaint owned by the student by Complaint ID.
  4. **Delete Complaint:** Allows students to delete only their own complaints.
  5. **Sort My Complaints (Bubble Sort):** Sorts student's complaints by Complaint ID in ascending order.

### 🔑 Admin Login & Features
- **Default Credentials:**
  - **Username:** `admin`
  - **Password:** `1234`
- **Features:**
  1. **View All Complaints:** Displays every complaint submitted in the system.
  2. **Search Complaint (Linear Search):** Searches for any complaint by Complaint ID.
  3. **Update Complaint Status:** Changes complaint status between `Pending`, `In Progress`, and `Resolved`.
  4. **Sort Complaints (Bubble Sort):** Sorts all system complaints by Complaint ID.

---

## 🚀 How to Run

1. Open a terminal / command prompt.
2. Navigate to the project directory:
   ```bash
   cd "c:\Users\angee\Desktop\complaint management system"
   ```
3. Run the Python application:
   ```bash
   python main.py
   ```

---

## 🛡️ Exception & Error Handling

- Handled invalid menu options gracefully without crashing.
- Prevents duplicate usernames during student registration.
- Prevents non-alphabetic student usernames and non-numeric passwords.
- Validates file availability and handles file reading/writing errors cleanly.
