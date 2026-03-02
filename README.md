# 🌦️ Desafio de Integração: Clima e Tempo

Este projeto faz parte de um desafio técnico para demonstrar a integração de scripts Python com APIs REST públicas e manipulação de dados em planilhas.

## 📋 Objetivo
O script consome a API pública **Open-Meteo** para coletar dados climáticos históricos da última semana (temperatura máxima, mínima, precipitação e velocidade do vento) para a cidade de Brasília, BR.

## 🚀 Funcionalidades
- Conexão com API REST (Open-Meteo).
- Coleta de dados históricos dos últimos 7 dias.
- Processamento de dados com a biblioteca `pandas`.
- Exportação automática para formatos **Excel (.xlsx)** e **CSV**.
- Estrutura preparada para integração com **Google Sheets**.

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Pandas**: Manipulação e análise de dados.
- **Requests**: Consumo de APIs REST.
- **Openpyxl**: Geração de arquivos Excel.

## 📂 Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/[SEU_USUARIO]/desafio-clima-python.git
   cd desafio-clima-python
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script:
   ```bash
   python weather_script.py
   ```

## 📊 Resultados
Após a execução, o script gerará dois arquivos na raiz do projeto:
- `dados_climaticos.xlsx`
- `dados_climaticos.csv`

---
*Desenvolvido como parte de um processo seletivo.*
