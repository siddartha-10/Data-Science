from flask import Flask, request, Response, render_template
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

# Load the StandardScaler and Machine Learning Model
with open("standardScalar.sav", 'rb') as f:
    scalar = pickle.load(f)

with open("modelForPrediction.sav", 'rb') as f:
    model = pickle.load(f)

class ClientApi:

    def __init__(self):
        pass

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predictRoute():
    try:
        # Extract form data as floats
        data = {
            'Pregnancies': float(request.form['pregnancies']),
            'Glucose': float(request.form['glucose']),
            'BloodPressure': float(request.form['bloodPressure']),
            'SkinThickness': float(request.form['skinThickness']),
            'Insulin': float(request.form['insulin']),
            'BMI': float(request.form['bmi']),
            'DiabetesPedigreeFunction': float(request.form['diabetesPedigree']),
            'Age': float(request.form['age'])
        }

        # Create a DataFrame from the input data
        data_df = pd.DataFrame([data])

        # Scale the data using the loaded StandardScaler
        scaled_data = scalar.transform(data_df)

        # Make a prediction using the loaded model
        predict = model.predict(scaled_data)

        if predict[0] == 1:
            result = 'Diabetic'
        else:
            result = 'Non-Diabetic'

        return result
    except Exception as e:
        print('exception is', e)
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
