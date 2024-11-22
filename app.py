from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Carregando o modelo
with open('rfcemployee.pkl', 'rb') as file:
    model_data = pickle.load(file)

model = model_data["model"]
model_columns = model_data["model_columns"]

# Organização de dados
def process_data(data):
    df = pd.DataFrame(data, index=[0])
    df = df[model_columns]
    return df

# Validação e processamento
def validate_and_process_input(data):
    try:
        validated_data = {
            'JoiningYear': int(data.get('JoiningYear', 0)),
            'PaymentTier': int(data.get('PaymentTier', 0)),
            'Age': int(data.get('Age', 0)),
            'EverBenched': 1 if data.get('EverBenched') == 'Yes' else 0,
            'ExperienceInCurrentDomain': int(data.get('ExperienceInCurrentDomain', 0)),
            'Female': 1 if data.get('Sexo') == '1' else 0,
            'Male': 1 if data.get('Sexo') == '0' else 0,
            'Bachelors': 1 if data.get('Education') == 'Bachelors' else 0,
            'Masters': 1 if data.get('Education') == 'Masters' else 0,
            'PHD': 1 if data.get('Education') == 'PHD' else 0
        }
        return validated_data, None
    except ValueError as e:
        return None, f"Erro de validação: {str(e)}"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        raw_data = request.form
        data, error = validate_and_process_input(raw_data)
        if error:
            return render_template("index.html", prediction_result=f"Erro: {error}")
        processed_data = process_data(data)
        prediction = model.predict(processed_data)
        message = "Left the company" if prediction[0] == 1 else "Didn't leave the company"
        return render_template("index.html", prediction_result=message)

if __name__ == '__main__':
    app.run(debug=True)
