import requests
import pandas as pd
from datetime import datetime, timedelta

# Configurações de Brasília
LAT_BSB = -15.7801
LON_BSB = -47.9292

def buscar_clima_semana(lat, lon, cidade="Brasília"):
    # Pegando o intervalo dos últimos 7 dias (até ontem)
    hoje = datetime.now().date()
    data_fim = hoje - timedelta(days=1)
    data_inicio = data_fim - timedelta(days=7)
    
    # API Open-Meteo (Archive)
    endpoint = "https://archive-api.open-meteo.com/v1/archive"
    
    payload = {
        "latitude": lat,
        "longitude": lon,
        "start_date": data_inicio.isoformat( ),
        "end_date": data_fim.isoformat(),
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum", "windspeed_10m_max"],
        "timezone": "America/Sao_Paulo"
    }
    
    print(f"-> Coletando dados de {cidade} ({data_inicio} a {data_fim})...")
    
    try:
        r = requests.get(endpoint, params=payload)
        r.raise_for_status()
        res = r.json()
        
        # Montando o dataframe com o que interessa
        dados = res['daily']
        df = pd.DataFrame({
            "data": dados['time'],
            "temp_max": dados['temperature_2m_max'],
            "temp_min": dados['temperature_2m_min'],
            "chuva_mm": dados['precipitation_sum'],
            "vento_max_kmh": dados['windspeed_10m_max'],
            "cidade": cidade
        })
        
        return df
        
    except Exception as e:
        print(f"Erro na integração: {e}")
        return None

if __name__ == "__main__":
    # Execução principal
    df_clima = buscar_clima_semana(LAT_BSB, LON_BSB)
    
    if df_clima is not None:
        # Exportando para os formatos solicitados
        df_clima.to_excel("dados_climaticos.xlsx", index=False)
        df_clima.to_csv("dados_climaticos.csv", index=False)
        
        print("\nProcesso finalizado. Planilhas geradas com sucesso!")
        print(df_clima.tail()) # Mostra as últimas linhas pra conferir
    else:
        print("Não foi possível gerar os arquivos.")
