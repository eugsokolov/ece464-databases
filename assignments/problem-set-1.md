# Problem Set 1 Description

### Part 1
Download the dataset and schema of sailors and boats from our in class discussion. Write SQL queries to answer the following questions. Include your query (and its output from your terminal in a presentable fashion) in your submissions.

1. List, for every boat, the number of times it has been reserved, excluding those boats that have never been reserved (list the id and the name).
2. List those sailors who have reserved every red boat (list the id and the name).
3. List those sailors who have reserved only red boats.
4. For which boat are there the most reservations?
5. Select all sailors who have never reserved a red boat.
6. Find the average age of sailors with a rating of 10.
7. For each rating, find the name and id of the youngest sailor.
8. Select, for each boat, the sailor who made the highest number of reservations for that boat.

### Part 2
Represent the sailors and boats schema using an ORM - I prefer SQLAlchemy but students have the freedom to choose their own language and ORM. Show that it is fully functional by writing tests with a testing framework using the data from part 1 (writing the queries for the questions in Part 1) - I prefer pytest but students are have the freedom to choose their own testing framework.

### Part 3
Students are hired as software consults for a small business boat rental that is experiencing a heavy influx of tourism in its area. This increase is hindering operations of the mom/pop shop that uses paper/pen for most tasks. Students should explore “inefficient processes” the business may have and propose ideas for improvements - in the form of a brief write-up.
Expand the codebase from part 2 to include a few jobs, reports, integrity checks, and/or other processes that would be beneficial to the business. Use the data provided in part 1 and expand it to conduct tests and show functionality. Examples include, but are not limited to:
* Bi weekly payment query
* Monthly accounting manager
* Daily inventory control
* Inventory repair tracker (and cost analysis)
