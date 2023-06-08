from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import date

# Создание подключения к базе данных
engine = create_engine('postgresql://postgres:35502@localhost/postgres')
Session = sessionmaker(bind=engine)
session = Session()

# Создание базовой модели
Base = declarative_base()

# Определение сущностей базы данных
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    date_of_birth = Column(Date)

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    degree = Column(String)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    grade = Column(Float)
    student = relationship("Student", backref="grades")
    course = relationship("Course", backref="grades")

    # Определение моделей данных для входных и выходных данных

class StudentCreate(BaseModel):
    name: str
    surname: str
    date_of_birth: date

class StudentUpdate(BaseModel):
    name: str
    surname: str
    date_of_birth: date

class TeacherCreate(BaseModel):
    name: str
    surname: str
    degree: str

class CourseCreate(BaseModel):
    name: str
    description: str

class GradeCreate(BaseModel):
    student_id: int
    course_id: int
    grade: float

class GradeUpdate(BaseModel):
    grade: float