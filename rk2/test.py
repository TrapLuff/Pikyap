import unittest
from rk2 import Student, SchoolClass, Class_Students, find_by_surname, class_by_average_age, find_classes_with_a

class TestSchoolProgram(unittest.TestCase):
    def setUp(self):
        self.students = [
            Student(1, "Иван Иванов", 11, 1),
            Student(2, "Мария Петрова", 12, 1),
            Student(3, "Цекарь Эйсап", 12, 2),
            Student(4, "Анна Кузнецова", 13, 2),
            Student(5, "Игорь Гофман", 14, 3),
            Student(6, "Спартак Бендеров", 17, 4),
            Student(7, "Дмитрий Соколовский", 13, 2),
        ]
        self.school_classes = [
            SchoolClass(1, 5, "А"),
            SchoolClass(2, 7, "Б"),
            SchoolClass(3, 6, "В"),
            SchoolClass(4, 10, "А"),
        ]
        self.relations = [
            Class_Students(1, 1),
            Class_Students(2, 1),
            Class_Students(3, 2),
            Class_Students(4, 2),
            Class_Students(5, 3),
            Class_Students(6, 4),
            Class_Students(7, 2),
        ]

    def test_find_by_surname(self):
        result = find_by_surname(self.students, self.school_classes)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["full_name"], "Иван Иванов")
        self.assertIn("Иван Иванов", [student["full_name"] for student in result])

    def test_class_by_average_age(self):
        result = class_by_average_age(self.students, self.school_classes)
        self.assertEqual(result[0]["class"], "5А")
        self.assertAlmostEqual(result[0]["average_age"], 11.5)
        self.assertGreater(result[-1]["average_age"], result[0]["average_age"])

    def test_find_classes_with_a(self):
        result = find_classes_with_a(self.students, self.school_classes, self.relations)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["class"], "5А")
        self.assertTrue(any(student["full_name"] == "Иван Иванов" for student in result[0]["students"]))

if __name__ == "__main__":
    unittest.main()
