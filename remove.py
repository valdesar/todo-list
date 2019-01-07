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
print("<style>body {padding-left:5%; background-color: lightyellow;}</style>")



print ("<a class='btn btn-info' href='index.py'>Task list</a>")
print("<br><br>")
print ("<form method ='post'>")
print ("<input name='remove' size='20' maxlength='2' placeholder='task id' />")
print ("<input type='submit' class='btn btn-default' value='Submit' />")
print ("</form>")


form = cgi.FieldStorage()

remove_task  = form.getvalue('remove')
remove_task = str(remove_task)



connection = sqlite3.connect('tasks.sqlite')
cursor = connection.cursor()
if len(remove_task) == 1:
    cursor.execute("UPDATE tasks SET name = '', status ='' WHERE id = ?", (remove_task))

if len(remove_task) == 2:
    cursor.execute("UPDATE tasks SET name = '', status ='' WHERE id = " +remove_task+"")

connection.commit()
connection.close()



