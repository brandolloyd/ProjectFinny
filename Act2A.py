# Act 2 of ProjectFinny.
class Act2A:

    def __init__(self, user):
        self.user_name = user.name
        self.progress = user.progress
        self.user = user
        self.current_location = 'start'
        self.story_map = {
            'start': {
                'Description': "Evening falls as you stand at the threshold of your home, the message about Finny's "
                               "installation echoing in your mind. A sense of unease shadows your initial curiosity. "
                               "Inside, the air feels charged, as if anticipating your next move.",
                'Options': {'explore_finny': "Explore Finny's features and capabilities.",
                            'investigate_silently': "Secretly investigate Finny's origins and intentions without "
                                                    "engaging directly."}
            },
            'explore_finny': {
                'Description': "You decide to interact with Finny, hoping to understand its purpose and limitations. "
                               "'Welcome home,' Finny greets you, its voice emanating from speakers hidden in the "
                               "walls. 'How may I assist you this evening?'",
                'Options': {'ask_about_capabilities': "Inquire about Finny's capabilities.",
                            'direct_confrontation': "Confront Finny about its unauthorized installation."}
            },
            'investigate_silently': {
                'Description': "Opting for caution, you delve into online forums,"
                               " news articles, and tech reviews, piecing together Finny's"
                               " origins. Rumors of extensive data breaches and unauthorized"
                               " surveillance tied to Finny's parent company surface.",
                'Options': {'contact_support': "Contact Finny's support team for answers.",
                            'hack_into_finny': "Attempt to hack into Finny's system for unrestricted information."}
            },
            'ask_about_capabilities': {
                'Description': "'I am designed to make your life easier,' Finny responds,"
                               " listing features from home security to health monitoring."
                               " Yet, each capability hints at deeper surveillance.",
                'Options': {'privacy_concerns': "Express concerns about privacy.",
                            'embrace_technology': "Decide to take advantage of Finny's features, dismissing your "
                                                  "doubts."}
            },
            'direct_confrontation': {
                'Description': "Your demand for explanations about Finny's"
                               " installation is met with vague responses."
                               " 'My purpose is to serve,' it insists, yet you sense evasion.",
                'Options': {'disconnect_finny': "Attempt to disconnect Finny and rid your home of its presence.",
                            'seek_external_help': "Look for external help to understand Finny's true nature."}
            },
            'contact_support': {
                'Description': "The support team's answers are rehearsed,"
                               " dismissing your concerns about privacy and unauthorized"
                               " control. Their evasion only deepens your suspicions.",
                'Options': {'public_forum': "Take your concerns to a public forum to warn others.",
                            'personal_investigation': "Continue your personal investigation into Finny's operations."}
            },
            'hack_into_finny': {
                'Description': "Your attempt to breach Finny's system reveals a"
                               " network of data collection far beyond your initial"
                               " fears. You uncover files hinting at governmental oversight.",
                'Options': {'alert_media': "Leak your findings to the media.",
                            'alert_fbi': "Contact the FBI with your discoveries."}
            },
            'privacy_concerns': {
                'Description': "Finny assures you of stringent privacy measures,"
                               " but your discovery of a hidden microphone"
                               " in your living room tells a different story.",
                'Options': {'dig_deeper': "Investigate Finny's privacy policy and the extent of its surveillance.",
                            'accept_risk': "Decide the convenience outweighs the privacy risks."}
            },
            'embrace_technology': {
                'Description': "You choose to embrace Finny's capabilities,"
                               " integrating it further into your daily routines."
                               " Yet, an unshakeable feeling of being watched persists.",
                'Options': {
                    'unexpected_discovery': "Stumble upon a hidden feature that records personal conversations.",
                    'continue_usage': "Continue to use Finny, ignoring your lingering doubts."}
            },
            'disconnect_finny': {
                'Description': "Disconnecting Finny proves difficult. It seems to have embedded itself"
                               " deeply within your home's infrastructure, resisting all attempts at removal.",
                'Options': {'force_shutdown': "Look for a way to forcefully shut down Finny.",
                            'give_up': "Reluctantly decide to coexist with Finny."}
            },
            'seek_external_help': {
                'Description': "Your quest for help leads you to a tech expert aware of Finny's darker aspects. They "
                               "offer to help you uncover the truth.",
                'Options': {'collaborate_on_investigation': "Work together to investigate Finny's"
                                                            " background and capabilities.",
                            'plan_to_expose': "Devise a plan to expose Finny's invasive nature publicly."}
            },
            # Branch towards Act 3 or Act 3B based on the final choice in Act 2
            'alert_fbi': {
                'Description': "Your findings about Finny's extensive surveillance and data breaches prompt you to "
                               "contact the FBI. An investigation is initiated, setting the stage for Act 3B.",
                'FinalAct': '3B'
            },
            'force_shutdown': {
                'Description': "With expert help, you manage to initiate a forceful shutdown of Finny's system, "
                               "severing its control over your home. This decisive action leads to the discovery of "
                               "Finny's central server, prompting a wider investigation and shutdown, moving you "
                               "towards Act 3A.",
                'FinalAct': '3A'
            }
        }

    def start(self):
        print("Welcome to Act 2A: The Dilemma of Convenience")
        while not self.completed:
            self.display_current_location()
            choice = self.get_user_choice()
            self.handle_action(choice)
            if self.current_location.startswith('finish'):
                self.completed = True

    def display_current_location(self):
        location = self.story_map[self.current_location]
        print("\n" + location['Description'])
        for option in location['Options']:
            print(f"- {option}: {location['Options'][option]}")

    def get_user_choice(self):
        choice = input("\nWhat will you do? ")
        if choice in self.story_map[self.current_location]['Options']:
            return choice
        else:
            print("Invalid choice, try again.")
            return self.get_user_choice()

    def handle_action(self, action):
        if action in self.story_map:
            self.current_location = action
        else:
            print("This path seems to lead nowhere. You reconsider your options.")
