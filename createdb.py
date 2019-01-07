#!/usr/bin/python3

import cgi, cgitb 
import sys, os
from urllib.parse import unquote
import urllib.parse
import smtplib
import sqlite3
import datetime


print ("Content-type:text/html; charset=utf-8\r\n\r\n")



connection = sqlite3.connect('tasks.sqlite')
cursor = connection.cursor()
#name = "Vasia"
#dob = 1975
cursor.execute("CREATE TABLE tasks (id INTEGER PRIMARY KEY  NOT NULL,name TEXT NOT NULL,status TEXT NOT NULL )")
#cursor.execute("CREATE TABLE timing_data (athlete_id INTEGER NOT NULL,value TEXT NOT NULL,FOREIGN KEY (athlete_id) REFERENCES athletes)")
#cursor.execute("INSERT INTO athletes (name, dob) VALUES (?,?)", (name, dat))

#cursor.execute("SELECT id from athletes WHERE name=? AND dob=?", (name, dob))
#the_current_id = cursor.fetchall()
#print (the_current_id)

connection.commit()
connection.close()
