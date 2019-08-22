# Final Project Proposal

Each proposal must include:
* Group name, member names, and member emails.
* General description of the project, including its purpose, general functionality, types of users, etc.
* More detail on the interface with which each type of user (if there is more than one type of user) will be presented (views). You do not have to show the exact interface, which may not have been decided yet, but explain what type of information the user will be able to enter, what choices they will be presented with, etc.
* A textual description of the data that will be stored in the database. In other words, explain the meaning of the data.
* An ER diagram (or a collection of ER diagrams) depicting your database. This should not be handwritten. The images should be part 	of the submitted, single file. The diagrams should follow standard conventions to indicate entity sets, relationship sets, attributes, 	key constraints, participation constraints, primary keys, weak entities, etc. 
* An explanation of how you will populate the database.
* The schemas 	for your relations using the informal notation used by our textbook 	and in lectures.  For example:

```
Students(sid: string, name: string, login: string, age: integer, gpa: real)
```

You should underline members of the primary key of each relation, but other constraints will not be indicated when using this notation. Along with each schema, provide a textual description if there is anything that is not obvious.

The SQL 	commands that will be used to create the relations (a.k.a. tables). 	For example, the command to create the relation indicated above 	might be:

```
CREATE TABLE Students ( sid CHAR(20),
name CHAR(30),
login CHAR(20),
age INTEGER,
gpa REAL,
PRIMARY KEY (sid) )
```

Using these statements, include any constraints that are possible and appropriate, including candidate and primary key constraints, foreign key constraints, participation constraints, etc. You may use `NULL` values, default values, `CASCADE` clauses, etc. You may try out the commands with a DBMS if you wish, but I am only going to look at them by eye now. I am mostly interested in seeing that you are appropriately using constraints and making appropriate decisions (e.g., when do you create a relation corresponding to a relationship set in the ER diagram, and when do you combine the relationship set with an entity set). Again, you may include a textual description explaining anything that is not obvious.

You don't necessarily have to include the requested components of the proposal in the specified order. You may combine parts, if that makes sense, or feel free to include more than I ask for if you think it would be helpful. This assignment is meant to serve a dual purpose of giving you experience creating ER diagrams and familiarizing me with your plans so that I can give helpful feedback and suggestions. You will be allowed to make changes as the semester progresses, but your final project may be partially evaluated based on how well you implement your proposal.


