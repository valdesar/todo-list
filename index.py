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
print('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">')
print('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>')
print("<style>body {padding-left:5%; background-color: lightyellow }</style>")
print ("<br><br>")
print ("<a class='btn btn-info' href='new.py'>New task</a>&nbsp&nbsp&nbsp&nbsp<a class='btn btn-info' href='remove.py'>Remove task</a>&nbsp&nbsp&nbsp&nbsp<a class='btn btn-info' href='insert.py'>Insert task</a>&nbsp&nbsp&nbsp&nbsp<a class='btn btn-success' href='done.py'>Mark as done by ID</a>")
print ("<br><br>")



connection = sqlite3.connect('tasks.sqlite')
cursor = connection.cursor()

#status = "new"
#cursor.execute("SELECT status from tasks WHERE id= " + number_of_tasks_string + " ")
#status = cursor.fetchone()



number_of_tasks = cursor.execute("select max(id)+1 from tasks")

number_of_tasks = cursor.fetchall()
number_of_tasks = number_of_tasks[0][0]
try:

    number_of_tasks = int(number_of_tasks)
    number_of_tasks_string = str(number_of_tasks)

    for x in range (0, number_of_tasks):
        number_of_tasks_string = str(x)
        if len(number_of_tasks_string) == 2:
            cursor.execute("SELECT id,name from tasks WHERE id= " + number_of_tasks_string + " ")
            the_current_id = cursor.fetchone()

            cursor.execute("SELECT status from tasks WHERE id= " + number_of_tasks_string + " ")
            status = cursor.fetchone()
            if the_current_id != "None" and the_current_id != None :
                if status[0] == 'new':
                    print ("<div style='background-color: #FFE0C0; width:70%; padding:1%;'>")
                else:
                    print ("<div style='background-color: palegreen; width:70%; padding:1%;'>")
                part1 = the_current_id[0]
                print (")    ")
                part2 = the_current_id[1]

                print (part1)
                print (part2)

                print ("</div><br><br>")
        else:
            cursor.execute("SELECT id,name from tasks WHERE id=?", (number_of_tasks_string))
            the_current_id = cursor.fetchone()

            cursor.execute("SELECT status from tasks WHERE id= " + number_of_tasks_string + " ")
            status = cursor.fetchone()

            if the_current_id != "None" and the_current_id != None :
                if status[0] == 'new':
#                    print ("new1")
                    print ("<div style='background-color: #FFE0C0; width:70%; padding:1%;'>")
                else:
                    print ("<div style='background-color: palegreen; width:70%; padding:1%;'>")
                print (the_current_id[0])
                print (")    ")
                print (the_current_id[1])
            print ("</div><br><br>")

    connection.commit()
    connection.close()
except:
    print ("No task yet, start from scratch")


