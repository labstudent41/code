Before proceeding, check if MongoDB is installed properly.
Open MongoDB Compass and connect.
If it connects successfully, proceed futher.
If it doesn't, then you will have to troubleshoot.


To run the WEB app, go inside the directory using command prompt in VS Code
> cd WEB/

Install required packages
> npm install path body-parser mangoose express

Start the server
> node app.js

Go to browser and open localhost at given port
http://127.0.0.1:3000/

Fill the form and submit. You will get JSON data in return.


To retrive data from database. Go to /display
http://127.0.0.1:3000/display

Enter your name and submit.
You will get your previously submitted form data back in JSON format.
