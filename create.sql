-- Создание таблицы "Здание"
CREATE TABLE buildings (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

-- Создание таблицы "Аудитория"
CREATE TABLE classrooms (
  id SERIAL PRIMARY KEY,
  building_id INTEGER REFERENCES buildings(id),
  number VARCHAR(50) NOT NULL
);


-- Создание таблицы "Отделение"
CREATE TABLE departments (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);


-- Создание таблицы "Группа"
CREATE TABLE groups (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  department_id INTEGER REFERENCES departments(id)
);

-- Создание таблицы "Студент"
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  surname VARCHAR(255) NOT NULL,
  date_of_birth DATE,
  group_id INTEGER REFERENCES groups(id)
);

-- Создание таблицы "Преподаватель"
CREATE TABLE teachers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  surname VARCHAR(255) NOT NULL,
  degree VARCHAR(255)
);

-- Создание таблицы "Курс"
CREATE TABLE courses (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT
);


-- Создание таблицы "Оценка"
CREATE TABLE grades (
  id SERIAL PRIMARY KEY,
  student_id INTEGER REFERENCES students(id),
  course_id INTEGER REFERENCES courses(id),
  grade FLOAT
);

-- Создание таблицы "Расписание"
CREATE TABLE schedule (
  id SERIAL PRIMARY KEY,
  course_id INTEGER REFERENCES courses(id),
  group_id INTEGER REFERENCES groups(id),
  teacher_id INTEGER REFERENCES teachers(id),
  classroom_id INTEGER REFERENCES classrooms(id)
);

-- Создание таблицы "Семестр"
CREATE TABLE semesters (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

-- Создание таблицы "Факультет"
CREATE TABLE faculties (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

-- Создание таблицы "Экзамен"
CREATE TABLE exams (
  id SERIAL PRIMARY KEY,
  course_id INTEGER REFERENCES courses(id),
  semester_id INTEGER REFERENCES semesters(id),
  room_id INTEGER REFERENCES classrooms(id),
  date DATE,
  time TIME
);

-- Создание таблицы "Задание для самост. работы"
CREATE TABLE assignments (
  id SERIAL PRIMARY KEY,
  course_id INTEGER REFERENCES courses(id),
  description TEXT,
  date DATE
);

-- Создание таблицы "Программа курса"
CREATE TABLE course_programs (
  id SERIAL PRIMARY KEY,
  course_id INTEGER REFERENCES courses(id),
  program_content TEXT
);

-- Создание таблицы "Учебный план"
CREATE TABLE curricula (
  id SERIAL PRIMARY KEY,
  course_id INTEGER REFERENCES courses(id),
  semester_id INTEGER REFERENCES semesters(id),
  group_id INTEGER REFERENCES groups(id)
);
