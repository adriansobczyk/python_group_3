import requests

# r = requests.get('https://api.github.com/events')
# print(r.text[:300])


response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
exchange_rate = response.json()
print(exchange_rate)
