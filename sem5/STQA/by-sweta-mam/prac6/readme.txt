workflow :

    The app.py file hosts the index page and sends data to index page by reading the excel file , so the first task of displaying user data is done.
    The test.py file conatins the test case which first checks the marks of the student from the table and extracts students having marks>60
    in any one or more than that of the subjet and stores it in array. Then we just iterate the array conating students data and extract the topper student
    for each subject ( for the analysis part of the question)

How to run:
    Terminal 1 : python app.py
    Terminal 2 : python test.py