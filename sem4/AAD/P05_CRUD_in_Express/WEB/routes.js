const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const User = require('./models/user');
  
router.post('/index',async (req,res) => {
    try {
        const userData = req.body;
        const newUser = new User(userData);
  
        const validationError = newUser.validateSync();
        if (validationError) {
            throw validationError;
        }
  
        output = await newUser.save();
        res.status(201).json(newUser);
    } catch (error) {
        console.error('Error saving user:', error.message);
        res.status(400).json({ error: error.message });
    }
});

router.post('/info', async (req, res) => {
    try {
        console.log(req.body);
        const b = req.body;
        const user = await User.findOne({name: b.name});
  
        if (!user) {
            return res.status(404).send('user not found');
        }
  
        res.send(user);
    } catch (error) {
        console.error('Error retrieving user:', error.message);
        res.status(500).send('Internal Server Error');
    }
  });

module.exports = router;