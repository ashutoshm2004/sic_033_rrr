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

connection=connect_db()
disconnect_db(connection)
