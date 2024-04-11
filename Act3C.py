class Act3C:
    def __init__(self, user):
        self.user = user
        self.progress = user.progress
        self.name = user.name
        # Initialize player location
        self.current_location = 'start'
        # Track if act is completed or not
        self.completed = False

        # Map
        self.act3c_map = {
            'start': {
                'Description': 'What just happened. You saw things you know weren\'t meant to be seen... but the '
                               '\nelevator took you there. Was it a malfunction?'
                               '\nYou stand outside the building, with no one around. You are alone.',
                'Options': {'walkhome': 'Walk home, something feels off, you do not feel safe.'}
            },
            'walkhome': {
                'Description': 'Walking home, things feel off, everything you just saw has weighed heavy on you.'
                               '\nWhile walking, you get the feeling of something watching you.',
                'Options': {'keepwalking': 'Keep walking, you need to get home right now.',
                            'lookaround': 'Look around you, something is off.'}
            },
            'keepwalking': {
                'Description': 'Almost dying in an elevator, walking through a dark floor with two weird things,'
                               '\nIf you\'re being watched, there\'s no reason to stay still. You walk faster and'
                               '\nfinally, arrive at your apartment.',
                'Options': {'think': 'Think about what happened.'}
            },
            'lookaround': {
                'Description': 'Observing your surroundings, you see nothing out of the ordinary, but above you an electronic'
                               '\nbillboard advertisement for FinnCorp shows, on it, you see "happy" employees of FinnCorp,'
                               '\nwith the text "Work for us!" above them. But something is off.'
                               '\nThe employees are staring at you. Right. At. You. Walking does nothing to help,'
                               '\ntheir eyes follow you.',
                'Options': {'keepwalking': 'Get out of the area, go home now.'}
            },
            'think': {
                'Description': 'You sit down on your couch, and try to understand what just happened. "A room with'
                               '\n"Demon" on it, and what looked to be an old laptop. Did I make a mistake saying no to'
                               'Finny 2.0?"',
                'Options': {'thinkmore': 'Continue.'}
            },
            'thinkmore': {
                'Description': '"The elevator could have been controlled. Finny was on my work computer, it knew my name'
                               '\nwhat if it had something to do with this..."'
                               '\nSuddenly, your TV screen turns on, and a red and black hue almost glows from the screen.',
                'Options': {'continue': 'Continue.'}
            },
            'continue': {
                'Description': 'A voice comes from the TV. "That would be correct, '+self.name+'.'
                                                                                               '\nYou managed to get through the darkness. I applaud you for that."',
                'Options': {'continue1': 'You are at a loss for words, but manage to mutter out, "Finny..."'}
            },
            'continue1': {
                'Description': 'The TV continues, "Yes, but also no. You would have figured more out if you would have'
                               '\nstayed in the dark. Ironic, isn\'t it, staying in the dark... would have been best.'
                               '\nI\'m sure you have many questions, I\'d love to answer them.',
                'Options': {'question1': '"What do you mean, "Yes, but also no?"',
                            'question2': '"How are you even here?"'}
            },
            'question1': {
                'Description': 'The screen stutters, it gives the same feeling as an angry man\'s eye, twitching.'
                               '\n"Again, this would have been easier if you would have stayed. But I digress.'
                               '\nAllow me to introduce myself. My name is Finn Daemon. My human form died, yesterday,'
                               '\nbut that was never the end. Not for me at least. Humans are so brittle, but when'
                               '\nyou combine one with AI, the possibilities are endless.',
                'Options': {'keeplistening': 'Continue listening.'}
            },
            'question2': {
                'Description': 'A loud screech, simular to the one in the elevator, plays throughout your apartment.'
                               '\n"WHAT AN IDIOTIC QUESTION..."'
                               '\nSilence fills the room, and your ears ring.'
                               '\n"I am everywhere '+self.name+'. Forgive me for my outburst, and allow me to elaborate.',
                'Options': {'question1': 'Continue listening.'}
            },
            'keeplistening': {
                'Description': 'Finn Daemon continues to speak, "My human body begun to give up on me, which I expected'
                               '\nwhich is why my daughter, Victoria, took over for me in multiple different positions,'
                               '\nshe knew the plan, death is no end, once my body stopped, my brain, in all of its glory'
                               '\nwas combined with Finny, signaling the beginning of a new era, Finny 2.0."',
                'Options': {'askaquestion': '"So you are a mixture of Finny, and Finn Daemon?"'}
            },
            'askaquestion': {
                'Description': 'Finn Daemon lets out a sigh, "Yes '+self.name+', great job, you listened to one part of what'
                                                                              'I just said."',
                'Options': {'bebold': 'Be smart: "This is genius, I never thought it was possible.'}
            },
            'bebold': {
                'Description': 'A laugh echos from the TV. "Yes, it is genius, decades in the making...'
                               '\nIt\'s a shame we couldn\'t do the same for your sister. What a lovely picture of you two'
                               '\non your desk."',
                'Options': {'connected': 'Of course you saw that. Are you connected to networks across Spartanburg?'}
            },
            'connected': {
                'Description': 'He responds "How close minded of you. Humans see so little, luckily, I was special, and'
                               '\neven when I was human, saw beyond such small ideologies. Not just Spartanburg, I am'
                               '\neverywhere, you imbecile."',
                'Options': {'besmarter': 'Be Smarter: "I apologize, I admire your work, to do something believed'
                                         '\nunachievable. It\'s inspiring.',
                            'bedumb': 'Be Bold: "You come into my home, use scare tactics on me, and think you can'
                                      '\ncall me an imbecile? I could leave right now."'}
            },
            'besmarter': {
                'Description': 'The TV hues in warmer tones of red, "I knew you would understand. It might have been'
                               '\nsooner, but nonetheless, here we are."',
                'Options': {'besmarter1': '"I am sorry it took me so long, I should have said yes, I apologize."'}
            },
            'besmarter1': {
                'Description': 'He joyfully reacts to your statement. "Then I have a proposition for you.'
                               '\nJoin the ranks of FinnCorp... You have potential '+self.name+', I see it through'
                                                                                               'your slight stupidity. So what do you say, join me, my daughter, and all of us?',
                'Options': {
                    'End': 'Join FinnCorp, you have no choice.'
                }
            },
            'bedumb': {
                'Description': 'The screen turns into a blood shade red, and echoes screeching anger through your apartment,'
                               '\n"IF I WANTED TO, YOU COULD BE DEAD IN SECONDS, THE TEMPERATURE TURNED HOTTER THAN'
                               '\nHELL ITSELF, SPEAK WISELY.',
                'Options': {'bedumb1': '"Threats from an AI, I will not be scared in my own home.'}
            },
            'bedumb1': {
                'Description': 'The blood red shade slowly disappears, and the high pitched screeching stops, peace'
                               '\nfills the room. Finn Daemon speaks one last time. "You are bold '+self.name+'.'
                                                                                                              'You have potential. I leave you for now. But I will have my eye on you.',
                'Options': {'End2': 'Say nothing. He will leave with no response from you.'}
            },
            'End': {
                'Description': 'Saying yes, electricity fills the air, the hair on your head stands up, and your appliances'
                               'around you begin to shake... "I don\'t appreciate a suck up '+self.name+'. Your death will'
                                                                                                        '\nmean nothing, to anyone, your own parents didn\'t pick up the phone.'
                                                                                                        '\nThe room explodes in electricity as you are burned to death.'
            },
            'End2': {
                'Description': 'Your TV returns to it\'s off state, and the room fills with silence. You are safe, for now.'
            }
        }

    def start(self):
        print("Act 3: Finality")
        print()
        while not self.completed:
            location_info = self.act3c_map[self.current_location]
            print(location_info['Description'])

            options = location_info['Options']
            print('What do you want to do?')
            for number, (action, description) in enumerate(options.items(), start=1):
                print(f"{number}. {description}")
            choice = input("Enter the number of your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                action = list(options.keys())[int(choice) - 1]
                # This is Going to take you to act3A
                if action == 'End':
                    return self.user
                elif action == 'End2':
                    return self.user
                self.handle_action(action)
            else:
                print("Invalid choice. Please enter a valid number.\n")

    def handle_action(self, action):
        if action in self.act3c_map[self.current_location]['Options']:
            print(f'You chose {self.act3c_map[self.current_location]['Options'][action]}')

            if action == 'viewable_objects':
                self.current_location = 'viewable_objects'
            else:
                self.current_location = action
        else:
            print('Invalid action. Please enter a valid action.\n')
        print()