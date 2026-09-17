class new_var:
    """A small student grade manager that stores a name-to-grade mapping."""

    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        """Add a new student with a grade if the name is valid and unique."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name must be a non-empty string.")
        try:
            grade = float(grade)
        except (TypeError, ValueError):
            raise ValueError("Grade must be a numeric value.")
        if name.strip() in self.students:
            raise ValueError(f"Student '{name.strip()}' already exists.")
        self.students[name.strip()] = grade
        return f"Added student '{name.strip()}' with grade {grade}."

    def remove_student(self, name):
        """Remove a student by name and return a useful status message."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name must be a non-empty string.")
        key = name.strip()
        if key not in self.students:
            raise KeyError(f"Student '{key}' does not exist.")
        del self.students[key]
        return f"Removed student '{key}'."

    def update_grade(self, name, grade):
        """Update an existing student's grade with validation."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name must be a non-empty string.")
        try:
            grade = float(grade)
        except (TypeError, ValueError):
            raise ValueError("Grade must be a numeric value.")
        key = name.strip()
        if key not in self.students:
            raise KeyError(f"Student '{key}' does not exist.")
        self.students[key] = grade
        return f"Updated '{key}' grade to {grade}."

    def get_average_grade(self):
        """Calculate the class average from all stored student grades."""
        if not self.students:
            return 0.0
        return sum(self.students.values()) / len(self.students)

    def display_report(self):
        """Return a nice multi-line grade report for the class."""
        title = f"{'=' * 40}STUDENT GRADE MANAGER{'=' * 40}"
        lines = [title]
        if not self.students:
            lines.append("No students have been added yet.")
        else:
            lines.append("Student Grades:")
            for name, grade in sorted(self.students.items()):
                lines.append(f"- {name}: {grade:.2f}")
            lines.append(f"Class Average: {self.get_average_grade():.2f}")
        lines.append("=" * 80)
        return "\n".join(lines)


if __name__ == "__main__":
    manager = new_var()
    manager.add_student("Alice", 90)
    manager.add_student("Bob", 85)
    manager.add_student("Charlie", 78)
    print(manager.display_report())
        