# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        # Проверяем, какой URL был запрошен
        if self.path == "/":
            # Если запрошен корневой URL, отправляем страницу "Контакты"
            self.send_response(200) # Отправка кода ответа
            self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
            self.end_headers() # Завершение формирования заголовков ответа
            with open("../html/contacts.html", "r") as f: # Читаем содержимое HTML-файла с контактами
                html_content = f.read()
            # response = requests.get('https://github.com/olegminntimer/basics_of_layout/blam/feature-1/html/contacts.html')
            # html_content = response.text
            # print(html_content)
            self.wfile.write(bytes(html_content, "utf-8")) # Тело ответа
        else:
            # Если запрошен другой URL, отправляем 404 Not Found
            self.send_response(404) # Отправка кода ответа
            self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
            self.end_headers() # Завершение формирования заголовков ответа
            self.wfile.write(bytes("<h1>404 Not Found</h1>", "utf-8")) # Тело ответа

if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
