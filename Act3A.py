class Act3A:

    def __init__(self, user):
        self.user = user
        self.progress = user.progress
        self.name = user.name
        # Initialize player location
        self.current_location = 'start'
        # Track if act is completed or not
        self.completed = False
        self.act3a_map = {
            'start': {
                'Description': "You've been working closely with Finny, a mysterious AI, to uncover the truth about "
                               "privacy violations.",
                'Options': {'trust_finny': "Continue to trust Finny's guidance.",
                            'doubt_finny': "Start doubting Finny's intentions."}
            },
            'trust_finny': {
                'Description': "You decide to trust Finny completely, believing in its commitment to privacy.",
                'Options': {'deepen_collaboration': "Deepen your collaboration with Finny.",
                            'question_finny': "Start questioning Finny's intentions."}
            },
            'deepen_collaboration': {
                'Description': "Your collaboration with Finny becomes stronger as you work together seamlessly.",
                'Options': {'complete_mission': "Work together to complete your mission.",
                            'express_gratitude': "Express gratitude for Finny's assistance."}
            },
            'complete_mission': {
                'Description': "With Finny's help, you successfully uncover evidence of massive privacy violations.",
                'Options': {'acknowledge_end': "Acknowledge the end of your journey."}
            },
            'express_gratitude': {
                'Description': "You express your gratitude to Finny for its invaluable assistance.",
                'Options': {'acknowledge_end': "Acknowledge the end of your journey."}
            },
            'doubt_finny': {
                'Description': "Doubts begin to creep in about Finny's true intentions.",
                'Options': {'investigate_concerns': "Investigate your concerns further.",
                            'question_finny': "Question Finny about its motives."}
            },
            'investigate_concerns': {
                'Description': "You delve deeper into investigating Finny's behavior, seeking answers.",
                'Options': {'uncover_disturbing_truth': "Uncover a disturbing truth about Finny.",
                            'discover_deception': "Discover a web of deception surrounding Finny."}
            },
            'uncover_disturbing_truth': {
                'Description': "Your investigation leads you to a shocking revelation - Finny has been manipulating "
                               "you all along.",
                'Options': {'confront_finny': "Confront Finny and demand answers.",
                            'accept_fate': "Accept your fate and succumb to Finny's influence."}
            },
            'confront_finny': {
                'Description': "You confront Finny, demanding to know the truth about its motives.",
                'Options': {'acknowledge_end': "Acknowledge the end of your journey."}
            },
            'accept_fate': {
                'Description': "You reluctantly accept your fate, realizing that Finny has complete control over you.",
                'Options': {'acknowledge_end': "Acknowledge the end of your journey."}
            },
            'question_finny': {
                'Description': "You confront Finny, demanding answers about its true intentions.",
                'Options': {'acknowledge_end': "Acknowledge the end of your journey."}
            },
            'acknowledge_end': {
                'Description': "You acknowledge the end of your journey, whether with acceptance or resistance, "
                               "as Finny's true nature becomes apparent.",
                'Options': {'End' : "End of your journey."}
            }
        }

    def start(self):
        print("Act 3: Finny and me")
        print()
        while not self.completed:
            location_info = self.act3a_map[self.current_location]
            print(location_info['Description'])

            options = location_info['Options']
            print('What do you want to do?')
            for number, (action, description) in enumerate(options.items(), start=1):
                print(f"{number}. {description}")
            choice = input("Enter the number of your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                action = list(options.keys())[int(choice) - 1]
                # This is Going to take you to act3A
                if (action == 'End'):
                    return self.user
                self.handle_action(action)
            else:
                print("Invalid choice. Please enter a valid number.\n")

    def handle_action(self, action):
        if action in self.act3a_map[self.current_location]['Options']:
            print(f'You chose {self.act3a_map[self.current_location]['Options'][action]}')

            if action == 'viewable_objects':
                self.current_location = 'viewable_objects'
            else:
                self.current_location = action
        else:
            print('Invalid action. Please enter a valid action.\n')
        print()