import requests
import os
from email_sender import enviar_email

TOKEN = os.getenv("BRAPI_TOKEN")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

alertas = {
    "BTC_62700": False,
    "BTC_70500": False,
    "BTC_75500": False,
    "BTC_80500": False,
    "PETR4_LOW": False,
    "ITSA3_LOW": False,
    "BBDC3_LOW": False,
    "ABEV3_LOW": False
}

def preco_crypto(symbol):
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        r = requests.get(url, timeout=15)
        data = r.json()
        return float(data["bitcoin"]["usd"])
    except Exception as e:
        print(f"Erro ao buscar preço do BTC: {e}")
        return None

def preco_acao(ticker):
    try:
        url = f"https://brapi.dev/api/quote/{ticker}"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        r = requests.get(url, headers=headers, timeout=10)
        data = r.json()
        return data["results"][0]["regularMarketPrice"]
    except Exception as e:
        print(f"Erro ao buscar preço de {ticker}: {e}")
        return None

def monitor():
    btc = preco_crypto("BTCUSDT")
    petr4 = preco_acao("PETR4")
    itsa3 = preco_acao("ITSA3")
    bbdc3 = preco_acao("BBDC3")
    abev3 = preco_acao("ABEV3")

    if btc is not None:
        print(f"BTCUSDT: {btc}")
        if btc < 62700 and not alertas["BTC_62700"]:
            enviar_email("BTC abaixo de 62700", f"Preço: {btc}", EMAIL_USER, EMAIL_PASS)
            alertas["BTC_62700"] = True
        if btc >= 62700:
            alertas["BTC_62700"] = False

        if btc > 70500 and not alertas["BTC_70500"]:
            enviar_email("BTC acima de 70500", f"Preço: {btc}", EMAIL_USER, EMAIL_PASS)
            alertas["BTC_70500"] = True
        if btc <= 70500:
            alertas["BTC_70500"] = False

        if btc > 75500 and not alertas["BTC_75500"]:
            enviar_email("BTC acima de 75500", f"Preço: {btc}", EMAIL_USER, EMAIL_PASS)
            alertas["BTC_75500"] = True
        if btc <= 75500:
            alertas["BTC_75500"] = False

        if btc > 80500 and not alertas["BTC_80500"]:
            enviar_email("BTC acima de 80500", f"Preço: {btc}", EMAIL_USER, EMAIL_PASS)
            alertas["BTC_80500"] = True
        if btc <= 80500:
            alertas["BTC_80500"] = False

    if petr4 is not None:
        print(f"PETR4: {petr4}")
        if petr4 < 35 and not alertas["PETR4_LOW"]:
            enviar_email("PETR4 abaixo de 35", f"Preço: {petr4}", EMAIL_USER, EMAIL_PASS)
            alertas["PETR4_LOW"] = True
        if petr4 >= 35:
            alertas["PETR4_LOW"] = False

    if itsa3 is not None:
        print(f"ITSA3: {itsa3}")
        if itsa3 < 12.72 and not alertas["ITSA3_LOW"]:
            enviar_email("ITSA3 abaixo de 12.72", f"Preço: {itsa3}", EMAIL_USER, EMAIL_PASS)
            alertas["ITSA3_LOW"] = True
        if itsa3 >= 12.72:
            alertas["ITSA3_LOW"] = False

    if bbdc3 is not None:
        print(f"BBDC3: {bbdc3}")
        if bbdc3 < 16.87 and not alertas["BBDC3_LOW"]:
            enviar_email("BBDC3 abaixo de 16.87", f"Preço: {bbdc3}", EMAIL_USER, EMAIL_PASS)
            alertas["BBDC3_LOW"] = True
        if bbdc3 >= 16.87:
            alertas["BBDC3_LOW"] = False

    if abev3 is not None:
        print(f"ABEV3: {abev3}")
        if abev3 < 14.74 and not alertas["ABEV3_LOW"]:
            enviar_email("ABEV3 abaixo de 14.74", f"Preço: {abev3}", EMAIL_USER, EMAIL_PASS)
            alertas["ABEV3_LOW"] = True
        if abev3 >= 14.74:
            alertas["ABEV3_LOW"] = False

if __name__ == "__main__":
    monitor()
