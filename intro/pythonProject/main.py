# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import tornado


# Wrapper for getting input from the terminal
def get_input() -> str:
    return input("Enter a command:\n")


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def overwrite_file(filename: str, contents: str):
    with open(filename, "w") as f:
        f.write(contents)


MY_DATABASE = "my_database.txt"
STUDENTS = "students.txt"
COURSES = "courses.txt"
REGISTRATION = "registration.txt"

students = {
    1: {"name": "John"},
    2: {"name": "Steve"},
    3: {"name": "Bill"},
    4: {"name": "Bob"},
    5: {"name": "Joe"},
}

courses = {
    1: {
        "name": "Databases",
        "course_number": 465,
        "instructor": "Katz",
        "num_seats": 3,
    },
    2: {
        "name": "Compilers",
        "course_number": 466,
        "instructor": "Hak",
        "num_seats": 3,
    },
}

registrations = [
    # {"student_id": 1, "course_id": 1},
    # {"student_id": 1, "course_id": 2},
    # {"student_id": 2, "course_id": 1},
]


def get_courses(student_id: int) -> list[int]:
    return [c["course_id"] for c in registrations if c["student_id"] == student_id]


def num_registered_students(course_id: int) -> int:
    return len([c for c in registrations if c["course_id"] == course_id])


def remaining_seats(course_id: int) -> int:
    return courses[course_id]["num_seats"] - num_registered_students(course_id)


def register_student(student_id: int, course_id: int) -> bool:
    """Returns false if the class is full"""
    n_seats = remaining_seats(course_id)
    if n_seats <= 0:
        return False
    registrations.append({"student_id": student_id, "course_id": course_id})
    return True


def drop_student(student_id: int, course_id: int) -> bool:
    """returns false if the student isn't in the course"""
    record = [
        r
        for r in registrations
        if r["student_id"] == student_id and r["course_id"] == course_id
    ]

    if len(record) == 0:
        return False

    assert len(record) == 1
    registrations.remove(record[0])
    return True


def load_registrations():
    filename = MY_DATABASE
    with open(filename, "r") as f:
        for line in f:
            student_id, course_id = line.split(",")
            register_student(int(student_id), int(course_id))


def save_registrations():
    filename = MY_DATABASE
    with open(filename, "w") as f:
        for r in registrations:
            f.write(f"{r['student_id']},{r['course_id']}\n")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    # save_registrations()
    load_registrations()
    print(registrations)

    # assert register_student(3, 1) == True
    # assert register_student(4, 1) == False
    # assert drop_student(4, 1) == False
    # assert drop_student(1, 1) == True
    # assert num_registered_students(1) == 2

    # print(get_courses(1))
    # print(remaining_seats(1))
    # print(remaining_seats(2))
    # print(remaining_seats(3))
    # overwrite_file(MY_DATABASE, "Hello, World!")
    # print(read_file(MY_DATABASE))
    # while True:
    #     try:
    #         i = get_input()
    #     except Exception as e:
    #         print(f"Error: {e}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
