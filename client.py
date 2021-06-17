import socket


class Exit(Exception):
    pass


sock = socket.socket()
server = "localhost"
port = input('Enter port: ')
print()

try:
    sock.connect((server, int(port)))

    print(f"Server: {server}/{port}")


except ConnectionRefusedError as e:
    print(f"ERROR {e}")
    exit()

while True:

    try:
        data = sock.recv(1024).decode("utf8")

        if data.lower() == 'stop':
            raise Exception("You disconnected.")

    except ConnectionResetError as e:
        print(f"ERROR: {e}")
        sock.close()
        exit()

    except Exception as e:
        print(f"ERROR: {e}")
        sock.close()
        exit()

    print(f"\nServer: {data}")

    try:
        text = input("\n Message: ")
    except KeyboardInterrupt as e:
        print(f"ERROR: {e}")
        exit()

    try:
        result = sock.send(text.encode())
        if not result:
            raise Exception("Nthg to send")
    except Exception as e:
        print(f"ERROR: {e}")
        exit()

sock.close()
