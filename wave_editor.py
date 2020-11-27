import wave_helper

MENU_CHOICES = {1: "Reverse",2: "negative", 3: "accelerate", 4: "slow",5: "volume up", 6:"volume down",7: "filter dim"}
def start_menu():
    # menu:
    # 1. change wave file
    # 2.compose melody in the correct format
    # exit

    user_input = input("Hey sir, press 1 to edit wav. file, 2 to compose a melody"
                           "press 3 to exit moderfucker! ")
    while user_input != '3':

        if user_input == '1':
            edit_wave_file()
        elif user_input == '2':
            compose_melody()
        else:
            print("invalid input, please try again!")
        user_input = input("Hey sir, press 1 to edit wav. file, 2 to compose a melody"
                               "press 3 to exit moderfucker! ")


def compose_melody():
    pass

def print_menu():
    """print menu infomation"""
    print("1. reverse audio")
    print("2.negative")
    print("3.accelerate")
    print("4.slow down")
    print("5.volume up")
    print("6.volume down")
    print("7.filter dim")
def get_file():
    """

    :param filename:
    :return:
    """
    file_name_input = input("enter wav filename: ")
    return file_name_input

def edit_wave_file():
    # get user input (1-7)
    wave_file_list = wave_helper.load_wave(get_file())
    print(wave_file_list)
    print_menu()
    user_choice = input("")


    # 1. reverse
    pass

def main():
    start_menu()

if __name__ == '__main__':
    main()