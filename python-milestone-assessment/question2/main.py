"""Simple Employee File Management.

Stores employee records in employees.txt (ID,Name,Role,Salary per line),
reads them back and produces a short report.
"""

import os
import sys

FILE_NAME = "employees.txt"
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)
HIGH_SALARY_LIMIT = 50000


class Employee:
    """A single employee record."""

    def __init__(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = salary

    def display_details(self):
        """Print the employee on one line."""
        print(f"{self.employee_id} - {self.name} - {self.role} - ₹{self.salary}")


def add_employee(employee, path=FILE_PATH):
    """Append one employee record to the file."""
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{employee.employee_id},{employee.name},{employee.role},{employee.salary}\n")


def read_employees(path=FILE_PATH):
    """Read all employees from the file.

    Raises FileNotFoundError if the file does not exist; the caller handles it.
    """
    employees = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            employee_id, name, role, salary = line.split(",")
            employees.append(Employee(employee_id, name, role, int(salary)))
    return employees


def find_employees_above_salary(employees, limit):
    """Return employees whose salary is strictly greater than the limit."""
    return [employee for employee in employees if employee.salary > limit]


def find_highest_salary(employees):
    """Return the employee with the highest salary, or None if the list is empty."""
    if not employees:
        return None
    return max(employees, key=lambda employee: employee.salary)


def find_employees_by_role(employees):
    """Group employees by role. Returns {role: [Employee, ...]}."""
    groups = {}
    for employee in employees:
        groups.setdefault(employee.role, []).append(employee)
    return groups


def main():
    try:
        employees = read_employees()
    except FileNotFoundError:
        print(f"Error: '{FILE_NAME}' was not found at {FILE_PATH}.")
        return
    except ValueError:
        print(f"Error: '{FILE_NAME}' contains a malformed line or salary.")
        return

    if not employees:
        print("No employees found in the file.")
        return

    print("\n===== Employee Details =====\n")
    for employee in employees:
        employee.display_details()

    print(f"\n===== Employees with Salary > {HIGH_SALARY_LIMIT} =====\n")
    for employee in find_employees_above_salary(employees, HIGH_SALARY_LIMIT):
        print(f"{employee.name} - ₹{employee.salary}")

    highest = find_highest_salary(employees)
    print("\nHighest Paid Employee:")
    print(f"{highest.name} - ₹{highest.salary}")

    print("\nEmployee Count by Role:")
    for role, members in sorted(find_employees_by_role(employees).items()):
        print(f"{role}: {len(members)}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")  # so ₹ prints on Windows consoles
    main()
