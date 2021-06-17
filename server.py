import socket
from commands import System

system = System("")

# starting server
sock = socket.socket()
print('Server is starting.')

port = input('Enter port: ')
sock.bind(('', int(port)))

while True:

    # listening to the port
    sock.listen(1)
    print(f"Listening to the port ({port})")

    # client address
    conn = sock.accept()[0]

    # запрашиваем рабочую директорию
    print()
    message = "Enter your home directory"
    conn.send(message.encode())
    print(f"Sending data: {message}")

    # получаем команду с клиента
    while True:
        try:
            message = ""
            data = conn.recv(1024).decode("utf8")

        except ConnectionResetError as e:
            print(f"ERROR: {e}")
            exit()

        if data == "stop":
            print(f"Client disconnected")
            break

        elif system.path != "":
            message = system.main(data)

        if system.path == "":
            message = system.setPath(data)

        conn.send(message.encode())
        print(f"Sending data: {message}")
        
    if data == "stop":
        break

conn.close()
