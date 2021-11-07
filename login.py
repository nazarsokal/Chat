from logging import PlaceHolder
from os import close, name
from typing import Text
import mysql.connector
from pywebio.input import *
from pywebio.output import close_popup, output, put_button, put_markdown, put_scrollable, put_table, put_text
from functools import partial
import asyncio
import socket

ip_addres = socket.gethostbyname(socket.gethostname())

conn = mysql.connector.connect(
    user = 'root',
    password = '',
    host = 'localhost',
    database = 'db_for_chat'
)
mycurs = conn.cursor()

def reaction(value):
    pass

mycurs.execute("SELECT * FROM user_db WHERE ip = %s",(ip_addres,))
myresult = mycurs.fetchall()
for i in myresult:
    name_from_db = i[1]
    password_from_db = i[2]
    ip_from_db = i[3]
    isLoged_from_db = i[4]
    if ip_addres == ip_from_db and isLoged_from_db == 'Staying loged in':
        user_login_isLoged = input_group("Login",
        [
            input('Input your nickname', name='nickname', value=name_from_db, required=True, action=('Register', reaction)),
            input('Input your password', name='password', value=password_from_db, type=PASSWORD, required=True),
            checkbox(' ', name='isLoged', options=['Staying loged in'], value='Staying loged in')
        ])
        nickname_is_LogedIn = user_login_isLoged['nickname']
        password_is_LogedIn = user_login_isLoged['password']
        checkbox_is_LogedIn = user_login_isLoged['isLoged']
        try:
            if nickname_is_LogedIn == name_from_db and password_is_LogedIn == password_from_db and checkbox_is_LogedIn[0] == isLoged_from_db:
                print("All good")
            else:
                put_markdown("Your login or password is incorrect(if you don't have account,press upper button)")
        except Exception as e:
            if nickname_is_LogedIn == name_from_db and password_is_LogedIn == password_from_db and repr(e) == "IndexError('list index out of range')": 
                mycurs.execute("UPDATE user_db SET is_loged = 'No' WHERE ip = %s",(ip_addres,))
                conn.commit()
            #put_markdown("%s %s %s" % (nickname_is_LogedIn,password_is_LogedIn,checkbox_is_LogedIn[0])) 
    else:
        user_login = input_group("Login",
        [
            input('Input your nickname', name='nickname', required=True, action=('Register', reaction)),
            input('Input your password', name='password', type=PASSWORD, required=True),
            checkbox(' ', name='isLoged', options=['Staying loged in'])
        ])
        nickname = user_login['nickname']
        password = user_login['password']
        checkbx = user_login['isLoged']
        try:
            if nickname == name_from_db and password == password_from_db:
                if checkbx[0] != isLoged_from_db:
                    print("All good")
                    if checkbx[0] == 'Staying loged in':
                        mycurs.execute("UPDATE user_db SET is_loged = 'Staying loged in' WHERE ip = %s",(ip_addres,))
                        conn.commit()    
            else:
                put_markdown("Your login or password is incorrect(if you don't have account,press upper button)")
        except Exception as e:
            if nickname == name_from_db and password == password_from_db and repr(e) == "IndexError('list index out of range')": 
                mycurs.execute("UPDATE user_db SET is_loged = 'No' WHERE ip = %s",(ip_addres,))
                conn.commit() 

conn.close()


