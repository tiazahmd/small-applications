import sqlite3
import sys
import datetime

choice = 0
password_1 = 0
password_2 = 1
password = None
conn = sqlite3.connect('users.db') # Creates connection with server

cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user_info(ID INT PRIMARY KEY, Name TEXT, Username TEXT, Password TEXT, Times TEXT)")
                                    # creates a cursor to navigate through databases

# Function for checking if username exists or not
def userval(rows, username):
    rowlen = len(rows)
    for i in range(0, rowlen):
        if (username == rows[i][2]): # Loops through database to see if username exists or not.
            return True #  If it does, returns true.
    return False

# Function to create a unique id to be used as a primary key.
def getid():
    cursor.execute('SELECT max(ID) FROM user_info') # Selects the last row from the table
    max_id = int(cursor.fetchone()[0]) # Selects the ID from that table
    new_id = max_id + 1 # Adds 1 to the id to make a new consistent unique id
    return new_id # Returns the new id.

# Function for logging in - user authentication
def uauth(rows, user, passwd):
    rowlen = len(rows)
    for i in range (0, rowlen): # Loops through the table rows
        if user == rows[i][2] and passwd == rows[i][3]: # If finds username and associated password
            return True # Returns true
    return False

# Function for changing password
def changepass(rows, user, passwd):
    rowlen = len(rows)
    cplist = [None, False] # Initiates a list with default values
    for i in range (0, rowlen):
        if user == rows[i][2] and passwd == rows[i][3]: # Loops through rows to find if provided user
                                                        # and password matches. If not, returns the
                                                        # list with False
            cpid = i # Extracts the id of that row
            cpstatus = True # Updates bool value to True suggesting the username pass match
            cplist[0] = cpid # updates list with new value
            cplist[1] = True # updates list with new bool value
            return cplist
    return cplist

while (choice < 1 or choice > 4):
    print("-------------------------------------------------------")
    print("                 Simple Login Module                   ")
    print("-------------------------------------------------------")
    print("                         Menu                          ")
    print("-------------------------------------------------------")
    print("1. Add a new user\n"
          "2. Login existing user\n"
          "3. Change password\n"
          "4. Quit")
    print("-------------------------------------------------------")

    # Input validation
    try:
        choice = int(input("Please enter your choice(1-4): "))
    except ValueError:
        print("Wrong input - please enter a choice between 1-4")
        continue

    # Registering new user
    if choice == 1:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Extracts datetime
        fullname = input("Enter your full name: ")

        # Username validation
        cursor.execute("SELECT * FROM user_info") # Selects the database table
        rows = cursor.fetchall() # rows gets a tuple (kind of list) with all the database information
        lim = 1
        while lim != 0:
            username = input("Enter desired username: ")
            if (userval(rows, username) == True): # validating if username exists or not
                print("Username exists. Try again.")
            else:
                break
        # End username validation


        # Password validation
        while (password_1 != password_2):
            password_1 = input("Enter desired password: ")
            password_2 = input("Reenter desired password: ")
            if (password_1 != password_2):
                print("Password mismatch. Try again.")
            else:
                password = password_1
                break
        # End password validation

        user_id = getid() # Generates a random userid to be used as a primary key

        userinformation = [(user_id, fullname, username, password, timestamp)]
        cursor.executemany("INSERT INTO user_info VALUES(?, ?, ?, ?, ?)", userinformation)
                                # Takes the user information from list and inserts, in a secure
                                # way in the database table.
        conn.commit() # Commits the changes made in the database

        print("New user registration success.")
    # End registering new user

    # Begin login module
    elif choice == 2:
        username = input("Username: ")
        password = input("Password: ")
        cursor.execute("SELECT * FROM user_info")
        rows = cursor.fetchall()
        if (uauth(rows, username, password) == True):
            print("Success. You're now logged in.")
        else:
            print("Username & Pass mismatch.")
    # End login module

    # Begin update password module
    elif choice == 3:
        lim = 1
        while (lim != 0):
            username = input("Enter username: ")
            old_pass = input("Enter previous password: ")
            cursor.execute("SELECT * FROM user_info")
            rows = cursor.fetchall()
            if (changepass(rows, username, old_pass)[1] == True):
                newpass = input("Enter new password: ")
                cpid = changepass(rows, username, old_pass)[0]
                cursor.execute('''UPDATE user_info SET Password = ? WHERE ID = ?''', (newpass, cpid))
                                    # Updates the db table with new password.
                conn.commit()
                print("Password updated.")
                break
            print("Wrong old username and/or password.")
    # End update password module

    elif choice == 4:
        sys.exit()

    else:
        print("Please enter a choice between 1 and 4")


conn.close()
