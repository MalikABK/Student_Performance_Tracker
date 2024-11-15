from student import Student
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
class PerformanceTracker(Student):
    def __init__(self, student:dict):
        self.student=student
        super().__init__(name, scores)