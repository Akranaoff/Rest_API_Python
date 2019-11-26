import sqlite3

def create():
    conn = sqlite3.connect('store.db')
    cur = conn.cursor()
    create_query1 = 'CREATE TABLE IF NOT EXISTS stores(store_id INT PRIMARY KEY, name TEXT)'
    create_query2 = 'CREATE TABLE IF NOT EXISTS items(prod_id INT PRIMARY KEY, name TEXT, price INT)'
    cur.execute(create_query1)
    cur.execute(create_query2)
    conn.commit()
    conn.close()

def insert_store(store_id,name):
    conn = sqlite3.connect('store.db')
    cur = conn.cursor()
    insert_query = "INSERT INTO stores VALUES(?,?)"
    cur.execute(insert_query,(store_id,name))
    #insert_query2 = "INSERT INTO items VALUES(?,?,?)"
    #cur.execute(insert_query2,(prod_id,name,price))
    conn.commit()
    conn.close()

def insert_items(prod_id,name,price):
    conn = sqlite3.connect('store.db')
    cur = conn.cursor()
    insert_query = "INSERT INTO items VALUES(?,?,?)"
    cur.execute(insert_query,(prod_id,name,price))
    conn.commit()
    conn.close()

def select():
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    #select_query = "SELECT * FROM stores INNER JOIN items ON store_id = prod_id"
    select_query = "SELECT * FROM stores INNER JOIN items ON store_id = prod_id"
    cur.execute(select_query)
    result = cur.fetchall()
    conn.close()
    return result

#insert_items(1,'ab',100)
print(select())