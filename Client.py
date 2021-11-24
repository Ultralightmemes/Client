import socket
import json


class Client:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 3345
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))

    def create_connection_client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))

    def receive(self):
        buf = self.s.recv(1024).decode('utf-8')
        return buf

    def sending(self, buf):
        self.s.send((buf + "\n").encode('utf-8'))

    def connection_end(self):
        self.s.close()


if __name__ == '__main__':
    client = Client()
    client.sending("first")

    # text = client.receive()
    # parsed_data = json.loads(text)
    # print(text)

    login = {}
    login["login"] = "login"
    login["password"] = "password"
    print(login)
    data = json.dumps(login)
    client.sending(data)


