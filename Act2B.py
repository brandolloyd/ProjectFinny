# Act2B of Project Finny
class Act2B:
    def __init__(self, user):
        self.user = user
        self.progress = user.progress
        self.name = user.name
        self.current_location = 'start'
        self.completed = False
        self.act2b_map = {
            'start': {
                'Description': 'Victoria frowns in disappointment, "Did you just say... \'No\'?"',
                'Options': {
                    'apologize': '"I\'m sorry, Victoria, I have to go with my gut on this one,'
                                 '\nFinny 2.0 is still in beta, and I don\'t want to risk it."',
                    'dontapologize': '"Yes, I just said no. You just revealed Finny 2.0 to us,'
                                     '\naccepting the assistant so early would be a bad move.'}
            },
            'apologize': {
                'Description': '"I expected more from you ' + self.name + ', but nonetheless, it is your choice.'
                                                                          '\nYou may leave now.',
                'Options': {'leave': 'Leave the room.'}
            },
            'dontapologize': {
                'Description': 'Victoria looks at you with a sharp disgust, "How long have you worked for FinnCorp?'
                               '\nDo you not understand the importance of Finny 2.0?...'
                               '\nRegardless, it is... was, your choice. Get back to work."',
                'Options': {'leave': 'Leave the room.'}
            },
            'leave': {
                'Description': 'The tension in the room could be cut with a knife... you leave quickly and'
                               '\nget back to your desk.',
                'Options': {'desk': 'View the items on your desk.',
                            'ted': 'Ted is sitting at his desk, visibly excited, talk to him.'}
            },
            'desk': {
                'Description': 'The letter you saw before is now gone... on your desk, is your computer, your phone,'
                               '\nand a picture of you and your deceased sister...',
                'Options': {'computer': 'Try and do some work. You will not be able to view other items after this.',
                            'phone': 'Call your parents, personal calls aren\'t permitted, but maybe just this once.',
                            'sister': 'View the image of you and your sister.'}
            },
            'computer': {
                'Description': 'Turning on your computer, it boots up normally, but you see a new icon in the corner,'
                               '\na black circle, with a red hue in the middle... Finny. I guess saying no only means'
                               '\nno to taking Finny home.',
                'Options': {'clickfinny': 'Click on Finny. See if anything happens.',
                            'work': 'Ignore Finny, continue with the workday like normal.'}
            },
            'clickfinny': {
                'Description': 'Clicking on the icon, your computer darkens into a black and red design. Finny speaks.'
                               '\n"Hi '+ self.name + ', I see you found the new Finny software installed on your computer.'
                                                   '\nI\'m here to help you out with any work related issues you may have.'
                                                   '\nWith that in mind, what can I do for you?',
                'Options': {'clickfinny1': 'Question Finny: "I don\'t need any help, but why were you installed on my computer?"',
                            'clickfinny2': 'Close Finny: "Nothing, I don\'t need any help from a personal assistant."'}
            },
            'clickfinny1': {

            },
            'clickfinny2': {

            },
            'phone': {
                'Description': 'You pick up the phone and dial your parents phone number, but it goes to voicemail...'
                               '\ntypical. Choose a voicemail to leave.',
                'Options': {'voicemail1': 'Detailed: "Hey, I was hoping to get your advice on something. Finny 2.0 got announced'
                                          '\n at work today... they asked if I would test it out, and I said no. I\'m'
                                          '\nworried it could be dangerous? I just have this bad feeling. Call me back'
                                          '\nwhen you can. Love you guys."',
                            'voicemail2': 'Vague: "Call me back when you get the chance, I need your opinion on something."'}
            },
            'voicemail1': {

            },
            'voicemail2': {

            },
            'sister': {
                'Description': 'You pick up the picture of your sister. You and her were kids back then, things were'
                               '\nsimple back then, then her car accident happened.'
            },
            'ted': {
                'Description': 'Ted wastes no time bragging, "I said yes! Victoria was so glad to hear it,'
                               '\nand on top of that I got a bonus too! Me and Finny are gonna be good friends.'
                               '\nI\'m sure your\'re excited too! They\'re probably installing it in'
                               '\nour homes right now!"',
                'Options': {'isaidno': 'Tell the truth. "I said no Ted, Finny 2.0 just got revealed... '
                                       '\nVictoria is pretty mad."',
                            'ignorehim': 'Ignore him. "Yep, that\'s great, I need to get to work. We\'ll talk later."'}
            },
            'isaidno': {
                'Description': 'His eyes widen, "You said no to a personal assistant in your home AND a bonus?'
                               '\nI guess to each their own! I guess I\'ll keep you updated, maybe Victoria will let'
                               '\nyou say yes later on."',
                'Options': {'work': 'End the conversation: "Yeah, maybe. I should get to work."'}
            },
            'ignorehim': {
                'Description': 'Surprisingly, he picks up on the social queue, "To each their own, I'
                               '\nshould get to work anyways.',
                'work': 'I hope I didn\'t make a mistake, time to work.'
            },
            'work': {

            }
        }

    def start(self):
        print()
        print("Act 2: Choices and Mistakes")
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
