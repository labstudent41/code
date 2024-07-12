
const express = require('express')
const fileUpload = require('express-fileupload')
var app = express();
const port = 3000
app.use(fileUpload());

app.get('/', (req, res) => {
	res.sendFile(__dirname + '/index.html');
})

app.post('/upload', (req, res) => {
	if (!req.files)
		return res.status(400).send("No files were uploaded.");

	console.log(req.files)
	const file = req.files.file;
	const filename = file.name

	file.mv('./uploads/' + filename, (err) => {
		if (err)
			res.send(err)
		else
			res.send(filename + " uploaded successfully")
	})
})

app.listen(port, () => {
	console.log(`server is runnning at port ${port}`)
});
