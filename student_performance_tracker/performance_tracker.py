from student import Student
class PerformanceTracker:
    """
    Create the PerformanceTracker Class
    This class will manage multiple students and provide methods to calculate the class average and display student performance.

    To Do:
    Define a class PerformanceTracker.
    Add an attribute students, which is a dictionary where the keys are student names and the values are Student objects.
    Write a method add_student() to add new students to the tracker.
    Write a method calculate_class_average() to calculate the average score across all students.
    Write a method display_student_performance() to print each student's performance.
    """
    def __init__(self):
        self.students = {}

    def add_student(self, name:str, scores:list):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if len(self.students) == 0:  
            return 0  # or return None
        total_scores = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students)


    def display_student_performance(self, passing_score=40):
        for student in self.students.values():
            average = student.calculate_average()
            passing_status = "Passing" if student.is_passing(passing_score) else "Failing"
            print(f"Name: {student.name}, Average: {average:.2f}, Status: {passing_status}")
