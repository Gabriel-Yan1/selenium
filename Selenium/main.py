import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === CONFIGURAÇÕES ===
URL = "https://ava.grupoceuma.com.br"
LOGIN = "seu_usuario_aqui"
SENHA = "sua_senha_aqui"      
DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads_ava")

# === CAMINHO DO CHROMEDRIVER ===
CHROMEDRIVER_PATH = r"C:\Users\gyan1\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# === CRIA DRIVER CONFIGURADO ===
def create_chrome_driver(download_dir):
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
    }
    options.add_experimental_option("prefs", prefs)
    
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def baixar_globo_pdf():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    driver = create_chrome_driver(DOWNLOAD_DIR)
    wait = WebDriverWait(driver, 20)

    try:
        # 1) Abrir o AVA
        driver.get(URL)

        # 2) Clicar no ícone da Unieuro
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="unieuro"]'))).click()

        # 3) Clicar em "Acessar login"
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="usernavigation"]/div[4]/div/span/a'))).click()

        # 4) Preencher login e senha
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))).send_keys(LOGIN)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(SENHA)

        # 5) Clicar no botão logar
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginbtn"]'))).click()

        # 6) Entrar na disciplina Projeto Integrador
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frontpage-course-list"]/div/div[2]/div[2]/div[1]/div[1]/div/a'))).click()

        # 7) Clicar no arquivo globo.pdf
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="module-37424"]/div/div[2]/div/div[1]/div/div[2]/div/a'))).click()

        # 8) Espera simples pelo download
        time.sleep(10)

        print("Download finalizado em:", DOWNLOAD_DIR)

    finally:
        driver.quit()

if __name__ == "__main__":
    baixar_globo_pdf()

