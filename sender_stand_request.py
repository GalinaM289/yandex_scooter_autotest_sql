import configuration
import requests

# функция получения ответа на запрос по созданию заказа
def create_order (order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

# функция получения ответа на запрос на получение заказа по треку 
def get_order_info_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track_number))