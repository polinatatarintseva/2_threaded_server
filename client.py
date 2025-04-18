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
    # Создаем TCP-сокет
 

    server_address = ('localhost', 9090)
 

    # Задаем адрес и порт сервера

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
    try:
 

        sock.connect(server_address)
 

        # Пытаемся подключиться к серверу
 

    except ConnectionRefusedError:
 

        # Если сервер недоступен, выводим сообщение и завершаем работу
 

        print("Не удалось подключиться к серверу. Пожалуйста, убедитесь, что сервер работает и доступен.")
 

        return
 

    except socket.error as e:
 

        # Обработка других ошибок подключения
 

        print(f"Ошибка подключения к серверу: {e}")
 

        return


    # Закрываем соединение с сервером
sock.close()
    try:
 

        while True:
 

            # Бесконечный цикл для отправки сообщений на сервер
 

            msg = input("Введите сообщение для отправки (для выхода введите 'exit'): ")
 

            # Запрашиваем у пользователя сообщение для отправки
 

            if msg.lower() == 'exit':
 

                # Если пользователь ввел 'exit', выходим из цикла и завершаем работу
 

                break
 

            try:
 

                sock.send(msg.encode())
 

                # Отправляем сообщение на сервер, преобразовав его в байты
 

            except BrokenPipeError:
 

                # Если соединение с сервером было разорвано
 

                print("Соединение с сервером было потеряно.")
 

                break
 

            except socket.error as e:
 

                # Обработка других ошибок отправки данных
 

                print(f"Ошибка отправки данных серверу: {e}")
 

                break
 


 

            try:
 

                data = sock.recv(1024)
 

                # Получаем данные от сервера (ожидаем эхо нашего сообщения)
 

                if not data:
 

                    # Если данных нет, сервер закрыл соединение
 

                    print("Соединение с сервером было закрыто.")
 

                    break
 

                print("Получено от сервера:", data.decode())
 

                # Выводим полученное сообщение, декодируя его из байтов в строку
 

            except socket.error as e:
 

                # Обработка ошибок получения данных
 

                print(f"Ошибка получения данных от сервера: {e}")
 

                break
 

    finally:
 

        sock.close()
 

        # Закрываем соединение с сервером
print(data.decode())
if __name__ == "__main__":
 

    main()
