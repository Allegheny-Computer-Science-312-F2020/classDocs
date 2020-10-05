### What is this?
Practical 2

### Date
28 Sept 2020

### Database:
myCampusDB.sqlite3

### GitHub Classroom Repository Link:
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
	- select * from Department where courseId like "3%";
	- Correct output:
		* 300h|Hst|History
		* 300p|Phl|Philosophy


2. Give all records from the **Department** table where the CourseID begins with 2.
	- select * from Department where courseId like "2%";
	- Correct output:
		* 201cb|CmpBio|CompBio
		* 200e|Eng|ENG
		* 200f|FR|FRCH


3. Give all records from the **Department** table where the CourseID contains the last three characters are "00p".
	- select * from Department where courseId like "_00p" ;
	- Correct output:
		* 300p|Phl|Philosophy

4. Give all records from the **Instructor** table where a name contains a subsequence "ille"
	-	select * from Instructor where name like "%ille%";
	-	Correct output:
		* 10101|Miller|S1|CompSci|90000

5. Give all records from the **Instructor** table where the salaries are less than 100000 and the results are grouped by deptName.
	- select * from Instructor GROUP BY deptName HAVING salary < 100000;
	- Correct output:
		* 10107|Chesterfield|S3|CompBio|97000
		* 10101|Miller|S1|CompSci|90000
		* 10105|Mauler|S3|Math|99000

6. Give the average salaries of all salary information in the **Instructor** table.
 	- select AVG(salary) from Instructor;
	- Correct output:
		* 95000.0

7. Give the name and salary records from the **Instructor** table where the salaries fall between 90000 and 100000.
	- select name, salary from Instructor where salary <= 100000 and salary >= 90000;
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
	- select deptName from Department INTERSECT select deptName from Instructor;
	- Correct output:
		* CompBio
		* CompSci
		* Math

9. Give the UNION of _deptNames_ which have been taken from the **Department** and **Instructor** tables.
	- select deptName from Department UNION select deptName from Course;
	- Correct output:
		* CompBio
		* CompSci
		* ENG
		* FRCH
		* History
		* Math
		* Philosophy
