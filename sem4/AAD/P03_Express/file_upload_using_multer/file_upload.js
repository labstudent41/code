const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const multer = require('multer');
const app = express();

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: false }));

const upload = multer({ dest: "/tmp/files" });

app.get('/', function(req, res) {
	res.sendFile(`${__dirname}/file_upload.html`);
});

app.post("/file_upload", upload.single("file"), (req, res) => {
	console.log(req.file);
	const file = `${__dirname}/downloads/${req.file.originalname}`;

	fs.readFile(req.file.path, (err, data) => {
		fs.writeFile(file, data, (err) => {
			let response;
			if (err) {
				response = { error: err }
			} else {
				response = {
					message: "File uploaded succesfully",
					filename: req.file.originalname
				};
			}
			console.log(response);
			res.json(response);
		});
	});

});

app.listen(5000);
console.log("Server started at http://127.0.0.1:5000")
