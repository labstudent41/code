const express = require('express');
const path = require('path');
const mongoose=require("mongoose");
const bodyParser = require("body-parser");
const router = express.Router();
const app = express();
const User = require('./models/user');
const port = 3000;

const database = 'mongodb://127.0.0.1:27017/vartak'

mongoose.connect(database);

mongoose.connection.on('connected', () => {
    console.log('Connected to database' +database);
});

mongoose.connection.on('error', (err)=>{
    console.log('no to database '+database);
});
app.use(express.json());
app.use(express.urlencoded({extended: true}));

const routes = require('./routes');
app.use('/datas', routes);

app.get('/', async (req, res) => {
  try {
    res.sendFile(__dirname + '/index.html');
  } catch (error) {
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});

app.get('/display', (req, res) => {
  res.sendFile(__dirname + '/display.html');
})

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
