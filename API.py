import requests
import json

url = "https://www.alphavantage.co/query?" \
      "function=TIME_SERIES_INTRADAY&" \
      "symbol=AAPL&interval=1min&" \
      "apikey=UXCBBJBFC42EVXDP"

time_series = "Time Series (1min)"
element = "4. close"  # Элемент который нам нужен
array = list()

try:
    # Получаем JSON
    json_data = requests.get(url).json()

    # Закидываем нужные элементы в массив
    for timeitem in json_data[time_series]:
        array.append(json_data[time_series][timeitem][element])

    # Выводим json
    print('{' + json.dumps(array) + '}')
except ConnectionError:
    print("Нет соединения с интернетом!")
