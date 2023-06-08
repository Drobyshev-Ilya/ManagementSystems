Выбрать всех студентов, обучающихся на курсе "Математика":

SELECT students.*
FROM students
JOIN grades ON students.id = grades.student_id
JOIN courses ON grades.course_id = courses.id
WHERE courses.name = 'Математика';



Обновить оценку студента по курсу:

UPDATE grades
SET grade = <новая_оценка>
WHERE student_id = <student_id> AND course_id = <course_id>;


Выбрать всех преподавателей, которые преподают в здании №3:

SELECT teachers.*
FROM teachers
JOIN schedule ON teachers.id = schedule.teacher_id
JOIN classrooms ON schedule.classroom_id = classrooms.id
JOIN buildings ON classrooms.building_id = buildings.id
WHERE buildings.id = 3;



Удалить задание для самостоятельной работы, которое было создано более года назад:

DELETE FROM assignments
WHERE date <= CURRENT_DATE - INTERVAL '1 year';



Добавить новый семестр в учебный год:

INSERT INTO semesters (name)
VALUES ('<название_семестра>');