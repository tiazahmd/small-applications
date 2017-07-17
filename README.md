# Simple Registration & Login Module
###### Version 1.0

#### Features:
1. New user registration
2. Basic user Login
3. Updating user password
4. Uses database(SQLite3) to store information

#### Registration Logic:
1. User provides full name, username and password
  1. The password is checked against each other to check if they match
2. A function generates a unique id (primary key) for this new user
  1. Selects the last row from the table
  2. Selects the ID from that table
  3. Adds 1 to the id to make a new consistent unique id and then returns the new id
3. The information (name, username, password, unique id) is stored in a list
5. The list is passed to DB and the table gets updated

#### Login Module Logic:
1. Program gets username and password from the username and passes to a Function
  1. Function calls the db table
  2. Loops through the rows
  3. If, in a row, both the username and password match, return True
2. If the function returns true, login is accepted

#### Update Password Module:
1. Program gets username and old password from user
  1. Program sends the information to a function to check if the existing username
     and password match
     1. The function loops through the database and finds the username and password.
        Similar logic to Login Module.
     2. If the username and password matches:
        1. Takes the ID of that row
        2. Takes the boolean value true
        3. Combines ID and boolean value in a list and returns the list
  2. Now the username and password match and we have a the row id where new password
     will go
2. Program asks for the new password from the user
3. Program updates the new password
  1. Goes to the exact row with the ID
  2. Updates the password field with the new password
