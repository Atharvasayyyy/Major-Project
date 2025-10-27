# Hobbies MVP Project

A hobby recommendation system using Node.js backend and Python machine learning model.

## Project Structure

```
hobbies-mvp/
├── backend/                  # Node.js backend
│   ├── package.json         # Node.js dependencies and scripts
│   ├── server.js           # Express server setup
│   ├── routes/            # API routes
│   ├── controllers/       # Request handlers
│   └── utils/            # Utility functions
├── model/                # Python ML model
│   ├── requirements.txt  # Python dependencies
│   ├── train_model.py   # Model training script
│   └── predict.py       # Prediction script
├── data/               # Dataset
│   └── hobbies_dataset.csv
└── README.md
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```
2. Install dependencies:
   ```
   npm install
   ```
3. Start the server:
   ```
   npm start
   ```

### Python Model Setup

1. Navigate to the model directory:
   ```
   cd model
   ```
2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Train the model:
   ```
   python train_model.py
   ```

## API Usage

Make a POST request to `/api/predict` with user data to get hobby recommendations:

```json
{
  "age": 25,
  "gender": "M",
  "location": "urban",
  "interests": "technology",
  "personality_type": "introvert"
}
```

The API will return top 5 recommended hobbies with their probabilities.
