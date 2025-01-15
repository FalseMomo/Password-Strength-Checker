# **Password Strength Checker**

## **Overview**
This project is a Python-based password strength checker designed to help users create secure passwords that adhere to cybersecurity best practices. The program evaluates passwords against a set of criteria recommended by the Cybersecurity and Infrastructure Security Agency (CISA) to ensure they are strong and resilient to attacks.

---

## **Features**
- **Common Password Check**: Verifies the password against a list of 10,000,000 common passwords to avoid easily guessable passwords.
- **Strength Validation**:
  - Ensures a minimum length of 16 characters.
  - Requires at least one uppercase letter.
  - Requires at least one digit.
  - Requires at least one special character, including `!@#$%^&*()_+-=[]{}|;:'",.<>?/~\``.
- **Detailed Feedback**: Provides clear messages to guide users in creating stronger passwords.
- **Error Handling**: Detects missing or inaccessible password files and alerts the user.

---

## **How It Works**
1. The program reads a text file containing common passwords and stores them in a set for fast lookups.
2. It evaluates the user's password against:
   - Common passwords.
   - Length and complexity requirements (uppercase letters, digits, special characters).
3. Provides feedback indicating whether the password is strong or suggests improvements.

---

## **Usage**

### **Requirements**
- Python 3.12.8 installed on your system.

### **Steps to Run**
1. Clone the repository
2. Navigate to the project directory
3. Run the program
3. Enter a password when prompted, and the program will provide feedback 

## **Key Technologies**
- Python
- Regular Expressions (Regex)
- File I/O
- Data Structures (Set)


