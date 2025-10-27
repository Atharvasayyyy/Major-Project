const { spawn } = require("child_process");
const path = require("path");

/**
 * callPythonScript
 * @param {string} scriptPath - Path to the Python script
 * @param {Object} inputData - JSON object to send as input
 * @returns {Promise<string>} - Resolves with Python script output
 */
function callPythonScript(scriptPath, inputData) {
  return new Promise((resolve, reject) => {
    // Correct path to predict.py
    const resolvedPath = path.join(__dirname, "..", "..", "model", "predict.py");

    const py = spawn("python", [resolvedPath, JSON.stringify(inputData)]);

    let result = "";
    let error = "";

    py.stdout.on("data", (data) => {
      result += data.toString();
    });

    py.stderr.on("data", (data) => {
      error += data.toString();
    });

    py.on("close", (code) => {
      if (code === 0) {
        try {
          resolve(JSON.parse(result));
        } catch (parseError) {
          reject(parseError);
        }
      } else {
        reject(new Error(error || `Python exited with code ${code}`));
      }
    });
  });
}

module.exports = { callPythonScript };
