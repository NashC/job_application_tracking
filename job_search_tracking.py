#job_search_tracking

import datetime as dt
import psycopg2
import pandas as pd


def basic():
	print "Company:"
	company = raw_input()
	print "Job Title:"
	job_title = raw_input()
	print "Job Posting URL:"
	job_url = raw_input()
	print "Date Applied (mm/dd/yyyy):"
	date = [ int(x) for x in raw_input().split('/') ]
	date_applied = dt.date(date[2], date[0], date[1])
	return company, job_title, job_url, date_applied


dbname = 'test1'
user = 'nashc'
try:
    #conn = psycopg2.connect(dbname='test1', user='nashc')
    conn = psycopg2.connect(dbname=dbname, user=user)
    print "Connected to database successfully"
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
company, job_title, job_url, date_applied = basic()

cur.execute("INSERT INTO jobs1 (company, role, url, date_applied) \
	VALUES (%s, %s, %s, %s)", (company, job_title, job_url, date_applied))

conn.commit()
print "Records created successfully"
conn.close()

