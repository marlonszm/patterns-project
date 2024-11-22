from flask import Flask, render_template, request, flash
import pickle 
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'rfcemployee.pkl'), 'rb') as file:
    model_data = pickle.load(file)

app = Flask(__name__)

model = model_data["model"]
model_columns = model_data["model_columns"]

def process_data(data):
    df = pd.DataFrame(data, index=[0])
    df = df[model_columns]
    return df

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = {
            'JoiningYear': int(request.form['JoiningYear']),
            'PaymentTier': int(request.form['PaymentTier']),
            'Age': int(request.form['Age']),
            'EverBenched': int(request.form['EverBenched']),
            'ExperienceInCurrentDomain': int(request.form['ExperienceInCurrentDomain']),
            'Female': 1 if request.form['Sexo'] == '1' else 0,  # Mapeia sexo
            'Male': 1 if request.form['Sexo'] == '0' else 0,  # Mapeia sexo
            'Bachelors': 1 if request.form['Education'] == 'Bachelors' else 0,
            'Masters': 1 if request.form['Education'] == 'Masters' else 0,
            'PHD': 1 if request.form['Education'] == 'PHD' else 0,
            'Education': request.form['Education']
        }
        processed_data = process_data(data)
        prediction = model.predict(processed_data)
        if prediction == 1:
            message = "Left the company"
        else:
            message = "Didn't leave the company"
            
        return render_template("index.html", prediction_result=message)
    
if __name__ == '__main__':
    app.run(debug=True)