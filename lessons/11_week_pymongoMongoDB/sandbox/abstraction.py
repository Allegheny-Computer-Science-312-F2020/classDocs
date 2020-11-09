#!/usr/bin/env python3

# Date 9 November 2020
# pymongo demo for python3

# Note: To find this file in your MongoDB container,
# this file is to be copied to the mongodata/src/ directory
# on your local machine.

from pymongo import MongoClient
import string



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


# creating connections for communicating with Mongo DB
client = MongoClient('localhost:27017')

db = client.AGENTS # the name of the database in mongo. this base may be found by the command, "show dbs" in mongo



def begin():
	""" Driver method for the program"""
	print(BIGreen +"\t The agents database for use with MongoDB."+White)
	print(BIGreen +"\t Uses the pymongo client"+White)
	print(BIGreen + "\t Welcome to the pyMongo automation program!\n")
	while(1):
	# choose an option to select a dataEmployee operation
		prmt = BIYellow + "\tSelect from the menu :" + White
		print(BICyan+"\t 0"+ White+" for DB information")
		print(BICyan+"\t 1"+ White+" to Insert")
		print(BICyan+"\t 2"+ White+" to Update")
		print(BICyan+"\t 3"+ White+" to Read DB")
		print(BICyan+"\t 4"+ White+" to Delete a document")
		print(BICyan+"\t q"+ White+" to Quit")
		selection = input(prmt)

		if selection == '0':
			info()
		elif selection == '1':
			insert()
		elif selection == '2':
			update()
		elif selection == '3':
			read()
		elif selection == '4':
			delete()
		elif selection.upper() == 'Q':
			print(BIRed + "\tExiting ... "+White)
			exit()
		else:
			print("\n INVALID SELECTION \n")
# end of begin()

def printIt(in_str, colour_str = BIGreen):
	"""Function to print up messages in colour."""
	print(colour_str + in_str + White)

def info():
# Function to get some information about the dataEmployee itself.
	printIt("\n\t Returns information about the collection.")

	try:
		result = db.Employee.db
		print(f"\n Info: {result}")

	except Exception as e:
		print(str(e))
# end of info()



def insert():
# Function to insert data into mongo db
	printIt("\n\t Inserts a document into the collection.")

	try:
		employeeId = input('Enter Employee id :')
		employeeFirstName = input('Enter FirstName :')
		employeeLastName = input('Enter LastName :')
		employeeAge = input('Enter age :')
		employeeCountry = input('Enter Country :')

# insert the data into the base
		db.Employee.insert_one(
		{
		"id": employeeId,
		"FirstName":employeeFirstName,
		"LastName":employeeLastName,
		"age":employeeAge,
		"country":employeeCountry
		})
		printIt("\n\t Inserted data successfully",BIYellow)

	except Exception as e:
		print(str(e))
# end of insert()



def update():
# Function to update record to mongo db
	printIt("\n\t Updates a document in the collection.")

	try:
		employeeId = input('  Enter Employee id :')
		employeeFirstName = input('  Enter FirstName :')
		employeeLastName = input('  Enter LastName :')
		employeeAge = input('  Enter age :')
		employeeCountry = input('  Enter Country :')


	# update the record with the new information
		db.Employee.update_one(
			{"id": employeeId},
			{
			"$set": {
			"firstName":employeeFirstName,
			"lastName":employeeLastName,
			"age":employeeAge,
			"country":employeeCountry
			}
			}
		)
		printIt("\n\t nRecords updated successfully.",BIYellow)

	except Exception as e:
		print(str(e))
# end of update()



def read():
# function to read records from mongo db
	printIt("\n\t Reads documents in the collection.")

	try:
		empCol = db.Employee.find()
		print("\n Found: all data from DataEmployee \n")
		for emp in empCol:
			print(emp)
	except Exception as e:
		print(str(e))
# end of read()



# Function to delete record from mongo db
def delete():
	printIt("\n\t Deletes a document in the collection.")
	print(BIRed + "\t This will destroy a document! " + White)


	try:
		employeeId = input('\nEnter employee id to delete. ')
		db.Employee.delete_many({"id":employeeId})
		print("\nDeletion successful\n")
	except Exception as e:
		print(str(e))
#end of deltete()


begin() # start up the program: call the main function to begin
