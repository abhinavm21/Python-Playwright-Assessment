# Question 2 – Simple Employee File Management

## Problem Statement

Store employee details (ID, Name, Role, Salary) in a text file, read them back, and produce a short report: all employees, employees earning more than ₹50,000, the highest-paid employee, and the number of employees in each role.

## Approach / Logic

1. **Data file** – `employees.txt` holds one employee per line in the form `ID,Name,Role,Salary`.
2. **Employee class** – `Employee` stores `employee_id`, `name`, `role` and `salary`. `display_details()` prints the record as `ID - Name - Role - ₹Salary`.
3. **Adding data** – `add_employee()` appends one record to the file, opening it with a context manager (`with open(...)`).
4. **Reading data** – `read_employees()` opens the file with a context manager, skips blank lines, splits each line on commas, and builds `Employee` objects.
5. **Error handling** – `main()` catches:
   - `FileNotFoundError` – prints a message and exits cleanly
   - `ValueError` – a malformed line or a non-numeric salary
6. **Reports**
   - `find_employees_above_salary()` – list comprehension, salary strictly greater than 50,000
   - `find_highest_salary()` – uses `max()` with a key on salary
   - `find_employees_by_role()` – groups employees into a dictionary `{role: [employees]}`; the counts are the lengths of those lists

The file path is built from the location of `main.py`, so the program runs correctly from any working directory.

## How to Run

Requires Python 3.8 or newer. No third-party packages are needed.

```bash
cd question2
python main.py
```

`employees.txt` must be in the same folder as `main.py`. If it is missing, the program prints an error message instead of crashing.

## Sample Input

`employees.txt`:

```
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000
```

## Sample Output

```
===== Employee Details =====

101 - Rahul - Python Developer - ₹50000
102 - Anjali - Tester - ₹45000
103 - John - Developer - ₹60000
104 - Priya - Tester - ₹48000

===== Employees with Salary > 50000 =====

John - ₹60000

Highest Paid Employee:
John - ₹60000

Employee Count by Role:
Developer: 1
Python Developer: 1
Tester: 2
```

## Python Concepts Used

- **File handling** – reading and appending text with `open()`
- **Context manager** – `with open(...) as file:` so the file is always closed
- **Exception handling** – `try`/`except` for `FileNotFoundError` and `ValueError`
- **Functions** – `add_employee`, `read_employees`, `find_highest_salary`, `find_employees_by_role`, `find_employees_above_salary`, `main`
- **Classes and objects** – `Employee` class with a constructor (`__init__`) and a method (`display_details`)
- **Lists and dictionaries** – list of employees, dictionary for role grouping
- **List comprehension** – filtering employees by salary
- **`max()` with `key`** – finding the highest salary
- **`sys.stdout.reconfigure`** – makes the ₹ symbol print correctly on Windows consoles
