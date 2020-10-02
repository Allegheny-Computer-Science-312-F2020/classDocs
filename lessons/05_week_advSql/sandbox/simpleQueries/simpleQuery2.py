#!/usr/bin/env python3


# DATE_STR = "2 Oct 2020"
# VERSION = "1_i"
# AUTHOR = "Oliver Bonham-Carter"
# AUTHORMAIL = "obonhamcarter@allegheny.edu"
# colour codes

# Define Colours for printing
BIBlack='\033[1;90m'      # Black
BIBlue='\033[1;94m'       # Blue
BICyan='\033[1;96m'       # Cyan
BIWhite='\033[1;97m'      # White
BIRed='\033[1;91m'        # Red
BIGreen='\033[1;92m'      # Green
BIYellow='\033[1;93m'     # Yellow
BIPurple='\033[1;95m'     # Purple
BWhite='\033[1;37m'       # White
White='\033[0;37m'        # White


#########################################
# The database managing code begins here.
#########################################


import sqlite3
print("\t _________________________________________________")
print(BIGreen +"\n\t  Program to demo automatic queries using SQLite3"+White) # add bright green to text then set it back to regular white.
print("\t -------------------------------------------------\n")


dbFilename_str = "myCampusDB.sqlite3" #establish the DB file
print(BICyan + f"\t [+] My Database is: {dbFilename_str}" + White)

print(BICyan + "\t [+] Opening the connection to the database..." + White)
conn = sqlite3.connect(dbFilename_str) # open connection to the DB
print(BICyan + f"\t [+] Connection established to {dbFilename_str} " + White)

### first query

myTable_str = "Course"
print(BIGreen + f"\n\n\t Running query in table : \"{myTable_str}\"" +White)

myQuery_str = f"SELECT * FROM {myTable_str};"
result = conn.execute(myQuery_str) # run the query
tables = result.fetchall() # collect query for processing
print(BICyan + "\t "+myQuery_str + White)
print(BIPurple +"\t [+] Results: "+White)
for i in tables:
	print(BIYellow + f"\t  {i}" + White) # show results of query



### next query
myTable_str = "Instructor"
attribute1_str = "name"
attribute2_str = "deptName"
print(BIGreen + f"\n\n\t Running query in table : \"{myTable_str}\"" +White)

myQuery_str = f"SELECT {attribute1_str},{attribute2_str} FROM {myTable_str};"
result = conn.execute(myQuery_str) # run the query
tables = result.fetchall() # collect query for processing
print(BICyan + "\t "+myQuery_str + White)
print(BIPurple +"\t [+] Results: "+White)
for i in tables:
	print(BIYellow + f"\t  {i}" + White) # show results of query

### next query
myTable_str = "Instructor"
attribute1_str = "name"
attribute2_str = "deptName"
attribute3_str = "salary"

print(BIGreen + f"\n\n\t Running query in table : \"{myTable_str}\"" +White)

myQuery_str = f"SELECT {attribute1_str},{attribute2_str}, {attribute3_str} FROM {myTable_str} WHERE {attribute3_str} > 99000;"
result = conn.execute(myQuery_str) # run the query
tables = result.fetchall() # collect query for processing
print(BICyan + "\t "+myQuery_str + White)
print(BIPurple +"\t [+] Results: "+White)
for i in tables:
	print(BIYellow + f"\t  {i}" + White) # show results of query
print("\n")

conn.close() # close the database connection
