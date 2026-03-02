# Automação de Dados Climáticos: Brasília (DF)

Este repositório contém um script em Python desenvolvido para automatizar a coleta e o processamento de dados meteorológicos históricos. O projeto foi criado como parte de um desafio técnico focado em **integrações via API REST** e manipulação de dados para negócios.

## Objetivo do Projeto
A ideia principal é extrair métricas climáticas da última semana (temperatura, precipitação e vento) para a cidade de **Brasília**, consolidando essas informações em formatos de planilha (Excel e CSV) prontos para análise ou importação em bancos de dados.

## Stack Técnica
*   **Linguagem:** Python 3.x
*   **Bibliotecas Principais:** 
    *   `Pandas`: Para estruturação e limpeza dos dados.
    *   `Requests`: Para consumo da API REST.
    *   `Openpyxl`: Engine para geração de arquivos `.xlsx`.
*   **Fonte de Dados:** [Open-Meteo API](https://open-meteo.com/ ) (escolhida pela precisão e facilidade de integração com dados históricos).

## Como o Script Funciona
1.  **Conexão:** O script faz uma requisição `GET` ao endpoint de arquivo da Open-Meteo usando as coordenadas geográficas de Brasília.
2.  **Processamento:** Os dados brutos em JSON são convertidos em um DataFrame do Pandas, onde as colunas são renomeadas e organizadas para facilitar a leitura humana.
3.  **Exportação:** O script gera automaticamente dois arquivos na raiz do projeto:
    *   `dados_climaticos.xlsx`: Ideal para visualização rápida e filtros no Excel.
    *   `dados_climaticos.csv`: Formato leve para integração com outros sistemas ou bancos de dados.

## Como Rodar Localmente
1.  Clone o repositório:
    ```bash
    git clone https://github.com/SEU_USUARIO/desafio-clima-python.git
    ```
2.  Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```
3.  Execute o script:
    ```bash
    python weather_script.py
    ```

## Estrutura dos Dados Coletados
O script extrai as seguintes métricas diárias:
*   **Data:** Dia da medição.
*   **Temp Max/Min:** Oscilação térmica em °C.
*   **Chuva (mm ):** Volume de precipitação acumulado.
*   **Vento Max (km/h):** Velocidade máxima das rajadas.

---
*Projeto desenvolvido para demonstração técnica de integração e manipulação de dados com Python.*
