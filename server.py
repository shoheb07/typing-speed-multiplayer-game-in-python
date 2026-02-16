import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

clients = []

text = "Python is a powerful programming language"

def handle_client(conn, addr):
    print(f"Connected: {addr}")

    conn.send(text.encode())

    while True:
        try:
            data = conn.recv(1024).decode()

            if not data:
                break

            print(f"{addr}: {data}")

            broadcast(data, conn)

        except:
            break

    conn.close()
    clients.remove(conn)

def broadcast(msg, sender):
    for client in clients:
        if client != sender:
            client.send(msg.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server started...")

while True:
    conn, addr = server.accept()
    clients.append(conn)

    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
