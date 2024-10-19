const mongoose = require('mongoose');

// Define the user schema
const userSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
    unique: true,  // Ensure each username is unique
  },
  password: {
    type: String,
    required: true,  // Password is required
  },
});

// Create and export the User model
const User = mongoose.model('User', userSchema);

module.exports = User;
