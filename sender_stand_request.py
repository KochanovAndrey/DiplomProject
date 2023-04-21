import configuration
import requests
import data

# запрос на создание нового заказа
def create_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставялем полный url
                         json=order_body,  # тут тело
                         headers=data.headers)   # а здесь заголовки

response = create_new_order(data.order_body) # переменная ответа
print(response.status_code)
print(response.json())

#  запоминаем номер заказа
def get_new_order_track():
    response = create_new_order(data.order_body)
    return response.json()['track']

track = response.json()['track']  # присваиваем переменной полученное значение track

# запрос на получения заказа по его номеру.
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + str(track))

response = get_order_by_track(track) # переменная ответа
print(response.json())
