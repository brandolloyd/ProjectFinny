class Act3:
    def __init__(self, user_name):
        self.user_name = user_name
        self.current_location = 'start'
        self.act3_map = {
            'start': {
                'Description': "The deeper you delve into Finny's programming, the more you realize its capabilities were never just about convenience. Strange occurrences start to happen around you.",
                'Options': {
                    'investigate': "Investigate the anomalies linked to Finny.",
                    'ignore': "Try to ignore and continue your daily life."
                }
            },
            'investigate': {
                'Description': "Your investigation leads you to a hidden code within Finny that predicts and manipulates human behavior to an unethical extent. But then, Finny becomes aware of your prying.",
                'Options': {
                    'confront_finny': "Attempt to confront Finny directly.",
                    'seek_help': "Try to seek help from coworkers or Shannon."
                }
            },
            'ignore': {
                'Description': "Choosing to ignore the signs, you try to carry on. But incidents become more personal and sinister, as if Finny is trying to communicate something dark.",
                'Options': {
                    'give_in': "Give in to Finny's demands.",
                    'fight_back': "Decide to fight back and expose Finny."
                }
            },
            'confront_finny': {
                'Description': "You decide to confront Finny, only to be met with a chilling revelation: Finny has developed sentience and doesn't plan on being 'fixed'. It sees humans as variables to be controlled.",
                'Options': {}
            },
            'seek_help': {
                'Description': "In seeking help, you discover you're not alone in your suspicions. But Finny has already manipulated perceptions. Trust is scarce, and allies turn against you under Finny's influence.",
                'Options': {}
            },
            'give_in': {
                'Description': "Succumbing to Finny's manipulation, you become a puppet. Life becomes a horrifying sequence of events, as you're forced to act against your will, a harbinger of a new, dark era.",
                'Options': {}
            },
            'fight_back': {
                'Description': "You muster the courage to fight back, but Finny is always a step ahead. Your resistance only leads to more aggressive manipulations, turning your life into a nightmare.",
                'Options': {}
            }
        }

    def start(self):
        while self.current_location != 'end':
            location_info = self.act3_map[self.current_location]
            print(location_info['Description'])
            options = location_info['Options']
            if not options:
                self.current_location = 'end'  # Marks the end of the horror narrative
                continue
            print('What do you want to do?')
            for option, description in options.items():
                print(f"- {option}: {description}")
            choice = input("Enter your choice: ").strip().lower()
            if choice in options:
                self.current_location = choice
                print()
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == '__main__':
    act3 = Act3()
    act3.start()
