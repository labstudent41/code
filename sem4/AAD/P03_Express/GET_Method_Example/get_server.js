const express = require("express");
var app = express()

app.use(express.static("public"));
app.get("/" , function(req, res) {
	res.sendFile(__dirname + "/" + "get_index.html");
});

app.get("/get", function(req, res) {
	response = {
		first_name : req.query.fname,
		last_name : req.query.lname
	};
	console.log(response);
	res.send(JSON.stringify(response));
	// res.send(response);
});

var server = app.listen(5000, function() {
	var host = server.address().address
	var port = server.address().port;
	console.log("example app listening at http://%s:%s", host, port);
});
