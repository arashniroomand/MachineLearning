import shutil
from constant import MENU, OPTIONS
from utility import set_values

terminal_width = shutil.get_terminal_size().columns  # Get terminal width dynamically
def menu():
    show_menu = True
    while show_menu:
        print(MENU)
        print()
        print(OPTIONS)
        option = input("ENTER YOUR CHOICE: ".center(terminal_width))
        match option:
            case '1':
                show_menu = set_values('loss')
            case '2':
                show_menu = set_values('Gradient')
            case '3':  # Exit option
                print("Exiting...".center(terminal_width))
                break  # Exit the loop

menu()
