from student import student_registration

def test_student_registration():
    result = student_registration("123", "Akash", "BCA", "2025-26")
    expected = (
        "Student ID       : 123\n"
        "Student Name     : Akash\n"
        "Course Enrolled  : BCA\n"
        "Academic Year    : 2025-26"
    )
    assert result == expected
