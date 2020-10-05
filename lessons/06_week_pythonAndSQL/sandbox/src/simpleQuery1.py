#!/usr/bin/env python3

# DATE_STR = "2 Oct 2020"
# VERSION = "1_i"
# AUTHOR = "Oliver Bonham-Carter"
# AUTHORMAIL = "obonhamcarter@allegheny.edu"

import sqlite3

dbFilename_str = "myCampusDB.sqlite3" #establish the DB file
conn = sqlite3.connect(dbFilename_str) # open connection to the DB

myTable_str = "Instructor"
attribute1_str = "name"
attribute2_str = "deptName"
attribute3_str = "salary"

print(f"\n\n\t Running query in table : \"{myTable_str}\"")

myQuery_str = f"SELECT {attribute1_str},{attribute2_str}, {attribute3_str} FROM {myTable_str} WHERE {attribute3_str} > 99000;"
result = conn.execute(myQuery_str) # run the query
tables = result.fetchall() # collect query for processing
print("\t "+myQuery_str)
print("\t [+] Results: ")
for i in tables:
	print(f"\t  {i}") # show results of query

conn.close() # close the database connection
