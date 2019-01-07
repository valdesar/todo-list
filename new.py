#!/usr/bin/python3

import cgi, cgitb 
import sys, os
from urllib.parse import unquote
import urllib.parse
import smtplib
import sqlite3
import datetime
import cgitb 

cgitb.enable()


print ("Content-type:text/html; charset=utf-8\r\n\r\n")
print ("<br><br>")
print('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">')
print('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>')
print("<style>body {padding-left:5%;background-color: lightyellow; }</style>")



print ("<a class='btn btn-info' href='index.py'>Task list</a>")
print("<br><br>")
print ("<form method ='post'>")
print ("<input  name='newtask' size='60' placeholder='Enter new task' />")
print ("<input type='submit' class='btn btn-default' value='Submit' />")
print ("</form>")


form = cgi.FieldStorage()

new_task  = form.getvalue('newtask')
new_task = str(new_task)
#new_task = new_task.encode('utf-8')
#f = open("restore-credentials.txt", "w")
#f.write(new_task)
#f.close()
status = "new"



connection = sqlite3.connect('tasks.sqlite')
cursor = connection.cursor()
if new_task != None and new_task != "None":
    cursor.execute("INSERT INTO tasks (name, status) VALUES (?,?)", (new_task, status))

connection.commit()
connection.close()



