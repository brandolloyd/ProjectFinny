# This is the main code for Project Finny
# Git commands to upload: git push
# Git command to download most recent code: git pull
# Git fetch or merge for other commands

from Act1 import Act1
# This Object is the user.
class CreateUser:
    # Acquire users name and location
    def __init__(self):
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
    User = CreateUser()

    print('Thank you for answering!\nwe know it might be unorthodox, but these questions...\nthey show us who you are.')
    print('\nPlease allow us up to three business days to get back to you,\nAnd thank you for applying at FINNCORP.')
    print()
    act1_instance = Act1()
    act1_instance.start()
game()