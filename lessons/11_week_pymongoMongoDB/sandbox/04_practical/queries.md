### Practical 4
### Name:
TODO


#### Steps:
 - Get into your MongoBDB Docker container.
 - Inside the container, type `mongo` to start up the database.
 - type `use mydb` to get into the "mydb" database in Mongo
 - Copy and paste the entire contents of the file, `syntheticData_small.json` into the MongoDB interactive terminal. This will create a collection called `employee`. Your queries are to use this collection.

#### Answer the following.
Using the following code to craft your queries,
`db.employee.find({},{yourQueryHere})`, `db.employee.find({},{_id:0, yourQueryHere}).pretty()` or `db.employee.find({},{_id:0, yourQueryHere})`, please respond to the following.


1. In terms of documents that are returned, explain the difference between the following queries in MongoDB.

db.employee.find({"name.last":"Moss"})
db.employee.find({"name.last":"Moss"},{"name.last":1})

SOLUTION:
```
TODO
```


 2. Give the query code to get the following output from the employee collection.
 ```
 { "_id" : "5c89c73ea91e2b221611b950", "favoriteFruit" : "apple" }
 { "_id" : "5c89c73ec4863a49668b3784", "favoriteFruit" : "strawberry" }
 { "_id" : "5c89c73ea080dbf02bd40f0e", "favoriteFruit" : "strawberry" }
 { "_id" : "5c89c73e5e7b4f23f0a32660", "favoriteFruit" : "apple" }
```

SOLUTION:
```
TODO
```



3. Give the query code to get the following output from the employee collection.
```
{ "name" : { "first" : "Pennington", "last" : "Moss" }, "favoriteFruit" : "apple" }
{ "name" : { "first" : "Belinda", "last" : "Guzman" }, "favoriteFruit" : "strawberry" }
{ "name" : { "first" : "Rosemary", "last" : "French" }, "favoriteFruit" : "strawberry" }
{ "name" : { "first" : "Cora", "last" : "Keith" }, "favoriteFruit" : "apple" }
```

SOLUTION:
```
TODO
```



4. Give the query code to get the following output from the employee collection.


```
{ "name" : { "first" : "Cora", "last" : "Keith" }, "favoriteFruit" : "apple" }
```
SOLUTION:
```
TODO
```



5. Give the query code to get the following output from the employee collection.

```
{ "age" : 33, "name" : { "first" : "Pennington", "last" : "Moss" } }
{ "age" : 27, "name" : { "first" : "Belinda", "last" : "Guzman" } }
{ "age" : 31, "name" : { "first" : "Rosemary", "last" : "French" } }
{ "age" : 23, "name" : { "first" : "Cora", "last" : "Keith" } }
```

SOLUTION:
```
TODO
```

6. Give the query code to get the following output from the employee collection.
```
{ "_id" : "5c89c73ea91e2b221611b950", "age" : 33, "name" : { "first" : "Pennington" } }
{ "_id" : "5c89c73ec4863a49668b3784", "age" : 27, "name" : { "first" : "Belinda" } }
{ "_id" : "5c89c73ea080dbf02bd40f0e", "age" : 31, "name" : { "first" : "Rosemary" } }
```

SOLUTION:
```
TODO
```

7. After a birthday, write the code to change the `age` of `Pennington Moss` from 33 to 34.

SOLUTION:
```
TODO
```


(Did you remember to add your name?)
