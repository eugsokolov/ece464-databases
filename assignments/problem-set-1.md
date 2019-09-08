# Problem Set 1 Description

### Part 1
Download the dataset and schema of sailors and boats from our in class discussion. Write SQL queries to answer the following questions. Include your query (and its output from your terminal) in your submissions.

1. Select, for each boat, the sailor who made the highest number of reservations for that boat.
2. List, for every boat, the number of times it has been reserved, excluding those boats that have never been reserved (list the id and the name).
3. List those sailors who have reserved every red boat (list the id and the name).
4. List those sailors who have reserved only red boats.
5. For which boat are there the most reservations?
6. Select all sailors who have never reserved a red boat.
7. Find the average age of sailors with a rating of 10.

### Part 2
Represent the sailors and boats schema using an ORM - I prefer SQLAlchemy but students have the freedom to choose their own language and ORM. Show that it is fully functional by writing tests using the data from part 1 - I prefer pytest but students are have the freedom to choose their own testing framework.

### Part 3
Students are hired as software consults for a small business boat rental that is experiencing a heavy influx of tourism in its area. This increase is hindering operations of the mom/pop shop that uses paper/pen for most tasks. Students should explore “inefficient processes” the business may have and propose ideas for improvements - in the form of a brief write-up.
Expand the codebase from part 2 to include a few jobs, reports, integrity checks, and/or other processes that would be beneficial to the business. Use the data provided in part 1 and expand it to conduct tests and show functionality. Examples include, but are not limited to:
* Bi weekly payment query
* Monthly accounting manager
* Daily inventory control
* Inventory repair tracker (and cost analysis)

#### “Extra Credit”
Use a web code review platform so I can write comments for review. I should get a link to a review platform and be able to easily write comments - perhaps after linking with github or creating a free account. Ones that I have found good are codacy.com and reviewable.io. This will help prepare you for the final project and is highly recommended. 