import requests

def get_global_crypto_data():
    url = "https://api.coingecko.com/api/v3/global"
    response = requests.get(url)
    if response.status_code == 200:
        res = response.json()
        data = {
            "active_cryptocurrencies": res["data"]['active_cryptocurrencies'],
            "market_cap_percentage": res["data"]['market_cap_percentage'],
            "market_cap_change_percentage_24h_usd": res["data"]["market_cap_change_percentage_24h_usd"]
        }
        return data
    else:
        return None


def get_crypto_market_data():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&price_change_percentage=24h,7d,30d&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        data.sort(key=lambda x: x['market_cap_rank'])
        return data
    else:
        return []
