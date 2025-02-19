import pymysql

def connect_db():
    try:
        connection = pymysql.Connect(host='localhost', port=34306, user='root', password='abcd1234', database='persons')
        print('Database Connected')
        return connection
    except:
        print("Connection failed")  

def disconnect_db(connection):
    connection.close()
    print('Database Disconnected')

def create_db():
    connection = connect_db()
    query = 'create database IF NOT EXISTS students;'
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    disconnect_db(connection)

def create_db():
    connection = connect_db()
    query = ''''create table IF NOT EXISTS stud(id INT, name VARCHAR(50), sem INT, gpa DECIMAL(3,2), gender CHAR check(gender IN ('M','F')));'''
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    disconnect_db(connection)

# def insert_row():
    

create_db()
insert_row()
# if connection:
#     disconnect_db(connection)
