#!/usr/bin/env python3

# DATE_STR = "2 Oct 2020"
# VERSION = "1_i"
# AUTHOR = "Oliver Bonham-Carter"
# AUTHORMAIL = "obonhamcarter@allegheny.edu"

#########################################
# The database managing code begins here.
#########################################



import sqlite3


dbFilename_str = "myCampusDB.sqlite3" #establish the DB file
conn = sqlite3.connect(dbFilename_str) # open connection to the DB

print("\t _________________________________________________")
print("\n\t  Program to demo automatic INSERT statements using SQLite3") # add bright green to text then set it back to regular white.
print("\t -------------------------------------------------\n")

print("\t [+] Simple table creation")
myTable_str = "StudyMusic" #define the table
attribute1_str = "id INTEGER NOT NULL " # define first attribute statement
attribute2_str = "favSong VARCHAR" # define first attribute statement
attribute3_str = "BandName VARCHAR" # define first attribute statement



# Create the table creation string
myCreation_str = f"CREATE TABLE {myTable_str} ({attribute1_str}, {attribute2_str}, {attribute3_str})"


try:
	print(f"\t my insert: {myCreation_str}")

	# pass the table building string to sqlite3 library
	conn.execute(myCreation_str)

	# Save (i.e., commit) the changes
	conn.commit()

except sqlite3.OperationalError: # does the table already exist? If so, ignore creation statement
	print("\t [-] Note: The table already exists.")


## Check the new table
myQuery_str = f"SELECT * FROM {myTable_str}"



# Insert a row of data

myTable_str = "StudyMusic" # define the table
attrID_str = "10"
attrSONG_str = "La Vie est Belle"
attrARTIST_str = "MC Solaar"

print(f"\t [+] Simple INSERT into Table {myTable_str}")


# define the insert statement

myInsert_str = f"INSERT INTO {myTable_str} VALUES ({attrID_str}, \"{attrSONG_str}\", \"{attrARTIST_str}\")"

print(f"\t [+] my insert statement {myInsert_str}")


# pass the INSERT string to sqlite3 library
conn.execute(myInsert_str)

# Save (i.e., commit) the changes
conn.commit()



# do a simple query to check that insert worked
myQuery_str = f"SELECT * FROM {myTable_str}"
result = conn.execute(myQuery_str) # run the query
tables = result.fetchall() # collect query for processing
print("\t "+myQuery_str)
print("\t [+] Results: ")
for i in tables:
	print(f"\t  {i}") # show results of query





conn.close() # close the database connection
