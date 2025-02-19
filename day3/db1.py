import pymysql
def connect_db():
    try:
        connection = pymysql.Connect(host='localhost', port=3306, user='root', password='abcd1234', database='persons')
        print('Database Connected')
    except:
        print("Connection failed")
    return connection

def disconnect_db(connection):
    connection.close()
    print('Database Disconnected')

connection=connect_db()
disconnect_db(connection)
