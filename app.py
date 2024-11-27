from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Carregando o modelo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'rfcemployee.pkl'), 'rb') as file:
    model_data = pickle.load(file)

model = model_data["model"]
model_columns = model_data["model_columns"]

# Organização de dados
def process_data(data):
    df = pd.DataFrame(data, index=[0])
    df = df[model_columns]
    return df

def validate_and_process_input(data):
    try:
        # Função para validar se o valor é um inteiro
        def try_int(value, default=0):
            try:
                return int(value)
            except ValueError:
                return default
        
        # Processamento dos dados
        validated_data = {
            'JoiningYear': try_int(data.get('JoiningYear', 0)),
            'PaymentTier': try_int(data.get('PaymentTier', 0)),
            'Age': try_int(data.get('Age', 0)),
            'EverBenched': 1 if data.get('EverBenched') == 'Yes' else 0,
            'ExperienceInCurrentDomain': try_int(data.get('ExperienceInCurrentDomain', 0)),
            'Female': 1 if data.get('Sexo') == '1' else 0,
            'Male': 1 if data.get('Sexo') == '0' else 0,
            'Bachelors': 1 if data.get('Education') == 'Bachelors' else 0,
            'Masters': 1 if data.get('Education') == 'Masters' else 0,
            'PHD': 1 if data.get('Education') == 'PHD' else 0
        }

        # Validação de valores aceitáveis
        if validated_data['PaymentTier'] not in [1, 2, 3, 4, 5]:
            return None, "Erro de validação: PaymentTier deve ser um número entre 1 e 5."
        
        if validated_data['Age'] < 18 or validated_data['Age'] > 100:
            return None, "Erro de validação: Idade deve estar entre 18 e 100."

        # Adicionar mais validações, se necessário, para outros campos
        if validated_data['ExperienceInCurrentDomain'] < 0:
            return None, "Erro de validação: Experiência no domínio atual não pode ser negativa."

        return validated_data, None
    except Exception as e:
        return None, f"Erro inesperado: {str(e)}"

@app.route('/', methods=['GET'])
def home():   
    return render_template("index.html")

@app.route('/graphs', methods=["GET"])
def graphs():
    return render_template("graficos.html")

@app.route('/aboutus', methods=["GET"])
def about_us():
    return render_template("sobre.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template("data.html")
    elif request.method == 'POST':
        raw_data = request.form
        data, error = validate_and_process_input(raw_data)
        
        # Se houver erro de validação, renderizar data.html com a mensagem de erro
        if error:
            return render_template("data.html", prediction_result=f"Erro: {error}")
        
        processed_data = process_data(data)
        prediction = model.predict(processed_data)
        message = "Left the company" if prediction[0] == 1 else "Didn't leave the company"
        return render_template("data.html", prediction_result=message)

if __name__ == '__main__':
    app.run(debug=True)
