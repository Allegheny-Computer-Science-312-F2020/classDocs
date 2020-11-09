

from pymongo import MongoClient
import string


def read():
	""" function to read records from mongo db """
	try:
		empCol = db.Employee.find()
		print("\n Found: all data from DataEmployee \n")
		for emp in empCol:
			print(f"\t [+] {emp}")
	except Exception as e:
		print(str(e))
# end of read()



def insert():
	""" Function to insert data into mongo db """
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
		print("\nInserted data successfully\n")

	except Exception as e:
		print(str(e))
# end of insert()



def update():
	""" Function to update record to mongo db """
	print("  Update:")
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
		})
		print("\nRecords updated successfully. \n")
	except Exception as e:
		print(str(e))
# end of update()



# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.mongodemo

print("\t [+] Data BEFORE addition")
read()

insert()

print("\t [+] Data AFTER addition")
read()
