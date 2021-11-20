import sqlite3


conn = sqlite3.connect('pets.db') #connect to the database

cur = conn.cursor() #once you have a cursor you can start executing sql commnands


#dummy data right now. clear out eventually
tasks = {
    1 : ['clean', 'connor', 'low'],
    2 : ['dishes', 'monk',  'medium'],
    3 : ['cook', 'peggy', 'high']
}

cur.execute('DROP TABLE IF EXISTS user')
cur.execute('DROP TABLE IF EXISTS laborer')
cur.execute('DROP TABLE IF EXISTS task')


# cur.execute('''CREATE TABLE IF NOT EXISTS user
#             (id INTEGER PRIMARY KEY, 
#             username TEXT)''')

# cur.execute('''CREATE TABLE IF NOT EXISTS laborer
#             (id INTEGER PRIMARY KEY, 
#             name TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS task
            (id INTEGER PRIMARY KEY, 
            task TEXT, 
            assigned_to TEXT, 
            priority TEXT)''')
            

# inserts given dictionary data into a given table 
def data_distribute(dict, table):
    for k, v in dict.items():
        v.insert(0, k)
        cur.execute(f'INSERT INTO {table} VALUES (?,?,?,?)', (v))


#insert dummy data into tables
# cur.execute('INSERT INTO user VALUES (?,?,?,,?)', data)
# cur.execute('INSERT INTO laborer VALUES (?,?)', data)
# cur.execute('INSERT INTO task VALUES (?,?,?,?,?)', data)


conn.commit()


if __name__ == '__main__':

    data_distribute(tasks, 'task')

    cur.execute("""
                SELECT * FROM task""")

    results = cur.fetchall()

    for r in results:
        print(r)