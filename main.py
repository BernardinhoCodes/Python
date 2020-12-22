# Car_game by Bernardinho_codes


#Quick race
def quick_race():
    print("You starting the Quick Race Modus")
    first_command_race = input('Enter "HELP" to get the command: ')
    if first_command_race.upper() == "HELP":
        print(f'The command which you could type in are: ')


#Training session
def training_session():
    print("You starting the Training session\n")
    first_command_training = input('Enter "HELP" to get the command: ')
    if first_command_training.upper() == "HELP":
        print(f'The command which you could type in are: {Commands.keys()}')


# In-Command_play
def help_game():
    pass

def start():
   start_greetings= input("When You are ready, type 'Y: ")
   if start_greetings.upper() != 'Y':
       print("Please just type in 'Y'")
   else:
       print("Ready...\nSet....\nGOOOOoooooo....\nYou are driving now!")


def accelerate():
    pass

def stop():
    pass

def nitro():
    pass


Commands = {

    'Start': start,
    'Drive': accelerate,
    'Nitro': nitro,
    'Stop': stop,


}


if __name__ == '__main__':

    print("Welcome to Nascar_Reload!\n"
      "1 - Quick Race\n"
      "2 - Training\n")

    cargame_decision = input("> ")

    if cargame_decision == str("1"):
        quick_race()
    elif cargame_decision == str("2"):
        training_session()
    else:
        print("Please enter the number for 1 for Quick Race or 2 for Training modus")


