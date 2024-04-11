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
                'Description': 'Finny hears your voice, and takes a second to think before responding... '
                               '\n"I was installed on all company computers ' + self.name + ', it seems you may have'
                                                                                            '\ndiscovered me a bit early! From what I see, you\'re my '
                                                                                            'first official company user!"',
                'Options': {'clickfinny1response': "Okay that didn\'t answer my question, but thanks Finny. Goodbye."}
            },
            'clickfinny1response': {
                'Description': 'Finny closes, and your screen goes back to it\'s original look.',
                'Options': {'work': 'That was interesting, continue with the workday.'}
            },
            'clickfinny2': {
                'Description': 'Finny stays on your screen, longer than normal, and responds, "Everyone needs help from time to time,'
                               '\neven you, ' + self.name + ', I\'ll leave, but let me know if you need anything.',
                'Options': {'work': 'It knows my name... I should get to work.'}
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
                'Description': 'They never answer, I\'m on my own with this one.',
                'Options': {'computer': 'Might as well just work. View computer.',
                            'sister': 'View the image of you and your sister.'}
            },
            'voicemail2': {
                'Description': 'They never have time for me, might as well leave a short voicemail. Guess I\'m'
                               '\non my own here.',
                'Options': {'computer': 'Might as well just work. View computer.',
                            'sister': 'View the image of you and your sister.'}
            },
            'sister': {
                'Description': 'You pick up the picture of your sister. You and her were kids back then, things were'
                               '\nsimple back then, then her car accident happened. I miss her so much.',
                'Options': {'computer': 'No more feeling sorry, time to work. View computer.',
                            'phone': 'Pick up the phone, call your parents.'}
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
                'Options': {'desk': 'End the conversation and view your desk: "Yeah, maybe. I should get to work."'}
            },
            'ignorehim': {
                'Description': 'Surprisingly, he picks up on the social queue, "To each their own, I'
                               '\nshould get to work anyways.',
                'desk': 'I hope I didn\'t make a mistake, time to work. View your desk.'
            },
            'work': {
                'Description': 'The work day goes normal, Victoria seems to keep an eye on you the entire day.'
                               '\nWhich makes you work harder, no chance in disappointing her more.',
                'Options': {'headhome': 'Pack up your things and head home.'}
            },
            'headhome': {
                'Description': 'You have all your things, and enter the elevator. Maybe it\'s exhaustion,'
                               '\nbut you have this weird feeling you\'re being watched.',
                'Options': {'pressbutton': 'Press the button to the first floor.',
                            'lookaround': 'Look around you, something seems off.'}
            },
            'pressbutton': {
                'Description': 'Pressing the button, nothing seems to happen, the doors close, but the elevator'
                               '\nrefuses to move...'
                               '\nSuddenly, noise plays on the elevator speakers, a high pitch screetch, a horrifying sound,'
                               '\nand the elevator drops... gravity is your enemy.',
                'Options': {'panic': 'Panic, the elevator is malfunctioning and your death is inevitable.'}
            },
            'lookaround': {
                'Description': 'Looking around you, you notice the camera system eyeing you, a red eye seems to be'
                               '\nin the lens. A new design maybe? You take a step to the right, and the camera follows'
                               '\nyou...',
                'Options': {'pressbutton': 'Press the button for the first floor, something feels off, go home.'}
            },
            'panic': {
                'Description': 'The elevator speakers get louder and louder as the it plummets, until finally'
                               '\nit comes to a slow halt, and the speakers revert to peaceful music. Something is wrong.'
                               '\nThe doors open, and you find yourself on a floor with almost no lighting,'
                               '\na dark void fills the area in front of you.',
                'Options': {'explore': 'Leave the safety of the elevator, explore the dark floor.',
                            'tryagain': 'Try pressing the first floor button again.'}
            },
            'explore': {
                'Description': 'Stepping out of the elevator, your eyes ever so slightly adjust to this darkness,'
                               '\nand you are able to make out few things, a room to the right with "Demon" on it,'
                               '\nand a table to the left with a laptop on it.',
                'Options': {'nope': 'Look for a way out, something is wrong here.'}
            },
            'tryagain': {
                'Description': 'Pressing the button again, the elevator shuts off, your light is gone, darkness'
                               '\nenvelopes you.',
                'Options': {'explore': 'There is no safety anymore, leave the dark elevator for an even darker floor.'}
            },
            'nope': {
                'Description': 'Danger lurks on this floor, you can feel it, a door with "Demon" on it, and a single'
                               '\nlaptop... you need to find a way out.',
                'Options': {'exploremore': 'Look for an exit, you need to get out now.'}
            },
            'exploremore': {
                'Description': 'You continue to walk in the dark, ignoring the Demon door and laptop. After minutes of '
                               '\nwalking in the dark, you vaguely make out a dead exit sign above a door. You have'
                               '\nfound the exit.',
                'Options': {'finalchoice': 'Although you have found the exit, there is something off about this floor,'
                                           '\nand something inside you wants to explore what you saw...'}
            },
            'finalchoice': {
                'Description': 'THIS ACTION WILL HAVE CONSEQUENCES. CHOOSE WISELY.'
                               '\nWhat will you do?',
                'Options': {'finish3C': 'Escape to the light.',
                            'finish3D': 'Discover what lurks in the darkness.'}
            },
            'finish3C': {
                'Description': 'You escape through the exit and run home.'
            },
            'finish3D': {
                'Description': 'You embrace the dark and choose to discover it\'s secrets.'
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
                # Final choice
                if action == 'finish3C':
                    self.progress = 2.3
                    return self.user
                elif action == 'finish3D':
                    self.progress = 2.4
                    return self.user
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
