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


dbFilename_str = "myCampusDB.sqlite3" #establish the DB file
conn = sqlite3.connect(dbFilename_str) # open connection to the DB

print("\t _________________________________________________")
print("\n\t BIGreen + Program to demo automatic INSERT statements using SQLite3" + White) # add bright green to text then set it back to regular white.
print("\t -------------------------------------------------\n")

print(BICyan + "\t [+] Simple table creation" + White)
myTable_str = "StudyMusic" #define the table
attribute1_str = "id INTEGER NOT NULL " # define first attribute statement
attribute2_str = "favSong VARCHAR" # define first attribute statement
attribute3_str = "BandName VARCHAR" # define first attribute statement



# Create the table creation string
myCreation_str = f"CREATE TABLE {myTable_str} ({attribute1_str}, {attribute2_str}, {attribute3_str})"


try:
	print(BIGreen + f"\t [+] My insert statement:\n\t" + BICyan + f" {myCreation_str}" + White)

	# pass the table building string to sqlite3 library
	conn.execute(myCreation_str)

	# Save (i.e., commit) the changes
	conn.commit()

except sqlite3.OperationalError: # does the table already exist? If so, ignore creation statement
	print(BIPurple + "\t [-] Note: The table already exists."+ White)


## Check the new table
myQuery_str = f"SELECT * FROM {myTable_str}"



# Insert a row of data

myTable_str = "StudyMusic" # define the table
attrID_str = "10"
attrSONG_str = "La Vie est Belle"
attrARTIST_str = "MC Solaar"



# define the insert statement

myInsert_str = f"INSERT INTO {myTable_str} VALUES ({attrID_str}, \"{attrSONG_str}\", \"{attrARTIST_str}\")"

print(BIGreen + f"\n\t [+] My insert statement:" + BICyan + f"\n\t {myInsert_str}" + White)


# pass the INSERT string to sqlite3 library
conn.execute(myInsert_str)

# Save (i.e., commit) the changes
conn.commit()



# do a simple query to check that insert worked
myQuery_str = f"SELECT * FROM {myTable_str}"
result = conn.execute(myQuery_str) # run the query
tables = result.fetchall() # collect query for processing
print(BIGreen + f"\n\t [+] My query statement:" + BICyan + f"\n\t {myQuery_str}" + White)

print(BIPurple + "\t [+] Results: " + White)
for i in tables:
	print(BIYellow + f"\t  {i}" + White) # show results of query





conn.close() # close the database connection
