import wave_helper, copy, math

# MENU_CHOICES = {1: "Reverse",2: "negative", 3: "accelerate", 4: "slow",5: "volume up", 6:"volume down",7: "filter dim"}
INT_RANGE = range(-32768,32767)
MAX_VOLUME = 32767
SAMPLE_RATE = 2000
NOTE_DICT = {'A': 440,'B': 494,'C': 523,'D': 587,'E': 659,'F': 698,'G': 784, 'Q': 0}
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

def exit_menu(wav_list):
    output_file_name = input("How do you want to save this file?")
    check_problem = wave_helper.save_wave(wav_list[0],wav_list[1], output_file_name+".wav")
    if check_problem == -1:
        print("There was a problem")

    start_menu()

def read_notes_for_compose(filename='sample1.txt'):
        with open(filename, 'r') as notes_file:
            note_file = []
            for char in notes_file.read():
                    note_file.append(char)

        return note_file[::2]


def compose_melody(filename='sample1.txt'):
    """
    """
    notes_list = read_notes_for_compose(filename)
    composed_wav_file = [SAMPLE_RATE, []]

    for note in range(0, len(notes_list), 2):
        frequency_rate = NOTE_DICT[notes_list[note]]
        sample_for_sound = int(notes_list[note + 1]) * 125
        samples_per_cycle = SAMPLE_RATE / frequency_rate
        for i in range(sample_for_sound + 1):
            formula = int(MAX_VOLUME * math.sin((2 * math.pi * i) / samples_per_cycle))
            composed_wav_file[1].append([formula, formula])
    return composed_wav_file

def print_menu():
    """print menu infomation"""
    print("1. reverse audio")
    print("2.negative")
    print("3.accelerate")
    print("4.slow down")
    print("5.volume up")
    print("6.volume down")
    print("7.filter dim")
    print("8. return to main menu")

def get_file():
    """

    :param filename:
    :return:
    """
    file_name_input = "sample1.wav" # input("enter wav filename: ")
    return file_name_input


def reverse_audio(edited_wave_file):
    """
    1.
    """
    return [edited_wave_file[0], edited_wave_file[1][::-1]]


def negative_audio(edited_wave_file):
    """
    2.
    """
    for i in range(len(edited_wave_file[1])):
        value_1 = edited_wave_file[1][i][0]
        value_2 = edited_wave_file[1][i][1]
        if value_1 == -32768:
            value_1 += 1
        if value_2 == -32768:
            value_2 += 1
        edited_wave_file[1][i][0] = -1 * value_1
        edited_wave_file[1][i][1] = -1 * value_2
    return edited_wave_file
    # TODO test this function and check range limit


def accelerate_audio(edited_wave_file):
    """
    3.
    """
    accelerate_wave = [edited_wave_file[0],[]]
    for i in range(len(edited_wave_file[1])):
        if i % 2 == 0:
            accelerate_wave[1].append(edited_wave_file[1][i])

    return accelerate_wave


def slow_down_audio(edited_wave_file):
    """ 4. this function get wav list and add between each pair new item which is the average of them"""
    for i in range(0, len(edited_wave_file[1]) + 2, 2):
        avg1 = int((edited_wave_file[1][i][0] + edited_wave_file[1][i+1][0]) / 2)
        avg2 = int((edited_wave_file[1][i][1] + edited_wave_file[1][i+1][1]) / 2)
        edited_wave_file[1].insert(i + 1, [avg1, avg2])
    return edited_wave_file


def volume_up_audio(edited_wave_file):
    """
    5
    """
    for i in range(len(edited_wave_file[1])):
        if int(edited_wave_file[1][i][0] * 1.2) in INT_RANGE :
            edited_wave_file[1][i][0] = int(edited_wave_file[1][i][0] * 1.2)
        elif int(edited_wave_file[1][i][0] * 1.2) > max(INT_RANGE):
            edited_wave_file[1][i][0] = max(INT_RANGE) + 1
        else:
            edited_wave_file[1][i][0] = min(INT_RANGE)
            # TODO create function because you suck
        if int(edited_wave_file[1][i][1] * 1.2) in INT_RANGE :
            edited_wave_file[1][i][1] = int(edited_wave_file[1][i][1] *1.2)
        elif int(edited_wave_file[1][i][1] * 1.2) > max(INT_RANGE):
            edited_wave_file[1][i][1] = max(INT_RANGE) + 1
        else: edited_wave_file[1][i][1] = min(INT_RANGE)
    return edited_wave_file

def volume_down_audio(edited_wave_file):
    """
    6
    """
    for i in range(len(edited_wave_file[1])):
        edited_wave_file[1][i][0] = int(edited_wave_file[1][i][0] / 1.2)
        edited_wave_file[1][i][1] = int(edited_wave_file[1][i][1] / 1.2)

    return edited_wave_file

def dim_filter_audio(edited_wave_file):
    """
    7
    """
    dimmed_wav_list = [edited_wave_file[0],[]]
    for i in range(len(edited_wave_file[1])):
        if i == 0:
            left_avg = int((edited_wave_file[1][i][0] + edited_wave_file[1][i + 1][0]) / 2)
            right_avg = int((edited_wave_file[1][i][1] + edited_wave_file[1][i + 1][1]) / 2)
        elif i == len(edited_wave_file[1]) - 1:
            left_avg = int((edited_wave_file[1][i-1][0] + edited_wave_file[1][i][0]) / 2)
            right_avg = int((edited_wave_file[1][i-1][1] + edited_wave_file[1][i][1]) / 2)
        else:
            left_avg = int((edited_wave_file[1][i-1][0] + edited_wave_file[1][i][0]
                            + edited_wave_file[1][i + 1][0]) / 3)
            right_avg = int((edited_wave_file[1][i-1][1] + edited_wave_file[1][i][1]
                             + edited_wave_file[1][i + 1][1]) / 3)
            # TODO check why -3 // 2 = -2  (suppose to be -1)
        dimmed_wav_list[1].append([left_avg, right_avg])
    return dimmed_wav_list

def edit_wave_file():
    # get user input (1-7)
    wave_file_list = wave_helper.load_wave(get_file())
    edited_wave_file_list = copy.deepcopy(wave_file_list)
    # print(wave_file_list)
    print_menu()
    # edited_wave_file_list = [2000,[[1, 2], [2, 3], [3, 4], [4, 5]]]
    #edited_wave_file_list = [2000,[[-12,-12], [9,9], [20,-32768], [9, 9],[-12,-12],[2,2]]]
    user_choice = input("enter your choice: ")
    if user_choice == '8':
        return edited_wave_file_list

    while user_choice != '8':
        if user_choice == '1':
            print(edited_wave_file_list)
            print("______________________________________________________")
            edited_wave_file_list = reverse_audio(edited_wave_file_list)
            print(edited_wave_file_list)

        if user_choice == '2':
            print(edited_wave_file_list)
            print("______________________________________________________")
            edited_wave_file_list = negative_audio(edited_wave_file_list)
            print(edited_wave_file_list)

        if user_choice == '3':
            print(edited_wave_file_list)
            print("______________________________________________________")
            edited_wave_file_list = accelerate_audio(edited_wave_file_list)
            print(edited_wave_file_list)


        if user_choice == '4':
            print(edited_wave_file_list)
            print("______________________________________________________")
            edited_wave_file_list = slow_down_audio(edited_wave_file_list)
            print(edited_wave_file_list)

        if user_choice == '5':
            print(edited_wave_file_list)
            print("______________________________________________________")
            edited_wave_file_list = volume_up_audio(edited_wave_file_list)
            print(edited_wave_file_list)

        if user_choice == '6':
            print(edited_wave_file_list)
            print("______________________________________________________")
            edited_wave_file_list = volume_down_audio(edited_wave_file_list)
            print(edited_wave_file_list)

        if user_choice == '7':
            print(edited_wave_file_list)
            print("______________________________________________________")
            edited_wave_file_list = dim_filter_audio(edited_wave_file_list)
            print(edited_wave_file_list)
        user_choice = input("enter your choice: ")
    return exit_menu(edited_wave_file_list)



def main():
    # start_menu()
    #zubi(698, 16)
    #read_notes_for_compose()
    exit_menu(compose_melody())
if __name__ == '__main__':
    main()