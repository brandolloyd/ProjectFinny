# This is the main code for Project Finny
# Git commands to upload: git push
# Git command to download most recent code: git pull




#This Object is the user.
class createUser():
    #aquire users name and location
    name = input('Please start off by telling us... what is your name ').strip().title()
    location = input('Where are you from, ' + name + '? ')
    print(location + '...')
    print('Sounds lovely!')
    #Aquire list of users fears.
    options = ['Being alone', 'Dying with regret', 'Losing the people I love', 'Nothing']
    optionsList = '\n'.join(options)
    while(True):
        fear = input('What is your greatest Fear\n' + format(optionsList) + '\n')
        if fear in options:
            break
        else:print('INVALID, ANSWER FROM THE OPTIONS')


def game():
    # User has Name, Location, and fear1
    User = createUser()

    print('Thank you for answering!\nwe know it might be unorthodox, but these questions...\nthey show us who you are.')
    print('\nPlease allow us up to three business days to get back to you,\nAnd thank you for applying at FINNCORP.')

game()