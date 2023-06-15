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

# Класс модели для данных студента
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    date_of_birth = Column(Date)
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship('Group', back_populates='students')

# Класс модели для данных оценки
class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    grade = Column(Float)

# Класс модели для данных преподавателя
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    degree = Column(String(255))

# Класс модели для данных курса
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))

# Класс модели для данных группы
class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship('Department', back_populates='groups')
    students = relationship('Student', back_populates='group')

# Класс модели для данных отделения
class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    groups = relationship('Group', back_populates='department')


# Определение моделей данных для входных и выходных данных

# Модель данных для создания нового студента
class CreateStudent(BaseModel):
    name: str
    surname: str
    date_of_birth: date
    group_id: int


# Модель данных для обновления информации о студенте
class UpdateStudent(BaseModel):
    name: str
    surname: str
    date_of_birth: date
    group_id: int

# Модель данных для создания нового курса
class CreateCourse(BaseModel):
    name: str
    description: str


# Модель данных для создания новой оценки
class CreateGrade(BaseModel):
    student_id: int
    course_id: int
    grade: float

# Модель данных для обновления оценки
class UpdateGrade(BaseModel):
    student_id: int
    course_id: int
    grade: float
