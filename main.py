from flask import Flask, session, redirect, url_for, request, render_template, current_app, g
import sqlite3

conn = sqlite3.connect('hw13.db') #connect to the database
cur = conn.cursor() 


students = {
    1 : ['John', 'Smith']
}

quizzes = {
    1 : ['Python Basics', 5, 'February, 5th, 2015']
}

quiz_results = {
    1: [1, 1, 85]
}


#clear tables each time program is run - might remove
for i in ('students','quizzes','quiz_results'):
    cur.execute(f'DROP TABLE IF EXISTS {i}')


#create tables 
cur.execute('''CREATE TABLE IF NOT EXISTS students
            (id INTEGER PRIMARY KEY, 
            first_name TEXT,
            last_name TEXT
            )''')
cur.execute('''CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY,
            subject_ TEXT,
            numer_of_questions INT,
            date_given TEXT
            )''')
cur.execute('''CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            quiz_id INTEGER,
            score INTEGER
            )''')

def populate_table(dict, table):
    #add student data to table 
    for k, v in dict.items():
        v.insert(0, k)
        if table == 'students':
            cur.execute(f'INSERT INTO {table} VALUES (?,?,?)', (v))
        else: 
            cur.execute(f'INSERT INTO {table} VALUES (?,?,?,?)', (v))
    conn.commit()

#populate tables 
populate_table(students, 'students')
populate_table(quizzes, 'quizzes')
populate_table(quiz_results, 'quiz_results')






if __name__ == '__main__':
    

    # print(quiz_results(1, 85))
    results = []
    cur.execute('''SELECT * FROM students''')
    results.append(cur.fetchall())
    cur.execute('''SELECT * FROM quizzes''')
    results.append(cur.fetchall())
    cur.execute('''SELECT qr.score,
                s.first_name
                FROM quiz_results qr
                JOIN students s
                ON qr.student_id = s.id''')
    results.append(cur.fetchall())
    
    for r in results:
        print(r)