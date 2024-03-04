# Act 3 of ProjectFinny.
class Act3:
    def __init__(self, user_name, tested_finny):
        self.user_name = user_name
        self.tested_finny = tested_finny
        self.current_location = 'start'
        self.decisions = {}

        self.act3_map = {
            'start': {
                'Description': "After discovering Finny 2.0's invasive capabilities, you're faced with a critical choice.",
                'Options': {
                    'confront': "Confront Victoria and demand changes.",
                    'expose': "Expose Finny's invasive nature to the public.",
                    'collaborate': "Work with FinnCorp to responsibly fix Finny's issues."
                }
            },
            'confront': {
                'Description': "You decide to confront Victoria, demanding an explanation and immediate changes to Finny's programming.",
                'Options': {
                    'accept': "Victoria agrees to your demands, promising reforms.",
                    'reject': "Victoria dismisses your concerns, threatening your job."
                }
            },
            'expose': {
                'Description': "You choose to go public with your findings, risking your career to expose Finny's true nature.",
                'Options': {
                    'praised': "The public outcry leads to positive change; your actions are praised.",
                    'ostracized': "You're ostracized by FinnCorp and struggle to find work."
                }
            },
            'collaborate': {
                'Description': "Opting for a more diplomatic approach, you propose working together with FinnCorp to address Finny's issues.",
                'Options': {
                    'success': "Your collaboration leads to significant improvements in Finny, ensuring user privacy and safety.",
                    'failure': "Efforts stall due to corporate resistance; little changes."
                }
            },
            'accept': {
                'Description': "Victoria's acceptance marks the beginning of a new era for FinnCorp, with you leading the charge towards ethical AI.",
                'Options': {}
            },
            'reject': {
                'Description': "Facing rejection, you resign and start a movement advocating for digital privacy rights, inspiring many.",
                'Options': {}
            },
            'praised': {
                'Description': "Your courage to expose the truth brings widespread acclaim and sparks a global conversation on AI ethics.",
                'Options': {}
            },
            'ostracized': {
                'Description': "Despite the personal cost, your actions plant the seeds for future change, though you watch from the sidelines.",
                'Options': {}
            },
            'success': {
                'Description': "Your successful collaboration with FinnCorp sets a new standard for AI, blending innovation with integrity.",
                'Options': {}
            },
            'failure': {
                'Description': "Though your efforts don't yield the hoped-for changes, they ignite a debate on corporate responsibility in tech.",
                'Options': {}
            }
        }

    def start(self):
        while self.current_location != 'end':
            location_info = self.act3_map[self.current_location]
            print(location_info['Description'])
            options = location_info['Options']
            if not options:
                self.current_location = 'end'  # Ends the narrative loop
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
    user_name = input("Enter your name: ")
    tested_finny = input("Did you choose to test Finny? (yes/no): ").strip().lower() == 'yes'
    act3 = Act3(user_name, tested_finny)
    act3.start()
