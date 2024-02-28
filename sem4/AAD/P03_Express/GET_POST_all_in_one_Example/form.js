const express = require('express');
const bodyParser = require('body-parser');
app = express()

app.use(bodyParser.urlencoded({ extended: false }));

app.get("/", function(req, res) {
	res.sendFile(__dirname + "/form.html");
});

app.get("/get", function(req, res) {
	response = {
		first_name: req.query.fname,
		last_name: req.query.lname
	}
	console.log(response)
	res.send("GET: " + JSON.stringify(response))
});

app.post("/get", function(req, res) {
	response = {
		first_name: req.body.fname,
		last_name: req.body.lname
	}
	console.log(response)
	res.send("POST: " + JSON.stringify(response))
});

app.listen(5000);
console.log("Server started at localhost:5000")
