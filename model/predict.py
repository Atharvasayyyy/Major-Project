import sys
import json
import joblib
import numpy as np
import os

def bp_status(sysbp, diabp):
    """Determine blood pressure status"""
    if sysbp > 140 or diabp > 90:
        return "Hypertension", True
    elif 120 <= sysbp <= 139 or 80 <= diabp <= 89:
        return "Prehypertension Warning", True
    else:
        return "Normal", False

def calculate_hobby_score(sysbp, diabp):
    """Calculate hobby score based on blood pressure"""
    score = max(0, 10 - ((sysbp - 100) / 10 + (diabp - 70) / 10))
    return round(score, 1)

def predict_hobby(data):
    try:
        # Get the absolute path to the model file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, 'hobby_model.pkl')
        
        # Extract basic info
        child_id = data.get("child_id")
        hobbies = data.get("hobbies", [])
        results = []

        # Process each hobby
        for hobby in hobbies:
            hobby_name = hobby["name"]
            sysbp = hobby["sysbp"]
            diabp = hobby["diabp"]

            # Calculate score and status
            score = calculate_hobby_score(sysbp, diabp)
            status, alert = bp_status(sysbp, diabp)

            results.append({
                "hobby": hobby_name,
                "score": score,
                "status": status,
                "alert": alert
            })

        # Get model prediction if model exists
        try:
            model = joblib.load(model_path)
            features = np.array([
                data['age'],
                data['gender'],
                data['bmi'],
                data['sysbp'],
                data['diabp']
            ])
            prediction = model.predict(features.reshape(1, -1))[0]
            probability = float(model.predict_proba(features.reshape(1, -1))[0].max())
        except:
            prediction = None
            probability = None

        # Find recommended hobby (highest score)
        recommendation = max(results, key=lambda x: x["score"])["hobby"] if results else None

        return {
            "child_id": child_id,
            "results": results,
            "recommendation": recommendation,
            "model_prediction": prediction,
            "prediction_probability": probability
        }

    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    # Read input from Node.js
    input_data = json.loads(sys.argv[1])
    
    # Make prediction
    result = predict_hobby(input_data)
    
    # Return result to Node.js
    print(json.dumps(result))
