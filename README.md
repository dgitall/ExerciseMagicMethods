# ExerciseMagicMethods
 
## Introduction
In this exercise, we will have you use Python's magic methods to help work with data from an astronaut CSV.

1. Download the astronaut data from https://www.kaggle.com/nasa/astronaut-yearbook?select=astronauts.csv
2. Follow the parts below.
## Exercise
### Part I: Create an Astronaut Model
Review the Astronaut data and create a model for each astronaut object. Note: Some cells have more than one data element inside the cell.

### Part II: Create an Astronaut Object
Code the model you created in Part 1.

Add the additional magic methods as follows:

* Create a constructor for the Object

* Name, Flight (hr), and Status as required parts of an Astronaut and all other fields from the CSV as optional.

* Create gt, ge, eq magic methods based on the Flight (hr) column in the spreadsheet for comparisons.

  For example, A Joseph M. Acaba object > Loren W. Acton object if compared with >, =>, or =.

* Create a str magic method that will use a combination of Name from the CSV, a comma, and their status from the CSV file.

  For example: "Joseph M. Acaba, Active"

### Part III: Create a List of Astronaut Objects
Read in all of the data from the astronauts.csv file using the csv module or your preferred File I/O methods. As you are reading in each astronaut, create an Astronaut object with your constructor and store this in a List.

List all the mutable properties for the first astronaut object.

Pick two random Astronaut objects and compare them based on Flight(hrs). Do not compare their Flight(hrs) values directly. Compare the objects, and trust that your implementations of __gt__, __ge__, and __eq__ will work appropriately.

Print out all astronauts from the astronaut list. Assume you cannot access any attributes for this printout.