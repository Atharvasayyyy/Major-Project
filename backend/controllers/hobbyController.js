const { callPythonScript } = require("../utils/callPython");
const path = require('path');

const predictHobby = async (req, res) => {
  try {
    // Validate input
    const requiredFields = ['child_id', 'age', 'gender', 'bmi', 'hobbies'];
    for (const field of requiredFields) {
      if (!(field in req.body)) {
        return res.status(400).json({ error: `Missing required field: ${field}` });
      }
    }

    // Get absolute path to Python script
    const scriptPath = path.join(__dirname, '..', '..', 'model', 'predict.py');

    // Call Python script
    const prediction = await callPythonScript(scriptPath, req.body);
    
    // Handle response - could be string or object
    let result;
    if (typeof prediction === 'string') {
      try {
        result = JSON.parse(prediction);
      } catch (parseError) {
        throw new Error(`Invalid JSON response: ${prediction}`);
      }
    } else {
      result = prediction;
    }

    if ('error' in result) {
      throw new Error(result.error);
    }

    res.json(result);

  } catch (err) {
    console.error("Prediction Error:", err.message);
    res.status(500).json({ 
      error: "Prediction failed", 
      details: err.message,
      stack: process.env.NODE_ENV === 'development' ? err.stack : undefined
    });
  }
};

module.exports = { predictHobby };
