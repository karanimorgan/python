students = {
    "student1":{
        "personal_info": {
            "name":"John Doe",
            "age": 12
        },
        "contact_info": {
            "address": {
                "city": "Nairobi"
            }
        },
        "academic_info": {
            "units_scores":{
                "math": 78,
                "english": 88,
                "science": 90
            }
        },
        "parents_info": {
            "father": {
                "name": "Doe",
                "occupation": "Engineer"
            },
            "mother": {
                "name": "jane Doe",
                "occupation": "Doctor"
            }
        }
    },
}
def get_student_by_id(student_id):
    return students.get(student_id, "student not found")


def get_student_by_name(name):
    for student_id, student_info in students.items():
        if student_info.get("personal_info", {}).get("name") == name:
            return "student found:" + student_id
        return "student not found"
    
def total_grades():
    for i in students:
        student = students.get(i)
        grades = student.get("academic_info", {}).get("units_scores", {})
        total = sum(grades.values())
        print(f"Total grades for {student.get('personal_info').get('name')}: {total}")
# print(get_student_by_id("student1"))
# print (get_student_by_name("John Doe"))
total_grades()
