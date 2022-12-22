import argparse
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
    """
    The server has two communication protocols
    By default is using TCP protocol -> see line 57, socket.SOCK_STREAM
    Alternatively, UDP protocol can be used by adding --udp option when
    running server.py -> see line 55, socket.SOCK_DGRAM
    """
    parser = argparse.ArgumentParser(
        prog='Python Project',
        description='Play a game of Rock-Paper-Scissors-Lizard-Spock')
    parser.add_argument('--udp', action='store_true')
    args = parser.parse_args()

    if args.udp:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    else:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP

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
