'''Features:
1. Student add karo (Validation ke saath)
2. Student ki details dekho (Rich Table & Badge formatting)
3. Student search karo (ID ya Name se)
4. Student update karo (Name ya Marks)
5. Add / Update Marks (Subject-wise validation & grading)
6. Class Analytics & Summary (Topper, Average, Pass/Fail rate)
7. Student delete karo (Confirmation ke saath)
8. Data file me save/load karo (Safe File handling)
9. Error handling (try-except)

Concepts used:
class, object, methods, list/dict, functions, file handling, error handling, rich UI
'''

import os
import sys

# Windows terminal UTF-8 encoding support
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box

console = Console()

# File path relative to this script's directory for reliability across execution environments
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.txt")


class Student:
    """Represents an individual student with academic records."""

    def __init__(self, student_id, name, maths=None, physics=None, chemistry=None):
        self.student_id = str(student_id)
        self.name = str(name).strip()
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

    def has_marks(self):
        """Check if all three subject marks are recorded."""
        return (
            self.maths is not None
            and self.physics is not None
            and self.chemistry is not None
        )

    def total_marks(self):
        """Calculate total marks if all subjects have marks."""
        if self.has_marks():
            return self.maths + self.physics + self.chemistry
        return None

    def percentage(self):
        """Calculate percentage out of 300."""
        total = self.total_marks()
        if total is not None:
            return total / 3.0
        return None

    def grade(self):
        """Determine grade based on percentage."""
        pct = self.percentage()
        if pct is None:
            return "N/A"
        if pct >= 90:
            return "A+"
        if pct >= 80:
            return "A"
        if pct >= 70:
            return "B"
        if pct >= 60:
            return "C"
        if pct >= 50:
            return "D"
        return "F"

    def status(self):
        """Determine Pass/Fail/Pending status (passing marks: >= 33 in each subject)."""
        if not self.has_marks():
            return "[yellow]Pending[/yellow]"
        if self.maths >= 33 and self.physics >= 33 and self.chemistry >= 33:
            return "[bold green]PASS[/bold green]"
        return "[bold red]FAIL[/bold red]"

    def display_card(self):
        """Display a detailed visual card of the student."""
        total = self.total_marks()
        pct = self.percentage()
        grade = self.grade()

        total_str = str(total) if total is not None else "Not Available"
        pct_str = f"{pct:.2f}%" if pct is not None else "Not Available"

        card_content = (
            f"[bold cyan]ID:[/bold cyan] {self.student_id}\n"
            f"[bold cyan]Name:[/bold cyan] {self.name}\n"
            f"[bold cyan]Maths:[/bold cyan] {self.maths if self.maths is not None else 'N/A'}\n"
            f"[bold cyan]Physics:[/bold cyan] {self.physics if self.physics is not None else 'N/A'}\n"
            f"[bold cyan]Chemistry:[/bold cyan] {self.chemistry if self.chemistry is not None else 'N/A'}\n"
            f"[dim]------------------------------------[/dim]\n"
            f"[bold yellow]Total Marks:[/bold yellow] {total_str} / 300\n"
            f"[bold yellow]Percentage:[/bold yellow]  {pct_str}\n"
            f"[bold yellow]Grade:[/bold yellow]       [bold]{grade}[/bold]\n"
            f"[bold yellow]Result:[/bold yellow]      {self.status()}"
        )
        console.print(
            Panel(
                card_content,
                title=f"[bold green]Student Details: {self.name}[/bold green]",
                box=box.ROUNDED,
                expand=False,
            )
        )


students = {}


def load_students():
    """Load students from students.txt safely."""
    students.clear()
    if not os.path.exists(DATA_FILE):
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            line_no = 0
            for line in file:
                line_no += 1
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":")
                if len(parts) != 5:
                    console.print(f"[bold red]! Warning:[/bold red] Line {line_no} has invalid format, skipped.")
                    continue

                sid, sname, m_str, p_str, c_str = parts

                try:
                    maths = None if m_str == "None" else int(m_str)
                    physics = None if p_str == "None" else int(p_str)
                    chemistry = None if c_str == "None" else int(c_str)
                except ValueError:
                    console.print(f"[bold red]! Warning:[/bold red] Corrupted marks on line {line_no}, skipped.")
                    continue

                students[sid] = Student(sid, sname, maths, physics, chemistry)
    except Exception as e:
        console.print(f"[bold red]✗ Error loading file:[/bold red] {e}")


def save_students():
    """Save all student records to students.txt safely."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            for student_id, details in students.items():
                file.write(
                    f"{student_id}:{details.name}:{details.maths}:{details.physics}:{details.chemistry}\n"
                )
        return True
    except Exception as e:
        console.print(f"[bold red]✗ Error saving data to file:[/bold red] {e}")
        return False


def get_valid_marks(subject_name):
    """Prompt user for subject marks between 0 and 100 with error handling."""
    while True:
        raw_val = input(f"Enter {subject_name} marks (0-100) or 'skip': ").strip()
        if raw_val.lower() == "skip":
            return None
        try:
            val = int(raw_val)
            if 0 <= val <= 100:
                return val
            console.print("[bold yellow]! Marks must be between 0 and 100![/bold yellow]")
        except ValueError:
            console.print("[bold red]✗ Invalid input! Please enter a whole number.[/bold red]")


def add_student():
    """Add a new student with comprehensive validation."""
    console.print("\n[bold cyan]--- ADD NEW STUDENT ---[/bold cyan]")
    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        console.print("[bold yellow]! Student ID cannot be empty![/bold yellow]")
        return

    if not student_id.isdigit():
        console.print("[bold yellow]! Student ID must contain numbers only![/bold yellow]")
        return

    if student_id in students:
        console.print(f"[bold yellow]! Student ID '{student_id}' already exists![/bold yellow]")
        return

    student_name = input("Enter Student Name: ").strip()

    if not student_name:
        console.print("[bold yellow]! Name cannot be empty![/bold yellow]")
        return

    if not student_name.replace(" ", "").isalpha():
        console.print("[bold yellow]! Name must contain letters and spaces only![/bold yellow]")
        return

    add_marks_now = input("Do you want to enter marks now? (y/n): ").strip().lower()
    maths, physics, chemistry = None, None, None

    if add_marks_now == "y":
        maths = get_valid_marks("Maths")
        physics = get_valid_marks("Physics")
        chemistry = get_valid_marks("Chemistry")

    students[student_id] = Student(student_id, student_name, maths, physics, chemistry)
    save_students()
    console.print(f"[bold green]✓ Student '{student_name}' (ID: {student_id}) added successfully![/bold green]")


def view_students():
    """Display all students in an attractive Rich Table."""
    console.print("\n[bold cyan]--- ALL STUDENTS LIST ---[/bold cyan]")
    if not students:
        console.print("[yellow]No student records found![/yellow]")
        return

    table = Table(
        title="Student Academic Summary",
        box=box.ROUNDED,
        header_style="bold magenta",
        title_style="bold cyan",
    )

    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Name", style="bold white")
    table.add_column("Maths", justify="right")
    table.add_column("Physics", justify="right")
    table.add_column("Chemistry", justify="right")
    table.add_column("Total (300)", justify="right", style="yellow")
    table.add_column("Percentage", justify="right", style="bold yellow")
    table.add_column("Grade", justify="center", style="bold")
    table.add_column("Status", justify="center")

    for sid, s in sorted(students.items(), key=lambda x: int(x[0]) if x[0].isdigit() else x[0]):
        m_str = str(s.maths) if s.maths is not None else "[dim]-[/dim]"
        p_str = str(s.physics) if s.physics is not None else "[dim]-[/dim]"
        c_str = str(s.chemistry) if s.chemistry is not None else "[dim]-[/dim]"

        total = s.total_marks()
        pct = s.percentage()
        total_str = str(total) if total is not None else "[dim]-[/dim]"
        pct_str = f"{pct:.2f}%" if pct is not None else "[dim]-[/dim]"

        grade = s.grade()
        grade_colored = f"[bold green]{grade}[/bold green]" if grade in ["A+", "A"] else (
            f"[bold yellow]{grade}[/bold yellow]" if grade in ["B", "C"] else (
                f"[bold red]{grade}[/bold red]" if grade in ["D", "F"] else "[dim]N/A[/dim]"
            )
        )

        table.add_row(
            sid,
            s.name,
            m_str,
            p_str,
            c_str,
            total_str,
            pct_str,
            grade_colored,
            s.status(),
        )

    console.print(table)
    console.print(f"[dim]Total records: {len(students)}[/dim]\n")


def search_student():
    """Search for a student by ID or Name."""
    console.print("\n[bold cyan]--- SEARCH STUDENT ---[/bold cyan]")
    if not students:
        console.print("[yellow]No student records found to search![/yellow]")
        return

    query = input("Enter Student ID or Name to search: ").strip()
    if not query:
        console.print("[bold yellow]! Search query cannot be empty![/bold yellow]")
        return

    # Direct match on ID
    if query in students:
        students[query].display_card()
        return

    # Substring search by Name (case-insensitive)
    matches = [s for s in students.values() if query.lower() in s.name.lower()]

    if matches:
        console.print(f"[bold green]Found {len(matches)} matching student(s):[/bold green]")
        for s in matches:
            s.display_card()
    else:
        console.print(f"[bold red]✗ No student found matching '{query}'![/bold red]")


def update_student():
    """Update student name or marks."""
    console.print("\n[bold cyan]--- UPDATE STUDENT ---[/bold cyan]")
    student_id = input("Enter Student ID to update: ").strip()

    if not student_id:
        console.print("[bold yellow]! Student ID cannot be empty![/bold yellow]")
        return

    if student_id not in students:
        console.print(f"[bold red]✗ Student with ID '{student_id}' not found![/bold red]")
        return

    student = students[student_id]
    console.print(f"Editing: [bold white]{student.name}[/bold white] (ID: {student.student_id})")
    console.print("1. Update Name")
    console.print("2. Update Marks")
    console.print("3. Cancel")

    sub_choice = input("Enter your choice (1-3): ").strip()

    if sub_choice == "1":
        new_name = input(f"Enter new name (current: '{student.name}'): ").strip()
        if not new_name:
            console.print("[bold yellow]! Name cannot be empty![/bold yellow]")
            return
        if not new_name.replace(" ", "").isalpha():
            console.print("[bold yellow]! Name must contain letters and spaces only![/bold yellow]")
            return
        student.name = new_name
        save_students()
        console.print("[bold green]✓ Student name updated successfully![/bold green]")

    elif sub_choice == "2":
        manage_marks_for_student(student_id)

    elif sub_choice == "3":
        console.print("[dim]Update cancelled.[/dim]")
    else:
        console.print("[bold red]✗ Invalid option selected![/bold red]")


def manage_marks_for_student(student_id=None):
    """Add or update subject marks for a student."""
    if not student_id:
        console.print("\n[bold cyan]--- ADD / UPDATE MARKS ---[/bold cyan]")
        student_id = input("Enter Student ID: ").strip()

    if not student_id:
        console.print("[bold yellow]! Student ID cannot be empty![/bold yellow]")
        return

    if student_id not in students:
        console.print(f"[bold red]✗ Student with ID '{student_id}' not found![/bold red]")
        return

    student = students[student_id]
    console.print(f"\nEntering marks for: [bold white]{student.name}[/bold white] (ID: {student.student_id})")
    console.print(f"[dim]Current Marks -> Maths: {student.maths}, Physics: {student.physics}, Chemistry: {student.chemistry}[/dim]")

    maths = get_valid_marks("Maths")
    physics = get_valid_marks("Physics")
    chemistry = get_valid_marks("Chemistry")

    if maths is not None:
        student.maths = maths
    if physics is not None:
        student.physics = physics
    if chemistry is not None:
        student.chemistry = chemistry

    save_students()
    console.print("[bold green]✓ Marks updated successfully![/bold green]")
    student.display_card()


def delete_student():
    """Delete a student with confirmation to prevent accidental loss."""
    console.print("\n[bold cyan]--- DELETE STUDENT ---[/bold cyan]")
    student_id = input("Enter Student ID to delete: ").strip()

    if not student_id:
        console.print("[bold yellow]! Student ID cannot be empty![/bold yellow]")
        return

    if student_id not in students:
        console.print(f"[bold red]✗ Student with ID '{student_id}' not found![/bold red]")
        return

    student = students[student_id]
    confirm = input(
        f"Are you sure you want to permanently delete '{student.name}' (ID: {student_id})? (y/n): "
    ).strip().lower()

    if confirm == "y":
        students.pop(student_id)
        save_students()
        console.print(f"[bold green]✓ Student (ID: {student_id}) deleted successfully![/bold green]")
    else:
        console.print("[dim]Deletion cancelled.[/dim]")


def class_analytics():
    """Display analytics, toppers, and class performance statistics."""
    console.print("\n[bold cyan]--- CLASS ANALYTICS & SUMMARY ---[/bold cyan]")
    if not students:
        console.print("[yellow]No student records available for analytics![/yellow]")
        return

    total_students = len(students)
    graded_students = [s for s in students.values() if s.has_marks()]

    if not graded_students:
        console.print(f"Total Students: {total_students}")
        console.print("[yellow]! None of the students have complete marks recorded yet.[/yellow]")
        return

    percentages = [s.percentage() for s in graded_students]
    avg_percentage = sum(percentages) / len(percentages)

    passed_count = sum(1 for s in graded_students if "PASS" in s.status())
    failed_count = len(graded_students) - passed_count
    pass_rate = (passed_count / len(graded_students)) * 100

    # Highest scorer / Topper
    topper = max(graded_students, key=lambda s: s.total_marks())

    summary_text = (
        f"[bold white]Total Students Registered:[/bold white] {total_students}\n"
        f"[bold white]Students Evaluated:[/bold white]        {len(graded_students)}\n"
        f"[dim]-----------------------------------------[/dim]\n"
        f"[bold cyan]Class Average Percentage:[/bold cyan]  {avg_percentage:.2f}%\n"
        f"[bold green]Passed Students:[/bold green]           {passed_count} ({pass_rate:.1f}%)\n"
        f"[bold red]Failed Students:[/bold red]           {failed_count}\n"
        f"[dim]-----------------------------------------[/dim]\n"
        f"[bold yellow]* Class Topper:[/bold yellow]            [bold white]{topper.name}[/bold white] (ID: {topper.student_id})\n"
        f"[bold yellow]Topper Score:[/bold yellow]            {topper.total_marks()} / 300 ({topper.percentage():.2f}%) - Grade {topper.grade()}"
    )

    console.print(
        Panel(
            summary_text,
            title="[bold magenta]Academic Performance Report[/bold magenta]",
            box=box.ROUNDED,
            expand=False,
        )
    )


def show_menu():
    """Display the formatted main menu."""
    menu_content = (
        "[bold green]1.[/bold green] Add Student\n"
        "[bold green]2.[/bold green] View All Students (Table)\n"
        "[bold green]3.[/bold green] Search Student (by ID / Name)\n"
        "[bold green]4.[/bold green] Update Student\n"
        "[bold green]5.[/bold green] Add / Update Marks\n"
        "[bold green]6.[/bold green] Class Analytics & Summary\n"
        "[bold green]7.[/bold green] Delete Student\n"
        "[bold green]8.[/bold green] Exit"
    )
    console.print(
        Panel(
            menu_content,
            title="[bold cyan]MAIN MENU[/bold cyan]",
            box=box.ROUNDED,
            expand=False,
        )
    )


def main():
    """Main application loop."""
    console.print(
        Panel(
            "[bold white]STUDENT MANAGEMENT SYSTEM[/bold white]\n"
            "[dim]Python OOP • Rich UI • File Persistence[/dim]",
            box=box.DOUBLE_EDGE,
            style="bold magenta on blue",
            expand=False,
        )
    )

    load_students()
    console.print(f"[dim]Loaded {len(students)} student record(s) from database.[/dim]\n")

    while True:
        show_menu()
        try:
            choice_input = input("Enter your choice (1-8): ").strip()
            if not choice_input:
                continue
            choice = int(choice_input)
        except ValueError:
            console.print("[bold red]✗ Invalid input! Please enter a valid number (1-8).[/bold red]\n")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            manage_marks_for_student()
        elif choice == 6:
            class_analytics()
        elif choice == 7:
            delete_student()
        elif choice == 8:
            console.print(
                Panel(
                    "[bold green]Thank you for using Student Management System![/bold green]\n"
                    "[dim]Data has been saved safely. Goodbye![/dim]",
                    box=box.ROUNDED,
                    expand=False,
                )
            )
            break
        else:
            console.print("[bold red]✗ Invalid choice! Please select an option between 1 and 8.[/bold red]")

        console.print("")


if __name__ == "__main__":
    main()