import mysql.connector
from pywebio.input import *
from pywebio.output import put_text

conn = mysql.connector.connect(
    user = 'root',
    password = '',
    host = 'localhost',
    database = 'db_for_chat'
)

mycurs = conn.cursor()

def autorization():
    login = input("Enter your login: ", type=TEXT)
    password = input("Enter your password: ", type=PASSWORD)
    
if __name__ == '__main__':
    autorization()
conn.close()


