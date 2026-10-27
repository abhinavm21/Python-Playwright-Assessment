"""Student Marks Management System.

Collects marks for each student, calculates total, average, grade and
PASS/FAIL result, then prints a summary report.
"""

PASS_MARK = 40
DISTINCTION_AVERAGE = 75
SUBJECTS = ("Python", "SQL", "AI")


def get_grade(average):
    """Return the letter grade for an average mark."""
    if average >= 80:
        return "A"
    if average >= 60:
        return "B"
    if average >= 40:
        return "C"
    return "F"


def get_mark(subject, student_name):
    """Ask the user for one subject mark and validate it (0-100)."""
    while True:
        try:
            mark = int(input(f"  {subject} marks for {student_name}: "))
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if 0 <= mark <= 100:
            return mark
        print("  Marks must be between 0 and 100.")


def collect_students():
    """Read student details from the user until an empty ID is entered."""
    students = []
    while True:
        student_id = input("Enter Student ID (press Enter to finish): ").strip()
        if not student_id:
            break
        name = input("Enter Student Name: ").strip()
        marks = {subject: get_mark(subject, name) for subject in SUBJECTS}
        students.append({"id": student_id, "name": name, "marks": marks})
        print()
    return students


def calculate_results(students):
    """Add total, average, grade and result to every student record."""
    for student in students:
        marks = student["marks"].values()
        student["total"] = sum(marks)
        student["average"] = student["total"] / len(SUBJECTS)
        student["grade"] = get_grade(student["average"])
        student["result"] = "PASS" if student["average"] >= PASS_MARK else "FAIL"
    return students


def find_highest_average(students):
    """Return the student with the highest average, or None if no students."""
    if not students:
        return None
    return max(students, key=lambda student: student["average"])


def find_students_above(students, threshold):
    """Return the names of students whose average is above the threshold."""
    return [student["name"] for student in students if student["average"] > threshold]


def display_report(students):
    """Print the full result report for all students."""
    print("\n===== Student Result =====\n")
    for student in students:
        print(f"Student ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Total: {student['total']}")
        print(f"Average: {student['average']:g}")
        print(f"Grade: {student['grade']}")
        print(f"Result: {student['result']}")
        print()

    top = find_highest_average(students)
    above = find_students_above(students, DISTINCTION_AVERAGE)

    print(f"Highest Scoring Student: {top['name']}")
    print(f"Students above {DISTINCTION_AVERAGE}: {', '.join(above) if above else 'None'}")


def main():
    students = collect_students()
    if not students:
        print("No students entered.")
        return
    display_report(calculate_results(students))


if __name__ == "__main__":
    main()
