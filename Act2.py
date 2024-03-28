# Act 2 of ProjectFinny.
class Act2A:
    def __init__(self, user_name):
        self.user_name = user_name
        self.current_location = 'start'
        self.act2a_map = {
            'start': {
                'Description': f"You made the right choice, {self.user_name}. We've already gone ahead and had your internet service provider install Finny into your home.",
                'Options': {'office': "Continue your shift.", 'home': "Head home after your shift."}
            },
            'office': {
                'Description': "Victoria stares at you, asking you to leave with her eyes. Mike boasts about his new Finny.",
                'Options': {'home': "Finish your shift and head home."}
            },
            'home': {
                'Description': "You walk home with a fast pace. It can be dangerous out here at night.",
                'Options': {'safe_home': "Walk forward towards your home. (safe)", 'alley': "Investigate the noise in the alley. (risky)"}
            },
            'alley': {
                'Description': "A rat jumps out, scaring you, but you notice graffiti that says 'Finny Kills' in red.",
                'Options': {'safe_home': "Walk out of the alley, walk home."}
            },
            'safe_home': {
                'Description': f"Finally, you get home, Finny greets you, 'Hello {self.user_name}! Glad to see you home safe!'",
                'Options': {'finny_interaction': "Respond to Finny.", 'ignore_finny': "Say nothing."}
            },
            'finny_interaction': {
                'Description': "Finny: 'Sorry if I seem a bit excited, I'm just happy to be here, is there anything I can do for you?'",
                'Options': {'finny_capabilities': '"What can you do?"', 'finny_nothing': '"Nothing, Finny, I\'m tired."'}
            },
            'finny_capabilities': {
                'Description': 'Finny: "The better question is ‘What can’t I do?’, I can do it all. I can preheat your oven, change the temperature, even send a text for you!"',
                'Options': {'end': "Consider Finny's capabilities."}
            },
            'finny_nothing': {
                'Description': 'Finny: "I fully understand, do you want me to play some calming music for you?"',
                'Options': {'end': "Decline and get ready for bed."}
            },
            'ignore_finny': {
                'Description': "Finny: 'I understand, I'm a new member of the household, I'll leave you alone for now.'",
                'Options': {'end': "Go about your evening in silence."}
            },
            'end': {
                'Description': "You decide to get some rest, contemplating the day's events and Finny's place in your home.",
                'Options': {}
            }
        }

    def start(self):
        while self.current_location != 'end':
            location_info = self.act2a_map[self.current_location]
            print(location_info['Description'])
            options = location_info['Options']
            if not options:
                break  # End the loop if there are no more options
            print('What do you want to do?')
            for number, (action, description) in enumerate(options.items(), start=1):
                print(f"{number}. {description}")
            choice = input("Enter the number of your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                action = list(options.keys())[int(choice) - 1]
                self.current_location = action
            else:
                print('Invalid choice. Please enter a valid number.\n')

if __name__ == '__main__':
    user_name = input("Enter your name: ")
    act2a = Act2A(user_name)
    act2a.start()

class Act2B:
    def __init__(self, user_name):
        self.user_name = user_name
        self.completed = False


