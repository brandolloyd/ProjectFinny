# Act 1 of Project Finny!
class Act1:
    def __init__(self):
        # Initialize player location
        self.player_location = None
        # Initialize player inventory
        self.player_inventory = []
        # Track if act is completed or not
        self.completed = False

        # Map
        self.act1_map = {
            'apartment': {
                'Description': 'You wake up in your apartment, it is cold, lifeless, and YOU are somehow still tired.',
                'Options': {'viewable_objects': 'View your room.',
                            'bathroom': 'Freshen up in the bathroom.'}
            },
            'viewable_objects': {
                'Description': 'As you look through your room, you see two items, a rent bill, and a paycheck.',
                'Options': {'rent_bill': 'View your rent bill.',
                            'paycheck': 'View your recent paycheck.',
                            'bathroom': 'Freshen up in the bathroom.'},
            'rent_bill': {
                'Description': 'Things are getting really bad, I can barely afford to pay rent',
                'Options': {'paycheck': 'View your recent paycheck.',
                            'bathroom': 'Freshen up in the bathroom'}
            }
            },
            'bathroom': {
                'Description': 'As you walk towards the bathroom, the leak in the sink sings a sad song.',
                'Options': {'shower': 'Get ready for work.'}
            }
        }
        self.current_location = 'apartment'

    def start(self):
        print ("Act 1: Broke and Desperate")
        while not self.completed:
            location_info = self.act1_map[self.current_location]
            print(location_info['Description'])
            options = location_info['Options']
            print('What do you want to do?')
            for number, (action,description) in enumerate(options.items(), start=1):
                print(f"{number}. {description}")
            choice = input("Enter the number of your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                action = list(options.keys())[int(choice) - 1]
                self.handle_action(action)
            else:
                print ('Invalid choice. Please enter a valid number.')

    def handle_action(self, action):
        if action in self.act1_map[self.current_location]['Options']:
            print(f'You chose to {self.act1_map[self.current_location]['Options'][action]}')
            if action == 'viewable_objects':
                self.current_location = 'viewable_objects'
            elif action == 'bathroom':
                self.current_location = 'bathroom'
            else:
                print(self.act1_map[self.current_location]['Options'][action])
        else:
            print('Invalid action.')
