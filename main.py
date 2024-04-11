# This is the main code for Project Finny
# Git commands to upload: git push
# Git command to download most recent code: git pull
# Git fetch or merge for other commands

# Import Acts, player choice will decide which act they get
from Act1 import Act1   # Static beginning act, introduce world and situation
from Act2A import Act2A  # Say yes to Finny
from Act2B import Act2B  # Say no to Finny
from Act3A import Act3A
from Act3B import Act3B
from Act3C import Act3C
from Act3D import Act3D

# This Object is the user.
class CreateUser:
    # Acquire users name and location
    def __init__(self):
        self.progress = 0
        self.name = input('Please start off by telling us... what is your first name ').strip().title()
        self.location = input('Where are you from, ' + self.name + '? ').strip().title()
        print(self.location + '...')
        print('Sounds lovely!')
    # Acquire list of users fears.
        self.options = ['- Being alone', '- Dying with regret', '- Losing the people I love', '- Nothing']
        self.optionsList = '\n'.join(self.options)
        while True:
            fear = input('What is your greatest Fear\n' + format(self.optionsList) + '\n').strip().title()
            if fear.lower() in [option.lower().lstrip('- ') for option in self.options]:
                break
            else:
                print('INVALID, ANSWER FROM THE OPTIONS')

def game():
    # User has Name, Location, and fear
    user = CreateUser()

    print('Thank you for answering!')
    print('\nPlease allow us up to three business days to get back to you,\nAnd thank you for applying at FINNCORP.')
    print()
    #USE this to test the act
    user.progress = 0

    if user.progress == 0:
        user = Act1(user)
        user.start()
    # After Act 1 completes, final choice
    if user.progress == 1.1:
        user = Act2A(user)
        user.start()
    elif user.progress == 1.2:
        user = Act2B(user)
        user.start()
    elif user.progress == 2.1:
        user = Act3A(user)
        user.start()
    elif user.progress == 2.2:
        user = Act3B(user)
        user.start()
    elif user.progress == 2.3:
        user = Act3C(user)
        user.start()
    elif user.progress == 2.4:
        user = Act3D(user)
        user.start()
#

game()