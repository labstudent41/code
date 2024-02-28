const express = require('express');
const app = express();

app.get("/", (req, res) => {
	res.send("<h1>Welcome to full stack world</h1>");
});

app.listen(5000, () => {
	console.log("Listening on port 5000...");
});
