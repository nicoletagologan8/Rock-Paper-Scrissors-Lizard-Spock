import socket

OPTIONS = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
DEFAULT_SIZE = 256


def main():
    port = 10000
    host_ip = '127.0.0.1'
    try:
        connection = socket.create_connection((host_ip, port))
        connection.settimeout(1)
        server_message = connection.recv(DEFAULT_SIZE).decode()
        print(server_message)
    except socket.error as e:
        print("Socket connection error: " + str(e))


if __name__ == "__main__":
    main()
