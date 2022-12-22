import socket
import sys

OPTIONS = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
DEFAULT_SIZE = 256


def end_game(message):
    if message.endswith("You Lose!\n"):
        return True
    return False


def valid_option(option):
    if not option.isdigit():
        return False
    if 0 < int(option) <= len(OPTIONS):
        return True
    return False


def select_option():
    print("Please select you option:")
    for i, option in enumerate(OPTIONS):
        print(f'{i + 1}. {option}')
    while True:
        option = input('Option = ')
        if valid_option(option):
            return str(int(option) - 1)


def connection_error(server_message):
    return 'connection error: timed out' in server_message


def main():
    port = 10000
    host_ip = '127.0.0.1'
    try:
        connection = socket.create_connection((host_ip, port))
        connection.settimeout(1)
        while True:
            server_message = connection.recv(DEFAULT_SIZE).decode()
            print(server_message)
            if end_game(server_message) or connection_error(server_message):
                sys.exit(0)
            option = select_option()
            connection.send(option.encode())
    except socket.error as e:
        print("Socket connection error: " + str(e))


if __name__ == "__main__":
    main()
