const express = require('express');
const router = express.Router();
const hobbyController = require('../controllers/hobbyController');

// Test endpoint
router.get('/test', (req, res) => {
    res.json({ message: "API is working!" });
});

// Predict hobby endpoint
router.post('/predict', hobbyController.predictHobby);

module.exports = router;
