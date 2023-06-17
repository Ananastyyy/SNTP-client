import socket
import struct
import time

NTP_SERVER = 'localhost'
TIME1970 = 2208988800
PORT = 123


# Клиент подключается к серверу и получает от него результат
def SNTP_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'
    client.sendto(data.encode('utf-8'), (NTP_SERVER, PORT))
    data, address = client.recvfrom(1024)
    t = struct.unpack('!12I', data)[10] - TIME1970
    print('\nTime = %s' % time.ctime(t))


if __name__ == '__main__':
    try:
        SNTP_client()
    except PermissionError:
        pass
