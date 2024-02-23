class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score < 60:
            return "F"
        elif 60 <= score <= 69:
            return "D"
        elif 70 <= score <= 79:
            return "C"
        elif 80 <= score <= 89:
            return "B"
        elif 90 <= score:
            return "A"

    def add_course(self, course_name, score):
        self.__courses.setdefault(f"{course_name}", self.calculate_letter_grade(score))
        

    def get_courses(self):
        return self.__courses