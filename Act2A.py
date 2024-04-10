# Act 2 of ProjectFinny.
class Act2A:

    def __init__(self, user):
        self.user = user
        self.progress = user.progress
        self.name = user.name
        # Initialize player location
        self.current_location = 'start'
        # Track if act is completed or not
        self.completed = False
        self.act2a_map = {
            'start': {
                'Description': "Unease grips you as the sun sets, reflecting your growing concern over Finny's "
                               "influence in your life. It's time to take a stand, for your privacy and for all Finny"
                               " users.",
                'Options': {
                    'deep_dive': "Investigate Finny's privacy policies and data usage.",
                    'community_action': "Reach out to the community and gather collective experiences."
                }
            },
            'deep_dive': {
                'Description': "Your investigation uncovers a myriad of privacy concerns, painting a worrying picture "
                               "of Finny's reach into personal lives.",
                'Options': {
                    'gather_evidence': "Compile evidence and prepare to expose Finny's privacy invasions.",
                    'seek_expert_opinion': "Consult with privacy experts to bolster your findings."
                }
            },
            'community_action': {
                'Description': "Engaging with the community, you find you're not alone in your concerns. Together, "
                               "you start a movement for change.",
                'Options': {
                    'organize_forum': "Organize a public forum to discuss Finny's impact.",
                    'launch_campaign': "Launch a social media campaign to raise awareness."
                }
            },
            'gather_evidence': {
                'Description': "Armed with compelling evidence, you're at a crossroads. How will you use this "
                               "information to make a difference?",
                'Options': {
                    'final_decision': "Decide your next step."
                }
            },
            'seek_expert_opinion': {
                'Description': "Experts confirm your fears, adding credibility to your cause. It's time to decide how "
                               "to leverage this expertise.",
                'Options': {
                    'final_decision': "Decide your next step."
                }
            },
            'organize_forum': {
                'Description': "The forum turns out to be a powerful gathering, sparking a unified call for action "
                               "against Finny's overreach.",
                'Options': {
                    'final_decision': "Decide your next step."
                }
            },
            'launch_campaign': {
                'Description': "Your campaign goes viral, drawing attention from all corners to Finny's questionable "
                               "practices.",
                'Options': {
                    'final_decision': "Decide your next step."
                }
            },
            'final_decision': {
                'Description': "With evidence in hand and a community at your back, you face a pivotal decision. Will "
                               "you seek to reform Finny from within or take your findings public to force change?",
                'Options': {
                    'finish3A': "Work with Finny for change from within, hoping to influence better privacy practices.",
                    'finish3B': "Expose Finny's practices publicly, aiming for regulatory intervention and public "
                                "pressure."
                }
            }
        }

    def start(self):
        print("Act 2: Decision Collision")
        print()
        while not self.completed:
            location_info = self.act2a_map[self.current_location]
            print(location_info['Description'])

            options = location_info['Options']
            print('What do you want to do?')
            for number, (action, description) in enumerate(options.items(), start=1):
                print(f"{number}. {description}")
            choice = input("Enter the number of your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                action = list(options.keys())[int(choice) - 1]
                # This is Going to take you to act3A
                if (action == 'finish3A'):
                    self.progress = 2.1
                    return self.user
                # This is Going to take you to act3B
                if (action == 'finish3B'):
                    self.progress = 2.2
                    return self.user
                self.handle_action(action)
            else:
                print("Invalid choice. Please enter a valid number.\n")

    def handle_action(self, action):
        if action in self.act2a_map[self.current_location]['Options']:
            print(f'You chose {self.act2a_map[self.current_location]['Options'][action]}')

            if action == 'viewable_objects':
                self.current_location = 'viewable_objects'
            else:
                self.current_location = action
        else:
            print('Invalid action. Please enter a valid action.\n')
        print()