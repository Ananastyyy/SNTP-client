import select
import socket

from request_handler import RequestHandler


# Считываем данные из конфигурационного файла, запускаем сервер и в бесконечном цикле
# принимаем запросы от клиента, при получении которых запускаем обработчик запроса
def run():
    server_params_dict = {}
    with open('config.txt') as file:
        for param_name, param_value in map(lambda line: line.split(':'), file.readlines()):
            server_params_dict[param_name] = int(param_value)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(('localhost', server_params_dict['port']))
        print("Сервер запущен")
        while True:
            read_list, _, _ = select.select([sock], [], [], 1)
            if read_list:
                handler = RequestHandler(sock, server_params_dict['offset'])
                handler.start()
