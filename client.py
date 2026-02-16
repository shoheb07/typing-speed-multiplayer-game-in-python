import socket
import threading
import tkinter as tk
import time

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

start_time = None

def receive():
    global start_time

    while True:
        msg = client.recv(1024).decode()

        if not start_time:
            text_label.config(text=msg)
            start_time = time.time()
        else:
            result_label.config(text=msg)

def send():
    typed = entry.get()

    end = time.time()

    speed = len(typed.split()) / ((end - start_time) / 60)

    msg = f"Speed: {round(speed,2)} WPM"

    client.send(msg.encode())

root = tk.Tk()
root.title("Typing Speed Multiplayer")

text_label = tk.Label(root, text="Waiting...")
text_label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

btn = tk.Button(root, text="Submit", command=send)
btn.pack()

result_label = tk.Label(root, text="")
result_label.pack()

thread = threading.Thread(target=receive)
thread.start()

root.mainloop()
