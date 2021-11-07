from logging import PlaceHolder
from os import close, name
import mysql.connector
from pywebio.input import *
from pywebio.output import close_popup, output, put_button, put_markdown, put_scrollable, put_table, put_text
from functools import partial
import asyncio

conn = mysql.connector.connect(
    user = 'root',
    password = '',
    host = 'localhost',
    database = 'db_for_chat'
)

mycurs = conn.cursor()
put_markdown("Login into your account to start messaging")
user_login = input_group("Login",
[
    input('Input your nickname', name='nickname', required=True),
    input('Input your password', name='password', required=True, type=PASSWORD)
])
put_button("Don't have an account", onclick=lambda: react())
name = user_login['nickname']
password = user_login['password']
mycurs.execute("SELECT login,password FROM user_db")
myresult = mycurs.fetchall()
for i in myresult:
    name_from_db = i[0]
    password_from_db = i[1]
    if name_from_db == name and password_from_db == password:
        print("Good")
    else:
        put_markdown("Your login or password is incorrect(if you don't have account,press upper button)")

    
    
def react():
    info = input_group("Register",[
        input('Input your nickname', name='nickname', validate=reg_check),
        input('Input your password', name='password', type=PASSWORD)
        ])

def reg_check(name):
    for i in mycurs.execute("SELECT * FROM user_db(id,login,password)"):
        if name == i:
            put_markdown("This name is already exists")
        else:
            put_markdown("All good")

# if __name__ == "__main__":
#     autorization()

conn.close()


