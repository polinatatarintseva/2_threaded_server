import socket
from time import sleep
import socket  # Модуль для работы с сокетами

sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.38.165.12', 9090))
def main():
 

    sock = socket.socket()
 

    # Создаем сокет (TCP по умолчанию)
 

    sock.connect(('localhost', 9090))
 

    # Подключаемся к серверу по адресу и порту
 

    # Если сервер находится на удаленной машине, замените 'localhost' на IP-адрес сервера
#msg = input()
msg = "Hi!"
sock.send(msg.encode())
    while True:
 

        # Бесконечный цикл для отправки сообщений на сервер
 

        msg = input("Введите сообщение для отправки (для выхода введите 'exit'): ")
 

        # Запрашиваем у пользователя сообщение для отправки
 

        if msg.lower() == 'exit':
 

            # Если пользователь ввел 'exit', выходим из цикла и завершаем работу
 

            break
 

        sock.send(msg.encode())
 

        # Отправляем сообщение на сервер, предварительно преобразовав его в байты
 

        data = sock.recv(1024)
 

        # Получаем данные от сервера (ожидаем эхо нашего сообщения)
 

        print("Получено от сервера:", data.decode())
 

        # Выводим полученное сообщение, декодируя его из байтов в строку

data = sock.recv(1024)
    sock.close()
 

    # Закрываем соединение с сервером
sock.close()

print(data.decode())
if __name__ == "__main__":
 

    main()
