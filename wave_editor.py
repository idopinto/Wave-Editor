import wave_helper, copy

# MENU_CHOICES = {1: "Reverse",2: "negative", 3: "accelerate", 4: "slow",5: "volume up", 6:"volume down",7: "filter dim"}
INT_RANGE = (-32768,32767)
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
    file_name_input = "sample1.wav" # input("enter wav filename: ")
    return file_name_input


def reverse_audio():
    pass


def negative_audio():
    pass


def accelerate_audio(edited_wave_file):
    for i in range(len(edited_wave_file[1])):
        if i % 2 != 0:
            edited_wave_file[1][i].reverse()

    return edited_wave_file


def slow_down_audio(edited_wave_file_list):
    pass


def volume_up_audio(edited_wave_file_list):
    pass


def volume_down_audio(edited_wave_file_list):
    pass


def dim_filter_audio(edited_wave_file_list):
    pass


def edit_wave_file():
    # get user input (1-7)
    wave_file_list = wave_helper.load_wave(get_file())
    edited_wave_file_list = copy.deepcopy(wave_file_list)
    # print(wave_file_list)
    print_menu()
    user_choice = input("enter your choice: ")
    if user_choice == 1:
        edited_wave_file_list = reverse_audio(edited_wave_file_list)
         
    if user_choice == 2:
        edited_wave_file_list = negative_audio(edited_wave_file_list)
              
    if user_choice == 3:
        edited_wave_file_list = accelerate_audio(edited_wave_file_list)
          
    if user_choice == 4:
        edited_wave_file_list = slow_down_audio(edited_wave_file_list)
        
    if user_choice == 5:
        edited_wave_file_list = volume_up_audio(edited_wave_file_list)
        
    if user_choice == 6:
        edited_wave_file =  volume_down_audio(edited_wave_file_list)
    
    if user_choice == 7:
        edited_wave_file = dim_filter_audio(edited_wave_file_list)




    # 1. reverse
    pass

def main():
    start_menu()

if __name__ == '__main__':
    main()
