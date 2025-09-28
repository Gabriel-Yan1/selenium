# Automação com Selenium
## 🚀 Descrição
Projeto em Python usando Selenium para automatizar o download do arquivo globo.pdf do AVA da Unieuro/Grupo Ceuma. O script abre o navegador Chrome, realiza login, navega até a disciplina Projeto Integrador e baixa automaticamente o PDF.

## ✅ Funcionalidades
Abrir o Chrome e acompanhar os cliques em tempo real.

Realizar login automático no AVA.

Navegar até a disciplina Projeto Integrador.

Clicar no globo.pdf para download.

Espera automática até o download terminar.

Salvar arquivos na pasta downloads_ava.

## 🛠️ Pré-requisitos
Python 3.13.7.

Google Chrome instalado.

ChromeDriver compatível com sua versão do Chrome.

Instalar a biblioteca Selenium:

    python -m pip install selenium
Instalar o chromedriver: 
        https://googlechromelabs.github.io/chrome-for-testing/#stable
        
## ⚙️ Configuração
Abra o arquivo main.py.

Substitua suas credenciais na main.py:

    LOGIN = "seu_usuario_aqui"
    
    SENHA = "sua_senha_aqui"

Ajuste o caminho do ChromeDriver se necessário.

## ▶️ Como Executar
Abra PowerShell ou CMD na pasta do projeto.

Execute:

    python main.py
O Chrome abrirá e realizará todos os passos automaticamente.

O PDF será salvo em downloads_ava/ quando o download terminar.

##⚡ Observações
O navegador fica aberto para acompanhar os cliques.

O script espera automaticamente até o download terminar, sem precisar de time.sleep.

Funciona em Windows; para outros sistemas, ajuste o caminho do ChromeDriver.
