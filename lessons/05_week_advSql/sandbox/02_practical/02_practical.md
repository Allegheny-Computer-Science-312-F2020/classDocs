### Name
TODO

### What is this?
Practical 2

### Date
28 Sept 2020

### Using database:
myCampusDB.sqlite3

### GitHub Classroom Repository Link for practical work:
	- https://classroom.github.com/a/3FKw8tMD


### Instructions
	- Create a directory in your GitHub called `02_practical/`
	- Copy this file into this directory for working and to save your work.
	- Once you have completed the below queries, use the following three GitHub commands.
		* git add − A
		* git commit − m "Your commit caption here"
		* git push

### Due Date:		
	- Your check-marked assignment is due by Sept 30, 2020, 12:00 EDT


1. Give all records from the **Department** table where the CourseID begins with 3.
	- TODO: Add query here
	- Correct output:
		* 300h|Hst|History
		* 300p|Phl|Philosophy


2. Give all records from the **Department** table where the CourseID begins with 2.
	- TODO: Add query here
	- Correct output:
		* 201cb|CmpBio|CompBio
		* 200e|Eng|ENG
		* 200f|FR|FRCH


3. Give all records from the **Department** table where the CourseID contains the last three characters are "00p".
	- TODO: Add query here
	- Correct output:
		* 300p|Phl|Philosophy

4. Give all records from the **Instructor** table where a name contains a subsequence "ille"
	- TODO: Add query here
	-	Correct output:
		* 10101|Miller|S1|CompSci|90000

5. Give all records from the **Instructor** table where the salaries are less than 100000 and the results are grouped by deptName.
	- TODO: Add query here
	- Correct output:
		* 10107|Chesterfield|S3|CompBio|97000
		* 10101|Miller|S1|CompSci|90000
		* 10105|Mauler|S3|Math|99000

6. Give the average salaries of all salary information in the **Instructor** table.
	- TODO: Add query here
	- Correct output:
		* 95000.0

7. Give the name and salary records from the **Instructor** table where the salaries fall between 90000 and 100000.
	- TODO: Add query here
	- Correct output:
		* Miller|90000
		* Johnson|90000
		* Thompson|100000
		* Mauler|99000
		* Jackson|98000
		* Chesterfield|97000
		* William|99000
		* Watson|98000
		* Nelson|97000

8. Give the INTERSECT of _deptNames_ which have been taken from the **Department** and **Instructor** tables.
	- TODO: Add query here
	- Correct output:
		* CompBio
		* CompSci
		* Math

9. Give the UNION of _deptNames_ which have been taken from the **Department** and **Instructor** tables.
	- TODO: Add query here
	- Correct output:
		* CompBio
		* CompSci
		* ENG
		* FRCH
		* History
		* Math
		* Philosophy

	(Did you remember to add your name?)
