# Day 1 - Python Introduction

## 1. What is Python?

Python is a high-level, interpreted, general-purpose programming language designed to make programming simple and readable.

### Key Features
- Easy to learn
- Easy to read
- Cross-platform
- Large community
- Widely used in AI, ML, Web Development, Automation, and Data Science

---

## 2. Why Python?

- Simple syntax
- Huge ecosystem
- Excellent AI/ML libraries
- Fast development
- Strong community support

---

## 3. Interpreter vs Compiler

### Interpreter
- Executes code line by line
- Easier to debug
- Used by Python

### Compiler
- Translates the entire program before execution
- Faster after compilation
- Used by C and C++

---

## 4. Python Execution Process

Source Code
↓
Interpreter
↓
Bytecode
↓
Python Virtual Machine (PVM)
↓
Output

---

## 5. Commands Learned

python --version

python filename.py

---

## 6. What I Practiced Today

- print()
- Escape characters
- ASCII art
- Running Python files
- Writing simple programs

---

## 7. Common Mistakes

- Forgot to close quotation marks
- Used a single backslash (`\`) instead of `\\`
- Missed spaces while printing patterns

---

## 8. Key Takeaways

- Python is interpreted.
- `print()` displays output.
- `\\` prints a backslash.
- Debugging is part of programming.

##y 2 – Variables
📖 What I Learned
1. What is a Variable?
A variable is a name (identifier) that refers to a value stored in memory.
Variables make programs easier to read, write, and update.

Example:

name = "Rudra"
age = 21
2. Why Do We Need Variables?
To store data for later use.
To avoid repeating the same values.
To make code easier to maintain.
3. Variables vs Values
Variable: The name given to data (e.g., age).
Value: The actual data stored (e.g., 21).
4. Assignment Operator (=)
= is the assignment operator.
It assigns a value to a variable.
It does not mean mathematical equality.

Example:

age = 21
5. Dynamic Typing
Python automatically decides the data type.
The same variable can store different types of values.

Example:

x = 10
x = "Python"
6. Variable Naming Rules
Must start with a letter or _.
Can contain letters, numbers, and _.
Cannot start with a number.
Cannot contain spaces or special characters.
Cannot use Python keywords.

Valid:

student_name
age
_marks

Invalid:

2age
student name
class
7. Naming Conventions (PEP 8)
Use lowercase letters.
Separate multiple words with underscores (snake_case).

Example:

student_name
total_marks
average_score
8. Multiple Assignment

Assign multiple variables in one line.

a, b, c = 10, 20, 30
9. Same Value Assignment

Assign the same value to multiple variables.

x = y = z = 100
10. Variable Swapping

Python can swap variables without a temporary variable.

a, b = b, a
11. Best Practices
Use meaningful variable names.
Follow Python naming conventions.
Avoid using built-in function names (e.g., sum, list, str) as variable names.
💡 Key Takeaways
Variables store and manage data.
Python is dynamically typed.
Meaningful variable names improve code readability.
Multiple assignment and swapping make code shorter and cleaner.
Variables are used in every Python program and are the foundation of programming