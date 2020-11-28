import wave_helper, copy, math

# MENU_CHOICES = {1: "Reverse",2: "negative", 3: "accelerate", 4: "slow",5: "volume up", 6:"volume down",7: "filter dim"}
INT_RANGE = range(-32768, 32767)
MIN_VOLUME = -32768
MAX_VOLUME = 32767
SAMPLE_RATE = 2000

NOTE_DICT = {'A': 440, 'B': 494, 'C': 523, 'D': 587, 'E': 659, 'F': 698, 'G': 784}
SILENCE = 'Q'


def start_menu():
    """ this function is the start menu of the program """

    print("Welcome! \n --press 1 for editing wav file \n --press 2 for composing a melody \n --press 3 to exit menu\n")
    user_input = input()
    keep_it_active = True
    while keep_it_active:
        if user_input == '1':
            editing_menu()
        elif user_input == '2':
            composed_file_input = input("Enter file name to compose: ")
            composed_file = compose_melody(composed_file_input)
            save_audio("banana",composed_file)
        elif user_input == '3':
            keep_it_active = False
        else:
            print("invalid input, please try again!")
        print(
            "Welcome! \n --press 1 for editing wav file \n --press 2 for composing a melody \n --press 3 to exit menu\n")
        user_input = input()


def print_menu():
    """print menu information"""
    print("Welcome to editing menu!")
    print("1. Reverse audio")
    print("2. Negative")
    print("3. Accelerate")
    print("4. Slow down")
    print("5. Volume up")
    print("6. Volume down")
    print("7. Low-Pass Filter")
    print("8. Return to main menu")
    print(" -- pick your choice: ")


def get_file():
    """
    this function gets return wav file according to user input
    """
    print("Enter filename to edit: (-1 to cancel) ")
    file_name_input = input()
    return file_name_input



def save_audio(filename ,wav_list):
    """
    """
    valid_file = False
    temp_file = filename
    while not valid_file:
        temp_file = input("invalid name. enter valid filename: ")
        if temp_file != "":
            valid_file = True
    result = wave_helper.save_wave(wav_list[0],wav_list[1],temp_file + ".wav")
    return result

def exit_menu(wav_list):
    print("How do you want to save this file? ")
    output_file_name = input()
    if save_audio(output_file_name,wav_list) == -1:
        print("There was a problem, action was'nt completed")
    else:
        print("Action completed \n hope you like it! \n --- returning to main menu ---")
    start_menu()


########################################
# ~~~~OPTION 2~~~EDITING MENU~~~~~~~####
########################################


def editing_menu(filename=-1, audio_data=-1):
    """
    """
    filename = get_file()
    wave_file_list = wave_helper.load_wave(filename)
    if wave_file_list == -1:
        print("----------------------")
        print("File is not supported!")
        print("----------------------")
        return -1
    audio_file_copy = copy.deepcopy(wave_file_list)
    print_menu()
    audio_file_copy = [SAMPLE_RATE, [[-32768, -32768], [0, 0], [32767, 32767]]]
    user_choice = input()
    keep_edit = True

    if user_choice == '8':
        return audio_file_copy

    while keep_edit:

        if user_choice == '1':
            audio_file_copy[1] = reverse_audio(audio_file_copy[1])

        elif user_choice == '2':
            audio_file_copy[1] = negative_audio(audio_file_copy[1])

        elif user_choice == '3':
            audio_file_copy[1] = accelerate_audio(audio_file_copy[1])

        elif user_choice == '4':
            audio_file_copy[1] = slow_down_audio(audio_file_copy[1])

        elif user_choice == '5':
            audio_file_copy[1] = volume_up_audio(audio_file_copy[1])

        elif user_choice == '6':
            audio_file_copy[1] = volume_down_audio(audio_file_copy[1])

        elif user_choice == '7':
            audio_file_copy[1] = dim_filter_audio(audio_file_copy[1])
        elif user_choice == '8':
            keep_edit = False
        else:
            print("-------------------------")
            print("Invalid input, try again!")
            print("-------------------------")
        print_menu()
        user_choice = input()
    save_audio(filename, audio_file_copy)
    return audio_file_copy


# function 1 of 7
def reverse_audio(edited_wave_file):
    """
    1.
    """
    return edited_wave_file[::-1]  # functi


# function 2 of 7
def negative_audio(audio_list):
    """
    2.
    """
    for i in range(len(audio_list)):
        value_1 = audio_list[i][0]
        value_2 = audio_list[i][1]
        if value_1 == MIN_VOLUME:
            value_1 += 1
        if value_2 == MIN_VOLUME:
            value_2 += 1
        audio_list[i][0] = -1 * value_1
        audio_list[i][1] = -1 * value_2
    return audio_list


# function 3 of 7
def accelerate_audio(edited_wave_file):
    """
    3.
    """
    accelerate_wave = list()
    for i in range(len(edited_wave_file)):
        if i % 2 == 0:
            accelerate_wave.append(edited_wave_file[i])

    return accelerate_wave


# function 4 of 7
def slow_down_audio(audio_list):
    """ 4. this function get wav list and add between each pair new item which is the average of them"""
    samples_len = len(audio_list)
    for i in range(1, 2 * samples_len - 1, 2):
        avg1 = int((audio_list[i - 1][0] + audio_list[i][0]) / 2)
        avg2 = int((audio_list[i - 1][1] + audio_list[i][1]) / 2)
        audio_list.insert(i, [avg1, avg2])
    return audio_list


# function 5 of 7
def volume_up_audio(audio_list):
    """
    5
    """
    for i in range(len(audio_list)):
        if len(audio_list[i]) >= 1:
            if int(audio_list[i][0] * 1.2) in INT_RANGE:
                audio_list[i][0] = int(audio_list[i][0] * 1.2)
            elif int(audio_list[i][0] * 1.2) > max(INT_RANGE):
                audio_list[i][0] = max(INT_RANGE) + 1
            else:
                audio_list[i][0] = min(INT_RANGE)
                # TODO create function because you suck
            if int(audio_list[i][1] * 1.2) in INT_RANGE:
                audio_list[i][1] = int(audio_list[i][1] * 1.2)
            elif int(audio_list[i][1] * 1.2) > max(INT_RANGE):
                audio_list[i][1] = max(INT_RANGE) + 1
            else:
                audio_list[i][1] = min(INT_RANGE)
    return audio_list


# function 6 of 7
def volume_down_audio(audio_list):
    """
    6
    """
    for i in range(len(audio_list)):
        if len(audio_list[i]) >= 1:
            audio_list[i][0] = int(audio_list[i][0] / 1.2)
            audio_list[i][1] = int(audio_list[i][1] / 1.2)

    return audio_list


# function 7 of 7
def dim_filter_audio(audio_list):
    """
    7
    """
    dimmed_wav_list = list()
    if len(audio_list) == 0 or len(audio_list) == 1:
        return audio_list
    for i in range(len(audio_list)):
        if i == 0:
            left_avg = int((audio_list[i][0] + audio_list[i + 1][0]) / 2)
            right_avg = int((audio_list[i][1] + audio_list[i + 1][1]) / 2)
        elif i == len(audio_list) - 1:
            left_avg = int((audio_list[i - 1][0] + audio_list[i][0]) / 2)
            right_avg = int((audio_list[i - 1][1] + audio_list[i][1]) / 2)
        else:
            left_avg = int((audio_list[i - 1][0] + audio_list[i][0]
                            + audio_list[i + 1][0]) / 3)
            right_avg = int((audio_list[i - 1][1] + audio_list[i][1]
                             + audio_list[i + 1][1]) / 3)
        dimmed_wav_list.append([left_avg, right_avg])
    return dimmed_wav_list


########################################
# ~~~~OPTION 2~~~COMPOSE MENU~~~~~~~####
########################################

def read_notes_for_compose(filename):
    """
    this function gets txt file, read it and converts the content into list
    """

    with open(filename, 'r') as notes_file:
        note_file = []
        for line in notes_file.readlines():
            note_file.extend(line.strip().split())
        return note_file


def compose_melody(filename):
    """
    """
    notes_list = read_notes_for_compose(filename)
    composed_audio_list = [SAMPLE_RATE, []]

    for note in range(0, len(notes_list), 2):
        if notes_list[note] != SILENCE:
            frequency_rate = NOTE_DICT[notes_list[note]]  # Note
            sample_for_sound = int(notes_list[note + 1]) * 125  # number
            samples_per_cycle = SAMPLE_RATE / frequency_rate
        elif notes_list[note] == SILENCE:
            samples_per_cycle = 0

        for i in range(sample_for_sound + 1):
            if samples_per_cycle == 0:
                composed_audio_list.append([0, 0])
            else:
                formula = int(MAX_VOLUME * math.sin((2 * math.pi * i) / samples_per_cycle))
                composed_audio_list[1].append([formula, formula])
    return composed_audio_list


if __name__ == '__main__':
    start_menu()
