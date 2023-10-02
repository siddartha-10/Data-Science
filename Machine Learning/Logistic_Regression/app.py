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
        data = request.form.to_dict()
        data_df = pd.DataFrame([data])
        scaled_data = scalar.transform(data_df)
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
