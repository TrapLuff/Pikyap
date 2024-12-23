# Реализация классов и функций программы
class Student:
    """Школьник"""
    def __init__(self, student_id, full_name, age, class_id):
        self.student_id = student_id
        self.full_name = full_name
        self.age = age
        self.class_id = class_id

    def check_surname(self):
        if len(self.full_name.split()) < 2:
            return False
        surname = self.full_name.split()[-1]
        return surname.endswith("ов")


class SchoolClass:
    """Класс"""
    def __init__(self, class_id, grade, letter):
        self.class_id = class_id
        self.grade = grade
        self.letter = letter


class Class_Students:
    """Многие-ко-многим"""
    def __init__(self, student_id, class_id):
        self.student_id = student_id
        self.class_id = class_id


# Функции

def get_class_name(school_classes, class_id):
    for school_class in school_classes:
        if school_class.class_id == class_id:
            return f"{school_class.grade}{school_class.letter}"
    return "NS"


def find_by_surname(students, school_classes):
    return [
        {
            "full_name": student.full_name,
            "age": student.age,
            "class": get_class_name(school_classes, student.class_id),
        }
        for student in students
        if student.check_surname()
    ]


def class_by_average_age(students, school_classes):
    result = []
    for school_class in school_classes:
        ages = [student.age for student in students if student.class_id == school_class.class_id]
        avg_age = sum(ages) / len(ages) if ages else 0
        result.append({"class": f"{school_class.grade}{school_class.letter}", "average_age": avg_age})
    return sorted(result, key=lambda x: x["average_age"])


def find_classes_with_a(students, school_classes, relations):
    result = []
    for school_class in school_classes:
        if school_class.letter == "А":
            class_students = [
                {
                    "full_name": student.full_name,
                    "age": student.age,
                }
                for relation in relations
                if relation.class_id == school_class.class_id
                for student in students
                if student.student_id == relation.student_id
            ]
            result.append({"class": f"{school_class.grade}{school_class.letter}", "students": class_students})
    return result
