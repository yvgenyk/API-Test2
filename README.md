# API Testing Program
- This program is designed to test OHT main API calls.
- The program is written in Python.
- The program GUI is designed in PyQt.
- Main library to send API calls is Python requests.

# Overview

The main purpose of the program is to make integration testing of API methods fast and simple.
The program has a main json file that have all the calls to check (created manually) and executes this file line by line. Each line has the call method itself and the values to check in the response to the call. 
There is a settings window in which the user has to insert authentication keys and pricing of a proper test.
The user can see all the calls written in the file in a user friendly window, accessed from the main menu, in this window the user can also change each call and test each call separately.
There is a new line window to create and insert new lines to the main test file.
And finally there is a report window to show the user the test results, each line.

Once the user is ready to test, "Start test" button need to be clicked.
Then the test will start and the user has a table which shows him every line that is tested in three colors:
- Yellow - The line executed properly but nothing was checked in the response.
- Green - Line was executed properly and values that were checked found correct.
- Red - Line wasn't executed properly; bad status return from server or the checked values were incorrect and there is a problem with sites API.

After the program will finish the user can see the report and know if all is well with the site's API or not.
