from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved model
model = joblib.load('breast_cancer_rf_model.pkl')

FEATURE_NAMES = [
    'mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness',
    'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension',
    'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error',
    'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error',
    'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness',
    'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension'
]


@app.route('/')
def home():
    return render_template('index.html', feature_names=FEATURE_NAMES)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        features = [data[feature] for feature in FEATURE_NAMES]
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        prediction_proba = model.predict_proba(features_array)[0].tolist()
        return jsonify({
            'prediction': int(prediction),
            'probability': prediction_proba
        })
    except KeyError as e:
        return jsonify({'error': f'Missing feature: {e}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
