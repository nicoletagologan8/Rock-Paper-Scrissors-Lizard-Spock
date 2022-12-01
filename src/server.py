import socket
import threading
import time

OPTIONS = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
DEFAULT_SIZE = 256
CLIENT_COUNT = 0


def handle_game(socket):
    global CLIENT_COUNT
    time.sleep(60)
    print("game over")
    CLIENT_COUNT -= 1


def main():
    server_socket = socket.socket()
    host = '127.0.0.1'
    port = 10000
    server_socket.bind((host, port))
    server_socket.listen()
    global CLIENT_COUNT
    while True:
        if CLIENT_COUNT < 3:
            client, addr = server_socket.accept()
            CLIENT_COUNT += 1
            print('Connected to ', addr)
            client.send(f'Hello new player {CLIENT_COUNT}'.encode())
            game_thread = threading.Thread(target=handle_game, args=(server_socket,))
            game_thread.start()
            client.close()


if __name__ == "__main__":
    main()
