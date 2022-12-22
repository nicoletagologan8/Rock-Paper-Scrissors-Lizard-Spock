import random
import socket
import threading

from src.option import Option

OPTIONS = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
DEFAULT_SIZE = 256


def generate_server_option():
    return random.randint(0, len(OPTIONS) - 1)


def game_result(client_message):
    server_option = Option(generate_server_option())
    client_option = Option(client_message)
    game_status, message = client_option.defeats(server_option)
    return game_status, message


def handle_game(client_socket):
    while True:
        try:
            client_message = client_socket.recv(DEFAULT_SIZE).decode()
            game_status, message = game_result(client_message)
            if game_status == 1:
                client_socket.send(f"{message}You Win!\n".encode())
            elif game_status == -1:
                client_socket.send(f"{message}Draw!\n".encode())
            elif game_status == 0:
                client_socket.send(f"{message}You Lose!\n".encode())
                break
        except Exception as _:
            client_socket.close()
            break

    client_socket.close()


def main():
    server_socket = socket.socket()
    host = '127.0.0.1'
    port = 10000
    server_socket.bind((host, port))
    server_socket.listen()
    while True:
        if len(threading.enumerate()) < 4:  # including main thread
            client, addr = server_socket.accept()
            print('Connected to ', addr)
            client.send(f'Hello new player\n'
                        f'Welcome to Rock-Paper-Scissors-Lizard-Spock\n'
                        .encode())
            game_thread = threading.Thread(target=handle_game, args=(client,))
            game_thread.start()
            print(f"Client count = {len(threading.enumerate()) - 1}")


if __name__ == "__main__":
    main()
