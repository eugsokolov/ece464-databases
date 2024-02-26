import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, backref

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=False)
    Major = db.Column(db.String(255), default="Math")


class Course(Base):
    __tablename__ = "course"

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=False)
    Major = db.Column(db.String(255), default="Math")


class Professor(Base):
    __tablename__ = "professor"

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=False)
    Major = db.Column(db.String(255), default="Math")


class Registration(Base):
    __tablename__ = "registration"

    StudentId = db.Column(
        db.Integer, db.ForeignKey("student.Id"), primary_key=True, nullable=False
    )
    CourseId = db.Column(
        db.Integer, db.ForeignKey("course.Id"), primary_key=True, nullable=False
    )

    student = relationship("Student", backref=backref("registrations", uselist=True))
    course = relationship("Course", backref=backref("registrations", uselist=True))


class Teaches(Base):
    __tablename__ = "teaches"

    ProfessorId = db.Column(
        db.Integer, db.ForeignKey("professor.Id"), primary_key=True, nullable=False
    )
    CourseId = db.Column(
        db.Integer, db.ForeignKey("course.Id"), primary_key=True, nullable=False
    )

    professor = relationship("Professor", backref=backref("teaches", uselist=True))
    course = relationship("Course", backref=backref("teaches", uselist=True))


engine = create_engine(
    "postgresql+psycopg2://postgres:mysecretpassword@localhost:5440/ormlecture",
    echo=True,
)

# Don't combine this with alembic
Base.metadata.create_all(engine)

session = Session(engine)


def create_tables():
    Base.metadata.create_all(engine)


def insert_student(name: str, major: str = "English"):
    new_student = Student(Name=name, Major=major)
    session.add(new_student)
    session.commit()


def insert_course(name: str, major: str = "English"):
    new_course = Course(Name=name, Major=major)
    session.add(new_course)
    session.commit()


def insert_many_students():
    with session.begin():
        session.add_all(
            [
                Student(Name="David", Major="Math"),
                Student(Name="John", Major="Science"),
                Student(Name="James", Major="Math"),
            ]
        )


def register(student_id: int, course_id: int):
    new_registration = Registration(StudentId=student_id, CourseId=course_id)
    session.add(new_registration)
    session.commit()


def get_all_students():
    output = session.query(Student).all()
    print(output)
    return output


def get_student_by_id(student_id: int):
    output = session.query(Student).filter(Student.Id == student_id).one_or_none()
    print(output)
    return output


def drop_all_tables():
    Base.metadata.drop_all(engine)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    all_courses = session.query(Course)
    filtered = all_courses.filter(Course.teaches != None).all()
    print(len(filtered))
