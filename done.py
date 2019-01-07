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
print ("<input name='done' size='20' maxlength='2' placeholder='task id' />")
print ("<input type='submit' class='btn btn-default' value='Submit' />")


print ("</form>")


form = cgi.FieldStorage()

done_task  = form.getvalue('done')
done_task = str(done_task)
#f = open("restore-credentials.txt", "w")
#f.write(new_task)
#f.close()
#status = "new"



connection = sqlite3.connect('tasks.sqlite')
cursor = connection.cursor()

#cursor.execute("SELECT id FROM tasks WHERE name = '' LIMIT 1")
#idn = cursor.fetchone()

if done_task != None and done_task != "None":
    idn = done_task[0]
#    print (idn)

    if done_task != None and done_task != "None":
        cursor.execute("UPDATE tasks SET status ='done' WHERE id = ?", (idn))

    connection.commit()
    connection.close()



