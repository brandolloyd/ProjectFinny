# Act2B of Project Finny
class Act2B:
    def __init__(self, user_name):
        self.user_name = user_name
        self.current_location = 'start'
        self.completed = False
        self.act2b_map = {
            'start': {
                'Description': 'Victoria frowns in disappointment, "Did you just say... \'No\'?"',
                'Options': {
                    'apoligize': '"I\'m sorry, Victoria, I have to go with my gut on this one,'
                                 '\nFinny 2.0 is still in beta, and I don\'t want to risk it.',
                    'dontapoligize': '"Yes, I just said no. You just revealed Finny 2.0 to us,'
                                     '\naccepting the assistant so early would be a bad move.'
                }
            },
            'apoligize': {
                'Description': '"I expected more from you '+self.user_name+', but nonetheless, it is your choice.'
                                                                           '\nYou may leave now.',
                'Options': {

                }
            }
        }
    def start(self):
        print("Act 2B: Poor Choices")
        print()
        while not self.completed:
            location_info = self.act2b_map[self.current_location]
            print(location_info['Description'])
            options = location_info['Options']
            print('What do you want to do?')
            for number, (action, description) in enumerate(options.items(), start=1):
                print(f"{number}. {description}")
            choice = input("Enter the number of your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                action = list(options.keys())[int(choice) - 1]
                self.handle_action(action)
            else:
                print("Invalid choice. Please enter a valid number.\n")

    def handle_action(self, action):
        if action in self.act2b_map[self.current_location]['Options']:
            print(f'You chose {self.act2b_map[self.current_location]['Options'][action]}')
            if action == 'viewable_objects':
                self.current_location = 'viewable_objects'
            else:
                self.current_location = action
        else:
            print('Invalid action. Please enter a valid action.\n')
        print()