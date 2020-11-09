### Practical 3
### Name:
TODO


#### Steps:
 - Get into your MongoBDB Docker container.
 - Inside the container, type `mongo` to start up the database.
 - type `use mydb` to get into the "mydb" database in Mongo
 - Copy and paste the entire contents of the file, syntheticData_small.json into the MongoDB. This will create a collection called `employee`. Your queries are to use this collection.

#### Answer the following.
Using the following code to craft your queries,
`db.employee.find({},{yourQueryHere})`, `db.employee.find({},{_id:0, yourQueryHere}).pretty()` or `db.employee.find({},{_id:0, yourQueryHere})`, please respond to the following.



 1. Give the query code to get the following output from the employee collection.


``` { "_id" : "5c89c73ea91e2b221611b950", "friends" : [ { "id" : 0, "name" : "Lucia Mclean" }, { "id" : 1, "name" : "Nadia Soto" }, { "id" : 2, "name" : "Mae Elliott" } ] }
{ "_id" : "5c89c73ec4863a49668b3784", "friends" : [ { "id" : 0, "name" : "Bryan Frederick" }, { "id" : 1, "name" : "Navarro Rutledge" }, { "id" : 2, "name" : "Jacklyn Eaton" } ] }
{ "_id" : "5c89c73ea080dbf02bd40f0e", "friends" : [ { "id" : 0, "name" : "Fox White" }, { "id" : 1, "name" : "Josefa Ortiz" }, { "id" : 2, "name" : "Jean Patterson" } ] }
{ "_id" : "5c89c73e5e7b4f23f0a32660", "friends" : [ { "id" : 0, "name" : "Stefanie Beasley" }, { "id" : 1, "name" : "Colon Abbott" }, { "id" : 2, "name" : "Charmaine Key" } ] }
```


TODO




2. Give the query code to get the following output from the employee collection.



```
{ "_id" : "5c89c73ea91e2b221611b950", "name" : { "first" : "Pennington", "last" : "Moss" }, "email" : "pennington.moss@radiantix.tv" }
{ "_id" : "5c89c73ec4863a49668b3784", "name" : { "first" : "Belinda", "last" : "Guzman" }, "email" : "belinda.guzman@beadzza.org" }
{ "_id" : "5c89c73ea080dbf02bd40f0e", "name" : { "first" : "Rosemary", "last" : "French" }, "email" : "rosemary.french@prosure.co.uk" }
{ "_id" : "5c89c73e5e7b4f23f0a32660", "name" : { "first" : "Cora", "last" : "Keith" }, "email" : "cora.keith@combogen.io" }
```

TODO




3. Give the query code to get the following output from the employee collection.


```
{ "greeting" : "Hello, Pennington! You have 5 unread messages." }
{ "greeting" : "Hello, Belinda! You have 10 unread messages." }
{ "greeting" : "Hello, Rosemary! You have 7 unread messages." }
{ "greeting" : "Hello, Cora! You have 7 unread messages." }

```

TODO




(Did you remember to add your name?)
