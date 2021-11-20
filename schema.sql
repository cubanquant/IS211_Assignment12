CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);

CREATE TABLE quizzes (
    id INTEGER PRIMARY KEY,
    subject_ TEXT,
    numer_of_questions INT,
    date_given TEXT
);

CREATE TABLE quiz_results (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    quiz_id INTEGER,
    score INTEGER
);