class Act3B:

    def __init__(self, user):
        self.user = user
        self.progress = user.progress
        self.name = user.name
        # Initialize player location
        self.current_location = 'start'
        # Track if act is completed or not
        self.completed = False
        self.act3b_map = {
            'start': {
                'Description': "You wake up disoriented, finding yourself in a stark interrogation room.",
                'Options': {'observe_surroundings': "Observe your surroundings.",
                            'question_presence': "Question why you're here."}
            },
            'observe_surroundings': {
                'Description': "The room is dimly lit, with a two-way mirror on one wall and a table and chair in the "
                               "center.",
                'Options': {'sit_down': "Sit down and wait for someone to arrive.",
                            'inspect_mirror': "Inspect the two-way mirror."}
            },
            'sit_down': {
                'Description': "You sit down, preparing yourself for whatever is to come.",
                'Options': {'wait': "Wait for someone to enter the room."}
            },
            'wait': {
                'Description': "After a few tense moments, the door opens, and two FBI agents enter the room.",
                'Options': {'stay_calm': "Stay calm and cooperate.",
                            'demand_answers': "Demand to know why you're being detained."}
            },
            'stay_calm': {
                'Description': "You stay calm and cooperate with the FBI agents, hoping to learn more about your "
                               "situation.",
                'Options': {'acknowledge_end': "Acknowledge the end of your journey."}
            },
            'demand_answers': {
                'Description': "You demand answers from the FBI agents, refusing to cooperate until they provide an "
                               "explanation.",
                'Options': {'acknowledge_end': "Acknowledge the end of your journey."}
            },
            'inspect_mirror': {
                'Description': "You approach the two-way mirror and notice a faint reflection of someone observing "
                               "you from the other side.",
                'Options': {'acknowledge_end': "Acknowledge the end of your journey."}
            },
            'question_presence': {
                'Description': "You question the presence of the FBI agents and demand to know why you've been "
                               "detained. They tell you that you know exactly why you are here.",
                'Options': {'demand_answers': "Demand to know why you're being detained."}
            },
            'acknowledge_end': {
                'Description': "You acknowledge the end of your journey, whether with acceptance or resistance, "
                               "as you face the consequences of your actions.",
                'Options': {}
            }
        }

    def start(self):
        print("Act 3: Finny and me")
        print()
        while not self.completed:
            location_info = self.act3b_map[self.current_location]
            print(location_info['Description'])

            options = location_info['Options']
            print('What do you want to do?')
            for number, (action, description) in enumerate(options.items(), start=1):
                print(f"{number}. {description}")
            choice = input("Enter the number of your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                action = list(options.keys())[int(choice) - 1]
                # This is Going to take you to act3A
                if action == 'acknowledge_end':
                    # game over
                    return self.user
                self.handle_action(action)
            else:
                print("Invalid choice. Please enter a valid number.\n")

    def handle_action(self, action):
        if action in self.act3b_map[self.current_location]['Options']:
            print(f'You chose {self.act3b_map[self.current_location]['Options'][action]}')

            if action == 'viewable_objects':
                self.current_location = 'viewable_objects'
            else:
                self.current_location = action
        else:
            print('Invalid action. Please enter a valid action.\n')
        print()
