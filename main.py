from fastapi import FastAPI, HTTPException
import Defining_Database_Entities as dde


# Создание экземпляра FastAPI
app = FastAPI()

# Реализация маршрутов API

@app.post("/students")
def create_student(student: dde.StudentCreate):
    new_student = dde.Student(name=student.name, surname=student.surname, date_of_birth=student.date_of_birth)
    dde.session.add(new_student)
    dde.session.commit()
    dde.session.refresh(new_student)
    return {"id": new_student.id}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = dde.session.query(dde.Student).get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}")
def update_student(student_id: int, student: dde.StudentUpdate):
    db_student = dde.session.query(dde.Student).get(student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db_student.name = student.name
    db_student.surname = student.surname
    db_student.date_of_birth = student.date_of_birth
    dde.session.commit()
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    student = dde.session.query(dde.Student).get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    dde.session.delete(student)
    dde.session.commit()
    return {"message": "Student deleted successfully"}

@app.get("/teachers")
def get_teachers():
    teachers = dde.session.query(dde.Teacher).all()
    return teachers

@app.post("/courses")
def create_course(course: dde.CourseCreate):
    new_course = dde.Course(name=course.name, description=course.description)
    dde.session.add(new_course)
    dde.session.commit()
    dde.session.refresh(new_course)
    return {"id": new_course.id}

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    course = dde.session.query(dde.Course).get(course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.get("/courses/{course_id}/students")
def get_course_students(course_id: int):
    course = dde.session.query(dde.Course).get(course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    students = dde.session.query(dde.Student).join(dde.Grade).filter(dde.Grade.course_id == course_id).all()
    return students

@app.post("/grades")
def create_grade(grade: dde.GradeCreate):
    student = dde.session.query(dde.Student).get(grade.student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    course = dde.session.query(dde.Course).get(grade.course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    new_grade = dde.Grade(student_id=grade.student_id, course_id=grade.course_id, grade=grade.grade)
    dde.session.add(new_grade)
    dde.session.commit()
    dde.session.refresh(new_grade)
    return {"id": new_grade.id}

@app.put("/grades/{grade_id}")
def update_grade(grade_id: int, grade: dde.GradeUpdate):
    db_grade = dde.session.query(dde.Grade).get(grade_id)
    if db_grade is None:
        raise HTTPException(status_code=404, detail="Grade not found")
    db_grade.grade = grade.grade
    dde.session.commit()
    return {"message": "Grade updated successfully"}
