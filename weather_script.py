import requests
import pandas as pd
from datetime import datetime, timedelta
import os

def get_weather_data(lat=-15.7801, lon=-47.9292, city="Brasília"):
    """
    Busca dados climáticos da última semana usando a API Open-Meteo.
    Localização padrão: Brasília, DF.
    """
    # Última semana
    end_date = datetime.now().date() - timedelta(days=1)
    start_date = end_date - timedelta(days=7)
    
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date.strftime("%Y-%m-%d" ),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum", "windspeed_10m_max"],
        "timezone": "America/Sao_Paulo"  # Fuso horário oficial de Brasília
    }
    
    print(f"Buscando dados para {city} de {start_date} até {end_date}...")
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        daily_data = data['daily']
        
        # Organizar os dados em um DataFrame do Pandas
        df = pd.DataFrame({
            "Data": daily_data['time'],
            "Temp Max (°C)": daily_data['temperature_2m_max'],
            "Temp Min (°C)": daily_data['temperature_2m_min'],
            "Chuva (mm)": daily_data['precipitation_sum'],
            "Vento Max (km/h)": daily_data['windspeed_10m_max']
        })
        
        df['Cidade'] = city
        return df
    else:
        print(f"Erro ao acessar API: {response.status_code}")
        return None

def save_to_excel(df, filename="dados_climaticos.xlsx"):
    """Salva o DataFrame em um arquivo Excel."""
    df.to_excel(filename, index=False)
    print(f"Dados salvos com sucesso em {filename}")

def main():
    # Coletar dados de Brasília
    df = get_weather_data()
    
    if df is not None:
        # Exibir prévia no terminal
        print("\nPrévia dos dados coletados:")
        print(df.head(10))
        
        # Salvar os arquivos localmente
        save_to_excel(df)
        df.to_csv("dados_climaticos.csv", index=False)
        
        print("\nTarefa concluída com sucesso para Brasília!")
    else:
        print("Falha na execução do script.")

if __name__ == "__main__":
    main()
