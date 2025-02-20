import pymysql

def connect_db():
    try:
        connection = pymysql.Connect(host='localhost', port=3306, user='root', password='abcd1234', database='persons', charset='utf8')
        print('DB connected')
        return connection
    except:
        print('DB connection failed')

def disconnect_db(connection):
    try:
        connection.close()
        print('DB dis-connected')
    except:
        print('Error while disconnecting DB')

connection = connect_db()
if connection:
    disconnect_db(connection)