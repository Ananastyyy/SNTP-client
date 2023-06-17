from threading import Thread

from server import SNTPServer

BUFFER_SIZE = 4096


# В отдельном потоке запускаем класс, обработывающий запрос
class RequestHandler(Thread):
    def __init__(self, socket, offset):
        super().__init__()
        self.socket = socket
        self.offset = offset

    # Принимаем запрос от клиента, отправляем на наш сервер данные для
    # его обработки и отправляем клиенту ответ
    def run(self):
        request_package, address = self.socket.recvfrom(BUFFER_SIZE)
        package = SNTPServer(request_package, self.offset).build_package()
        self.socket.sendto(package, address)
