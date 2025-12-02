def student_registration(student_id, student_name, course_enrolled, academic_year):
    return (
        f"Student ID       : {student_id}\n"
        f"Student Name     : {student_name}\n"
        f"Course Enrolled  : {course_enrolled}\n"
        f"Academic Year    : {academic_year}"
    )
if __name__ == "__main__":
    result = student_registration(101, "Akash", "BCA", "2024-25")
    print(result)
