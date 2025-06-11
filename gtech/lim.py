from rich import print
from rich.prompt import Prompt
from rich.panel import Panel
import os

# Constant values
MIN_GRADE = 70
MAX_GRADE = 100
MENU_EXIT = "5"
YES_RESPONSE = "y"
ZERO = 0
INDEX_OFFSET = 1

def clear_screen():
    os.system("cls")

def press_enter():
    Prompt.ask("[italic sky_blue3]\nPress Enter to continue")

class StudentManager:
    # Class-level constants for available subjects and year levels
    SUBJECTS = [
        "English",
        "Math",
        "Science",
        "Filipino"
        ]
    YEAR_LEVELS = [
        "Grade 7",
        "Grade 8",
        "Grade 9",
        "Grade 10"
        ]

    def __init__(self):
        # Dictionary to store student data
        self.students = {}

    # Method 1: Display all subjects
    def display_subjects(self):
        for index, subject in enumerate(self.SUBJECTS, start=1):
            print(f"[bold light_cyan1][{index}] | {subject}")

    # Method 2: Display all year levels
    def display_year_levels(self):
        for index, level in enumerate(self.YEAR_LEVELS, start=1):
            print(f"[bold light_cyan1][{index}] | {level}")

    # Method 3: Return True if user inputs 'y'
    def confirm_yes_response(self, prompt_message):
        while True:
            response = Prompt.ask(
                f"\n[steel_blue1]{prompt_message} (y/n)"
            ).strip().lower()

            if response in ("y", "n"):
                return response == YES_RESPONSE
            
            print("[bold red3]Invalid choice. Please enter 'y' or 'n'.")
    
    # Method 4: Prompt user to select a valid index from a list
    def prompt_valid_index(self, prompt_message, max_index):
        while True:
            user_input = Prompt.ask(prompt_message).strip()
            if not user_input.isdigit():
                print("[bold red3]Invalid input. Please enter a number.")
                continue

            index = int(user_input) - INDEX_OFFSET
            if not ZERO <= index < max_index:
                print("[bold red3]Invalid selection.")
                continue

            return index
    
    # Method 5: Add a new student
    def add_student(self):
        while True:
            clear_screen()
            print(Panel(
                "[bold light_cyan1]✎  Student Information",
                border_style="WHITE",
                width=30
            ))

            student_name = Prompt.ask(
                "[bold steel_blue1]Enter student name (Surname, First Name)"
            ).strip()

            if self.is_existing_student(student_name):
                continue

            self.register_new_student(student_name)

            if not self.confirm_yes_response(
                "Would you like to add another student?"):
                break

    # Method 6: Check if student already exists
    def is_existing_student(self, student_name):
        if student_name in self.students:
            print("[bold red3]Student already exists. No changes made.")
            press_enter()
            return True
        return False

    # Method 7: Register new student
    def register_new_student(self, student_name):
        print("\n[bold steel_blue1]↓ Year Levels ↓")
        self.display_year_levels()

        yr_level_index = self.prompt_valid_index(
            "[bold steel_blue1]Select year level",
            len(self.YEAR_LEVELS)
        )

        year_level = self.YEAR_LEVELS[yr_level_index]
        self.students[student_name] = {
            "year_level": year_level,
            "subjects": {subject: [] for subject in self.SUBJECTS}
        }

        print("\n[italic dark_sea_green2]Student added successfully!")

    # Method 8: Select a student by name
    def select_student(self):
        clear_screen()
        if not self.students:
            print("[bold red3]No student records found.")
            press_enter()
            return None

        # Showing all student names
        student_content = "\n".join(
            f"[bold light_cyan1]⤷ {name}" for name in self.students
        )
        print(Panel(
            student_content,
            title="[bold steel_blue1]Students",
            border_style="WHITE",
            width=30
        ))

        selected = Prompt.ask(
            "[bold steel_blue1]Enter student name exactly: ").strip()
        
        if selected not in self.students:
            print("[bold red3]Student not found.")
            press_enter()
            return None

        return selected

    # Method 9: Prompt subject selection
    def select_subject(self):
        self.display_subjects()
        subject_choice = Prompt.ask(
            "\n[bold steel_blue1]Select a Subject"
        ).strip()

        if not subject_choice.isdigit():
            print("[bold red3]Invalid input. Please enter a number.")
            press_enter()
            return None

        subject_index = int(subject_choice) - INDEX_OFFSET
        if not ZERO <= subject_index < len(self.SUBJECTS):
            print("[bold red3]Invalid subject selection.")
            press_enter()
            return None

        return self.SUBJECTS[subject_index]

    # Method 10: Prompt for a valid grade input
    def input_valid_grade(self):
        try:
            grade = float(Prompt.ask(
                "\n[bold steel_blue1]Enter grade: "))
            if not MIN_GRADE <= grade <= MAX_GRADE:
                raise ValueError
            return grade
        except ValueError:
            print(
                f"[bold red3]Grade must be between "
                f"{MIN_GRADE} and {MAX_GRADE}."
            )
            press_enter()
            return None
        
    # Method 11: Confirm grade update if already exists
    def confirm_grade_update(self, subject, current_grades):
        print(
            f"\n[bold light_cyan1]{subject} current grades: "
            f"[bold deep_sky_blue4]{current_grades}"
        )
        update = Prompt.ask(
            "[steel_blue1]Grades already exist. "
            "Do you want to update? (y/n)"
        ).strip().lower()

        if update != YES_RESPONSE:
            print("[italic red3]Grade not updated.")
            press_enter()
            return False

        return True

    # Method 12: Add grade to a subject
    def add_grade(self):
        clear_screen()
        student_name = self.select_student()
        if not student_name:
            return

        student = self.students[student_name]
        subjects = student["subjects"]

        while True:
            clear_screen()
            print(Panel(
                "[bold light_cyan1]✎  Grade Entry",
                border_style="WHITE",
                width=20
            ))

            print(
                "[bold light_cyan1]\nName:"
                f"[bold steel_blue1] {student_name}"
            )

            print("\n[bold steel_blue1]↓ Subjects ↓")

            subject = self.select_subject()
            if subject is None:
                continue

            current_grades = subjects[subject]

            if current_grades and not self.confirm_grade_update(
                subject, current_grades):
                continue

            grade = self.input_valid_grade()
            if grade is None:
                continue

            subjects[subject] = [grade]

            status = "updated" if current_grades else "added"
            print(
                f"\n[italic dark_sea_green2]Grade {status} "
                f"successfully for {subject}."
            )

            if not self.confirm_yes_response(
                "Add another grade?"):
                break
    
    # Method 13: View student info and grades
    def view_student_info(self):
        while True:
            student_name = self.select_student()
            if not student_name:
                return

            clear_screen()
            print(Panel(
                "[bold light_cyan1]✎  Student Record",
                border_style="WHITE",
                width=30
            ))

            student = self.students[student_name]

            print(
                f"[bold light_cyan1]Name: "
                f"[bold deep_sky_blue4]{student_name:<10} "
                f"| [bold light_cyan1]Year Level: "
                f"[bold deep_sky_blue4]{student['year_level']}"
            )

            print(
                f"\n[bold light_cyan1]{'Subjects and Grades':^30}"
            )

            for subject, grades in student["subjects"].items():
                grade_list = grades if grades else "[bold red3]No grades yet"
                print(
                    f"\n[bold light_cyan1]{subject:<12} | "
                    f"[bold deep_sky_blue4]{grade_list}"
                )

            if not self.confirm_yes_response(
                "View another student?"):
                break
    
    # Method 14: Compute average of student grades
    def compute_average(self):
        while True:
            clear_screen()
            student_name = self.select_student()
            if not student_name:
                return

            student = self.students[student_name]
            subjects = student["subjects"]

            total = sum(sum(grades) for grades in subjects.values())
            count = sum(len(grades) for grades in subjects.values())

            if count == ZERO:
                print("[bold red3]No grades to compute average.")
                press_enter()
                return

            clear_screen()
            print(Panel("[bold light_cyan1]✎  Average Computation",
                border_style="WHITE",
                width=30
            ))

            print(f"\n[bold light_cyan1]Name: ",
                  f"[bold deep_sky_blue4]{student_name:<10} ",
                f"| [bold light_cyan1]Year Level: ",
                f"[bold deep_sky_blue4]{student['year_level']}"
            )

            average = total // count
            print(
                "\n[bold light_cyan1]Average Grade: "
                f"[bold deep_sky_blue4]{average:.2f}"
            )

            if not self.confirm_yes_response(
                "Compute another average?"):
                break

    def menu(self):
        OPTIONS = {
            "1": self.add_student,
            "2": self.add_grade,
            "3": self.view_student_info,
            "4": self.compute_average,
            MENU_EXIT: self.exit_program
        }

        while True:
            clear_screen()
            self.display_menu()
            user_choice = Prompt.ask(
                "[bold light_cyan1]Enter your choice (1-5)"
            ).strip()

            action = OPTIONS.get(user_choice)
            if action:
                action()
                if user_choice == MENU_EXIT:
                    break
            else:
                print("[bold red3]Invalid option!"
                "\nPlease enter a number between 1 and 5.")
                press_enter()

    def exit_program(self):
        clear_screen()
        print("[italic steel_blue1]Returning to team menu.")

    def display_menu(self):
        print(Panel(
            "[bold italic light_cyan1]"
            "✎  Welcome to Student Management System!",
            border_style="light_cyan1",
            width=45
        ))
        print("\n".join([
            "[italic steel_blue1][1] Add Student",
            "[italic steel_blue1][2] Add Grade",
            "[italic steel_blue1][3] View Student Info",
            "[italic steel_blue1][4] Compute Average",
            "[italic steel_blue1][5] Exit"
        ]))

# Add to main.py
lim = StudentManager()
lim.menu()