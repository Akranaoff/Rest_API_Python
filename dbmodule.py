import sqlite3

def create():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    create_query = 'CREATE TABLE IF NOT EXISTS user(id TEXT, pass TEXT)'
    cur.execute(create_query)
    conn.commit()
    conn.close()


def insert(id,password):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    insert_query = 'INSERT INTO user VALUES(?,?)'
    cur.execute(insert_query, (id,password))
    conn.commit()
    conn.close()

def select():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    select_query = 'SELECT * FROM user'
    cur.execute(select_query)
    result = cur.fetchall()
    conn.close()
    return result

def search(id = '', password = ''):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    search_query = 'SELECT * FROM user WHERE id=? AND pass=?'
    cur.execute(search_query,(id,password))
    result = cur.fetchall()
    conn.close()
    return result


#print(search('ck','abc123'))
print(select())