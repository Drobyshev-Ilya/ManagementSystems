# UniversityManagementSystems  

Целью этого задания является разработка структуры базы данных и реализация API для "Системы управления университетом".  
Это система, где учитываются студенты, преподаватели, курсы, группы, отделения университета, оценки и другие соответствующие данные.  

## Установка  

1. Клонируйте репозиторий на свой локальный компьютер(https://github.com/Drobyshev-Ilya/ManagementSystems.git).  
2. Перейдите в директорию проекта.  
3. Установите зависимости, выполнив команды:  
pip install sqlalchemy  
pip install fastapi  
pip install uvicorn  
pip install psycopg2  
3. В файле Defining_Database_Entities.py указать свои данные для подключения к БД PostgreSQL в строке:  
engine = create_engine('postgresql://username:password@localhost/dbname')  
4. Создать таблицы в БД (файл с sql запросами создания таблиц - create.sql, файл с sql запросами наполнения таблиц тестовыми данными - insert.sql)  
5. "Часть 2: SQL запросы" находятся в файле sql.sql  
6. ER-диаграмму можно загрузить для просмотра на https://app.diagrams.net/  

## Использование  

1. Запустите сервер с помощью команды `uvicorn main:app --reload`.  
2. Откройте Postman или другой инструмент для тестирования API.  
3. Создайте новые запросы к API, используя доступные точки входа.  

### Пример запроса  

1. Создание нового студента:  

URL: POST http://localhost:8000/students  
Тело запроса (raw JSON):  
```json   
{  
  "name": "Иван",  
  "surname": "Иванов",  
  "date_of_birth": "1995-10-15",  
  "group_id": 1  
}  
```   

2. Получение информации о студенте по его id:  

URL: GET http://localhost:8000/students/{student_id}  

3. Обновление информации о студенте по его id:  

URL: PUT http://localhost:8000/students/{student_id}  
Тело запроса (raw JSON):  
```json   
{  
  "name": "Иван",  
  "surname": "Смирнов",  
  "date_of_birth": "1995-10-15",  
  "group_id": 1  
}  
```   

4. Удаление студента по его id:  

URL: DELETE http://localhost:8000/students/{student_id}  

5. Получение списка всех преподавателей:  

URL: GET http://localhost:8000/teachers

6. Создание нового курса:  

URL: POST http://localhost:8000/courses  
Тело запроса (raw JSON):  
```json   
{  
  "name": "Менеджмент",  
  "description": "Основы менеджмента"  
}  
```   

7. Получение информации о курсе по его id:  

URL: GET http://localhost:8000/courses/{course_id}  

8. Получение списка всех студентов на курсе:  

URL: GET http://localhost:8000/courses/{course_id}/students  

9. Создание новой оценки для студента по курсу:  

URL: POST http://localhost:8000/grades  
Тело запроса (raw JSON):  
```json   
{  
  "student_id": 1,  
  "course_id": 1,  
  "grade": 90.5  
}  
```   

10. Обновление оценки студента по курсу:  

URL: PUT http://localhost:8000/grades/{grade_id}  
Тело запроса (raw JSON):  
```json   
{  
  "student_id": 1,  
  "course_id": 1,  
  "grade": 95.2  
}  
```   

## Точки входа API  
POST /students - создать нового студента.  
GET /students/{student_id} - получить информацию о студенте по его id.  
PUT /students/{student_id} - обновить информацию о студенте по его id.  
DELETE /students/{student_id} - удалить студента по его id.  
GET /teachers - получить список всех преподавателей.  
POST /courses - создать новый курс.  
GET /courses/{course_id} - получить информацию о курсе по его id.  
GET /courses/{course_id}/students - получить список всех студентов на курсе.  
POST /grades - создать новую оценку для студента по курсу.  
PUT /grades/{grade_id} - обновить оценку студента по курсу.  





## Описание каждой сущности и её свойств  

Здание (buildings):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор здания.  
name (VARCHAR(255) NOT NULL): Название здания.  

Аудитория (classrooms):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор аудитории.  
building_id (INTEGER REFERENCES buildings(id)): Идентификатор связанного здания.  
number (VARCHAR(50) NOT NULL): Номер аудитории.  

Отделение (departments):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор отделения.  
name (VARCHAR(255) NOT NULL): Название отделения.  

Группа (groups):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор группы.  
name (VARCHAR(255) NOT NULL): Название группы.  
department_id (INTEGER REFERENCES departments(id)): Идентификатор связанного отделения.  

Студент (students):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор студента.  
name (VARCHAR(255) NOT NULL): Имя студента.  
surname (VARCHAR(255) NOT NULL): Фамилия студента.  
date_of_birth (DATE): Дата рождения студента.  
group_id (INTEGER REFERENCES groups(id)): Идентификатор связанной группы.  

Преподаватель (teachers):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор преподавателя.  
name (VARCHAR(255) NOT NULL): Имя преподавателя.  
surname (VARCHAR(255) NOT NULL): Фамилия преподавателя.  
degree (VARCHAR(255)): Ученая степень преподавателя.  

Курс (courses):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор курса.  
name (VARCHAR(255) NOT NULL): Название курса.  
description (TEXT): Описание курса.  

Оценка (grades):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор оценки.  
student_id (INTEGER REFERENCES students(id)): Идентификатор связанного студента.  
course_id (INTEGER REFERENCES courses(id)): Идентификатор связанного курса.  
grade (FLOAT): Оценка студента по курсу.  

Расписание (schedule):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор записи в расписании.  
course_id (INTEGER REFERENCES courses(id)): Идентификатор связанного курса.  
group_id (INTEGER REFERENCES groups(id)): Идентификатор связанной группы.  
teacher_id (INTEGER REFERENCES teachers(id)): Идентификатор связанного преподавателя.  
classroom_id (INTEGER REFERENCES classrooms(id)): Идентификатор связанной аудитории.  

Семестр (semesters):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор семестра.  
name (VARCHAR(255) NOT NULL): Название семестра.  

Факультет (faculties):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор факультета.  
name (VARCHAR(255) NOT NULL): Название факультета.  

Экзамен (exams):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор экзамена.  
course_id (INTEGER REFERENCES courses(id)): Идентификатор связанного курса.  
semester_id (INTEGER REFERENCES semesters(id)): Идентификатор связанного семестра.  
room_id (INTEGER REFERENCES classrooms(id)): Идентификатор связанной аудитории.  
date (DATE): Дата экзамена.  
time (TIME): Время экзамена.  

Задание для самостоятельной работы (assignments):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор задания.  
course_id (INTEGER REFERENCES courses(id)): Идентификатор связанного курса.  
description (TEXT): Описание задания.  
date (DATE): Дата создания задания.  

Программа курса (course_programs):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор программы курса.  
course_id (INTEGER REFERENCES courses(id)): Идентификатор связанного курса.  
program_content (TEXT): Содержание программы курса.  

Учебный план (curricula):  
id (SERIAL PRIMARY KEY): Уникальный идентификатор учебного плана.  
course_id (INTEGER REFERENCES courses(id)): Идентификатор связанного курса.  
semester_id (INTEGER REFERENCES semesters(id)): Идентификатор связанного семестра.  
group_id (INTEGER REFERENCES groups(id)): Идентификатор связанной группы.  
