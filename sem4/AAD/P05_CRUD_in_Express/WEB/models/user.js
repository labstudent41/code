//create model folder a place this file inside it
const mongoose = require('mongoose');

//create a schema
const UserSchema = mongoose.Schema({
    name:{
        type: String
    },
    email:{
        type:String,
        required: true
    },
    username:{
        type:String,
        required:true
    },
    password:{
        type: String,
        required:true
    }
  });
  
  const User = mongoose.model('User',UserSchema);

  module.exports = User;