from http import client
import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))
while True:
    string = input("Enter String: ")
    server.send(bytes(string, "utf-8"))
    data = server.recv(1024)
    data = data.decode("utf-8")
    print(data)
    string1 = server.recv(1024)
    string1 = string1.decode("utf-8")
    print(string1)
    client.close()