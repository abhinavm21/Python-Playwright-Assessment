# Question 1 – Student Marks Management System

## Problem Statement

Build a simple Python program that accepts marks for multiple students (Python, SQL and AI), calculates each student's total, average, grade and PASS/FAIL result, and then displays a summary that includes the top student and the students with an average above 75.

## Approach / Logic

1. **Input** – `collect_students()` asks for a Student ID and Name, then asks for each subject mark. Marks are validated to be whole numbers between 0 and 100. An empty Student ID ends input.
2. **Storage** – each student is a dictionary with `id`, `name`, a `marks` dictionary, and later `total`, `average`, `grade` and `result`.
3. **Calculations** – `calculate_results()`:
   - Total = sum of the three marks
   - Average = Total / 3
   - Grade from `get_grade()`: A (≥ 80), B (≥ 60), C (≥ 40), F (< 40)
   - Result: PASS if average ≥ 40, otherwise FAIL
4. **Highest average** – `find_highest_average()` uses `max()` with a key on the average.
5. **Above 75** – `find_students_above()` uses a list comprehension to pick names whose average is greater than 75.
6. **Output** – `display_report()` prints each student, then the highest scorer and the students above 75.

## How to Run

Requires Python 3.8 or newer. No third-party packages are needed.

```bash
cd question1
python main.py
```

## Sample Input

```
Enter Student ID (press Enter to finish): 101
Enter Student Name: Rahul
  Python marks for Rahul: 80
  SQL marks for Rahul: 80
  AI marks for Rahul: 80

Enter Student ID (press Enter to finish): 102
Enter Student Name: Anjali
  Python marks for Anjali: 65
  SQL marks for Anjali: 65
  AI marks for Anjali: 65

Enter Student ID (press Enter to finish): 103
Enter Student Name: Priya
  Python marks for Priya: 85
  SQL marks for Priya: 80
  AI marks for Priya: 90

Enter Student ID (press Enter to finish):
```

## Sample Output

```
===== Student Result =====

Student ID: 101
Name: Rahul
Total: 240
Average: 80
Grade: A
Result: PASS

Student ID: 102
Name: Anjali
Total: 195
Average: 65
Grade: B
Result: PASS

Student ID: 103
Name: Priya
Total: 255
Average: 85
Grade: A
Result: PASS

Highest Scoring Student: Priya
Students above 75: Rahul, Priya
```

## Python Concepts Used

- **Lists** – the list of students, and the list comprehension in `find_students_above()`
- **Dictionaries** – each student record and the marks per subject
- **Functions** – `get_grade`, `get_mark`, `collect_students`, `calculate_results`, `find_highest_average`, `find_students_above`, `display_report`, `main`
- **Conditional statements** – grade boundaries and PASS/FAIL check
- **Loops** – `while` loops for input and validation, `for` loops for calculations and output
- **List comprehension** – `[student["name"] for student in students if student["average"] > threshold]`
- **`max()` with `key`** – finding the highest average
- **String formatting** – f-strings and `:g` for clean numbers
