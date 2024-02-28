const express = require("express");
const bodyParser = require("body-parser");
var app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static("public"));

app.get("/" , function(req, res) {
	res.sendFile(__dirname + "/" + "post_index.html");
});

app.post("/get", function(req, res) {
	response = {
		first_name : req.body.fname,
		last_name : req.body.lname
	};
	console.log(req.body);
	res.send(JSON.stringify(response));
	// res.send(res.body);
});

var server = app.listen(5000, function() {
	var host = server.address().address
	var port = server.address().port;
	console.log("example app listening at http://%s:%s", host, port);
});
