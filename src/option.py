OPTIONS = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


class Option:
    def __init__(self, option):
        self.option = int(option)

    def defeats(self, other_option):
        option = other_option.option
        message = f"You : {OPTIONS[self.option]}; Server : {OPTIONS[option]}\n"
        match self.option:
            # Rock
            case 0:
                if option in [2, 3]:
                    return 1, f'{message}{OPTIONS[self.option]} crushes {OPTIONS[option]}\n'
                elif option == 0:
                    return -1, f'{message}{OPTIONS[self.option]} <-> {OPTIONS[self.option]}\n'
                elif option == 1:
                    return 0, f'{message}{OPTIONS[self.option]} is covered by {OPTIONS[option]}\n'
                elif option == 4:
                    return 0, f'{message}{OPTIONS[self.option]} is vaporized by {OPTIONS[option]}\n'
            # Paper
            case 1:
                if option == 0:
                    return 1, f'{message}{OPTIONS[self.option]} covers {OPTIONS[option]}\n'
                elif option == 4:
                    return 1, f'{message}{OPTIONS[self.option]} disproves {OPTIONS[option]}\n'
                elif option == 1:
                    return -1, f'{message}{OPTIONS[self.option]} <-> {OPTIONS[self.option]}\n'
                elif option == 2:
                    return 0, f'{message}{OPTIONS[self.option]} is cut by {OPTIONS[option]}\n'
                elif option == 3:
                    return 0, f'{message}{OPTIONS[self.option]} is eaten by {OPTIONS[option]}\n'
            # Scissors
            case 2:
                if option == 1:
                    return 1, f'{message}{OPTIONS[self.option]} cuts {OPTIONS[option]}\n'
                elif option == 3:
                    return 1, f'{message}{OPTIONS[self.option]} decapitates {OPTIONS[option]}\n'
                elif option == 2:
                    return -1, f'{message}{OPTIONS[self.option]} <-> {OPTIONS[self.option]}\n'
                elif option == 0:
                    return 0, f'{message}{OPTIONS[self.option]} is crushed by {OPTIONS[option]}\n'
                elif option == 4:
                    return 0, f'{message}{OPTIONS[self.option]} is smashed by {OPTIONS[option]}\n'
            # Lizard
            case 3:
                if option == 1:
                    return 1, f'{message}{OPTIONS[self.option]} eats {OPTIONS[option]}\n'
                elif option == 4:
                    return 1, f'{message}{OPTIONS[self.option]} poisons {OPTIONS[option]}\n'
                elif option == 3:
                    return -1, f'{message}{OPTIONS[self.option]} <-> {OPTIONS[self.option]}\n'
                elif option == 0:
                    return 0, f'{message}{OPTIONS[self.option]} is crushed by {OPTIONS[option]}\n'
                elif option == 2:
                    return 0, f'{message}{OPTIONS[self.option]} is decapitated by {OPTIONS[option]}\n'
            # Spock
            case 4:
                if option == 0:
                    return 1, f'{message}{OPTIONS[self.option]} vaporizes {OPTIONS[option]}\n'
                if option == 2:
                    return 1, f'{message}{OPTIONS[self.option]} smashes {OPTIONS[option]}\n'
                elif option == 4:
                    return -1, f'{message}{OPTIONS[self.option]} <-> {OPTIONS[self.option]}\n'
                elif option == 1:
                    return 0, f'{message}{OPTIONS[self.option]} is disproved by {OPTIONS[option]}\n'
                elif option == 3:
                    return 0, f'{message}{OPTIONS[self.option]} is poisoned by {OPTIONS[option]}\n'
