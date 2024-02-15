# This is the main code for Project Finny
# Git commands to upload: git push
# Git command to download most recent code: git pull

def game():
    print('Thank you for showing interest in applying at FinnCorp, please start by answering some questions for us!')

    # Fortmat name code
    def format_name(name1):
        formatted_name = name1.strip().title()
        return formatted_name

    # Getting the players name for use
    unformatted_name = input('Please start off by telling us... what is your name? ')

    # Formatted
    name = format_name(unformatted_name)
    print('We are so pleased to meet you!')

    print('')

    # More questions, make it feel like a job application
    location = input('Where are you from, ' + name + '? ')
    print(location + '...')
    print('Sounds lovely!')

    print('')

    # Ask user what they fear
    def get_fear():
        options = ['- Being alone','- Dying with regret','- Losing the people I love','- Nothing']
        options_text = "\n".join(options)
        while True:
            fear = input('What do you fear the most? \n{}\nYour Choice: '.format(options_text))
            fear_lower = fear.lower()
            matching_options = [opt for opt in options if opt[2:].lower() in fear.lower()]
            if matching_options:
                chosen_option = matching_options[0][2:]
                if chosen_option == 'Being alone':
                    response = "Being alone... interesting."
                elif chosen_option == 'Dying with regret':
                    response = 'Dying with regret... specific.'
                elif chosen_option == 'Losing the people I love':
                    response = 'Losing the people you love... how human.'
                elif chosen_option == 'Nothing':
                    response = 'Nothing... that can change.'
                return chosen_option, response
            else:
                print('INVALID, ANSWER FROM THE OPTIONS')
    choice, response = get_fear()
    print(response)
    print()
    print('Thank you for answering!\nwe know it might be unorthodox, but these questions...\nthey show us who you are.')
    print('\nPlease allow us up to three business days to get back to you,\nAnd thank you for applying at FINNCORP.')



game()