import requests

def realDolar(valor_em_reais):
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        if response.status_code == 200:
            data = response.json()
            taxa_dolar = data['rates']['BRL']

            # Converter para dolar
            valor_em_dolares = valor_em_reais * taxa_dolar

            return valor_em_dolares

        else:
            print(f"Erro ao consultar API: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

