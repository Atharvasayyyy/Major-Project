import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

# Load hypertension dataset only since hobbies dataset is not in correct format
hypertension_data = pd.read_excel("../data/20220721_Hypertension_Final data table_Zenodo.xlsx")

# Select features and target
X = hypertension_data[['Age', 'Gender', 'BMI', 'sysbp', 'diabp']]
y = hypertension_data['Hypertension_US']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model with adjusted parameters
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42
)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "hobby_model.pkl")
print("Model trained and saved as hobby_model.pkl")

# Print model summary
print("\nFeatures used:", X.columns.tolist())
print("Number of training samples:", len(X_train))
print("Training accuracy:", model.score(X_train, y_train))
print("Testing accuracy:", model.score(X_test, y_test))

# Feature importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
})
print("\nFeature Importance:")
print(feature_importance.sort_values(by='importance', ascending=False))
