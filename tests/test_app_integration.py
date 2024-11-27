import pytest
import subprocess
import time
import socket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Função para iniciar o servidor Flask em um subprocesso
def start_flask_app():
    # Iniciar o servidor Flask usando subprocess
    return subprocess.Popen(["python", "app.py"])

# Função para verificar se o servidor Flask está disponível
def wait_for_server_to_start(host='localhost', port=5000, timeout=30):
    """Espera o servidor Flask estar disponível antes de rodar os testes."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            # Tenta se conectar ao servidor Flask
            with socket.create_connection((host, port), timeout=1):
                return True
        except (socket.timeout, ConnectionRefusedError):
            time.sleep(1)
    return False  # Timeout se não conseguir conectar

# Função para configurar o Selenium WebDriver
@pytest.fixture(scope="function")
def browser():
    # Inicia o servidor Flask
    flask_process = start_flask_app()
    
    # Espera o servidor Flask iniciar
    if not wait_for_server_to_start():
        flask_process.terminate()  # Se o servidor não iniciar no tempo esperado, interrompe o processo
        pytest.fail("Servidor Flask não foi iniciado no tempo esperado.")
    
    # Configura o WebDriver para o Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Para rodar sem abrir uma janela do navegador
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver  # Retorna o driver para o teste
    
    # Finaliza o WebDriver e o processo Flask após o teste
    driver.quit()
    flask_process.terminate()

# Testes de integração
def test_index_page(browser):
    browser.get("http://localhost:5000/predict")
    assert "Visualização de Gráficos" in browser.title  # Ajustado para o título correto

def test_form_submission_valid(browser):
    browser.get("http://localhost:5000/predict")
    
    # Preencher os campos do formulário
    browser.find_element(By.ID, "JoiningYear").send_keys("2020")
    browser.find_element(By.ID, "PaymentTier").send_keys("2")
    browser.find_element(By.ID, "Age").send_keys("30")
    
    # Selecionar o gênero (exemplo: selecionar Female)
    browser.find_element(By.ID, "Female").click()
    
    browser.find_element(By.ID, "EverBenched").send_keys("1")
    browser.find_element(By.ID, "ExperienceInCurrentDomain").send_keys("5")
    browser.find_element(By.ID, "Education").send_keys("Masters")
    
    # Submeter o formulário
    browser.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    
    # Aguardar a página carregar e verificar se a previsão foi exibida
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    # Verifique se a página contém o resultado esperado
    assert "Prediction Result" in browser.page_source



