goldentech_university = {
    "name": "GoldenTech Mega University",
    "faculties": {
        "Faculty of Science": {
            "departments": {
                "Computer Science": {
                    "students": {
                        "CS101": {"name": "Alice", "year": 2, "courses": ["CS101", "CS201"]},
                        "CS102": {"name": "Bob", "year": 3, "courses": ["CS201", "CS301"]},
                        "CS103": {"name": "Chloe", "year": 1, "courses": ["CS101", "CS100"]}
                    },
                    "lecturers": {
                        "Dr. Smith": {"courses": ["CS101", "CS201"], "room": "B101"},
                        "Dr. Rose": {"courses": ["CS301", "CS302"], "room": "B102"}
                    }
                },
                "Mathematics": {
                    "students": {
                        "MA101": {"name": "Daniel", "year": 1, "courses": ["MA101", "MA102"]},
                        "MA102": {"name": "Eva", "year": 2, "courses": ["MA201", "MA202"]}
                    },
                    "lecturers": {
                        "Prof. Khan": {"courses": ["MA101", "MA201"], "room": "C203"},
                        "Dr. Lily": {"courses": ["MA102", "MA202"], "room": "C204"}
                    }
                }
            },
            "clubs": ["Math Club", "Tech Innovators", "Robotics"],
            "events": ["Science Fair", "Hackathon"]
        },
        "Faculty of Business": {
            "departments": {
                "Accounting": {
                    "students": {
                        "AC101": {"name": "Fred", "year": 2, "courses": ["AC101", "AC201"]},
                        "AC102": {"name": "Grace", "year": 1, "courses": ["AC100", "AC101"]}
                    },
                    "lecturers": {
                        "Mr. Ken": {"courses": ["AC101", "AC201"], "room": "D302"},
                        "Dr. Zara": {"courses": ["AC100"], "room": "D301"}
                    }
                },
                "Marketing": {
                    "students": {
                        "MK101": {"name": "Henry", "year": 3, "courses": ["MK301", "MK302"]},
                        "MK102": {"name": "Irene", "year": 2, "courses": ["MK201", "MK202"]}
                    },
                    "lecturers": {
                        "Prof. Nancy": {"courses": ["MK201", "MK301"], "room": "D401"},
                        "Dr. Lee": {"courses": ["MK202", "MK302"], "room": "D402"}
                    }
                }
            },
            "clubs": ["Business Leaders Club", "Entrepreneurship Circle"],
            "events": ["Business Summit", "Career Day"]
        }
    },
    "courses": {
        "CS101": {"title": "Intro to Programming", "credits": 3, "instructor": "Dr. Smith"},
        "CS201": {"title": "Data Structures", "credits": 4, "instructor": "Dr. Smith"},
        "CS301": {"title": "AI Basics", "credits": 3, "instructor": "Dr. Rose"},
        "MA101": {"title": "Calculus I", "credits": 4, "instructor": "Prof. Khan"},
        "MA201": {"title": "Linear Algebra", "credits": 4, "instructor": "Prof. Khan"},
        "AC101": {"title": "Financial Accounting", "credits": 3, "instructor": "Mr. Ken"},
        "MK201": {"title": "Digital Marketing", "credits": 3, "instructor": "Prof. Nancy"}
    }
}

def list_all_departments(university):
    departments = []
    for faculty in university["faculties"].values():
        for department in faculty["departments"].keys():
            departments.append(department)
    return departments
# print("Departments in the iuniversity:", list_all_departments(goldentech_university))

def list_all_lecturers(university):
    lecturers = []
    for faculty in university["faculties"].values():
        for department in faculty["departments"].values():
            for lecturer in department["lecturers"].keys():
                lecturers.append(lecturer)
           
    return lecturers
# print("Lecturers in University:", list_all_lecturers(goldentech_university))

def list_all_courses(university):
    courses = []
    for course_code, course_info in university["courses"].items():
        courses.append(f"{course_code}: {course_info["title"]}")
    return courses
# print("courses offered in the university:", list_all_courses(goldentech_university) )

def list_students_in_course(university, course_code):
    student_in_course = []
    for faculty in university["faculties"].values():
        for department in faculty["departments"].values():
            for student_id, student_info in department["students"].items():
                if course_code in student_info["courses"]:
                    student_in_course.append(student_info["name"])
    return student_in_course
# print("Students enrolled in CS101:",list_students_in_course(goldentech_university,"CS101"))
# print("Students enrolled in MA101:", list_students_in_course(goldentech_university, "MA101"))

# list students by faculty
def list_all_students_by_faculty(university, faculty_name):
    pass