import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, backref

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=False)
    Major = db.Column(db.String(255), default="Math")
    Pass = db.Column(db.Boolean, default=True)


class Course(Base):
    __tablename__ = "course"

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


engine = create_engine(
    "postgresql+psycopg2://postgres:mysecretpassword@localhost:5440/ormlecture",
    echo=True,
)

# Don't combine this with alembic
Base.metadata.create_all(engine)

session = Session(engine)


def create_tables():
    Base.metadata.create_all(engine)


def insert_student():
    new_student = Student(Name="Matthew", Major="English", Pass=True)
    session.add(new_student)
    session.commit()
    output = session.query(Student).all()
    print(output)


def drop_all_tables():
    Base.metadata.drop_all(engine)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    # create_student_table()
    insert_student()
    # session.commit()
    # drop_all_tables()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
