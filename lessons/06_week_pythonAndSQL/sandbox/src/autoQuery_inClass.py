#!/usr/bin/env python3



# import sqlite3 library
import sqlite3

# open the database connection
dbFilename_str = "myCampusDB.sqlite3"
print(f"\t [+] The database is :{dbFilename_str}")


conn = sqlite3.connect(dbFilename_str)
print(f"\t [+] The database is open ")


# show me the tables of the database
myQuery_str = "SELECT name FROM sqlite_master WHERE type = 'table';"


def runQuery(conn, myQuery_str):
	"""DocString: What is this function? A function to perform my queries automatically."""
	result = conn.execute(myQuery_str)
	return(result.fetchall())
	#end of runQuery()

def parseResults(inResults_list):
	for i in inResults_list:
			print(f" {i}")
	#end of parseResults()

results_list = runQuery(conn, myQuery_str)
print(f" [+] My output is {results_list} and is of type {type(results_list)}")
parseResults(results_list)

tmp_list = [] # create a temp list
for i in range(len(results_list)):
#	print(f"{i}, {s[i][0]}, {type(s[i][0])}")
	tmp_list.append(results_list[i][0])
	print(f"\t [+] my tmp_list: {tmp_list}")

### query all tables in the database, names are in tmp_list

for i in tmp_list:
	print(f"\t [+] Current table: {i} ")
	myQuery_str = f"SELECT * FROM {i}"
	results = runQuery(conn, myQuery_str)
	parseResults(results)
	print("\n") # drop a line
