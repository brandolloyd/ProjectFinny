# Act 1 of Project Finny!




class Act1:
    def __init__(self, user):
        self.user = user
        self.progress = user.progress
        self.name = user.name
        # Initialize player location
        self.current_location = 'apartment'
        # Track if act is completed or not
        self.completed = False

        # Map
        self.act1_map = {
            'apartment': {
                'Description': 'You wake up in your apartment, it is cold, lifeless, '
                               '\nand YOU are somehow still tired.',
                'Options': {'viewable_objects': 'View your room.',
                            'bathroom': 'Freshen up in the bathroom.'}
            },
            'viewable_objects': {
                'Description': 'As you look through your room, you see two items, a rent bill, and a paycheck.',
                'Options': {'rent_bill': 'View your rent bill.',
                            'paycheck': 'View your recent paycheck.',
                            'bathroom': 'Freshen up in the bathroom.'}
            },
            'rent_bill': {
                'Description': 'Things are getting really bad, I can barely afford to pay rent',
                'Options': {'paycheck': 'View your recent paycheck.',
                            'bathroom': 'Freshen up in the bathroom'}
            },
            'paycheck': {
                'Description': 'This last paycheck was barely enough to buy groceries, '
                               '\nit may be time to beg for a raise...',
                'Options': {'rent_bill': 'View your rent bill',
                            'bathroom': 'Freshen up in the bathroom'}
            },
            'bathroom': {
                'Description': 'As you walk towards the bathroom, the leak in the sink sings a sad song.',
                'Options': {'shower': 'Get ready for work.'}
            },
            'shower': {
                'Description': 'You get ready for the workday, putting on your "FINNCORP" outfit '
                               '\nand finally, you are ready exit your apartment',
                'Options': {'Talk': 'Talk to the locals outside their apartments.',
                            'leave': 'Walk to work.'}  # Skip neighbors, head to work part
                # Talking to neighbors portion, multiple different outcomes!

            },
            'Talk': {
                'Description': 'Walking outside your apartment complex, you see your neighboring tenants,'
                               '\nyou dont talk to them much, but they still smile at you when you walk'
                               '\npast, maybe you should try talking?',
                'Options': {'younger': 'Speak to the younger lady, she seems mad, but isn\'t'
                                       '\neveryone these days?',
                            'older': 'Speak to the older man, he seems to be more upbeat, wonder why?'}
            },
            'younger': {
                'Description': 'As you walk up to the younger lady, she almost seems to'
                               '\nignore you, before you clear your throat in front of her.'
                               '\nLooks like its up to you to start the conversation...',
                'Options': {'start': '"Hey there! How are you doing today?"',
                            'leave': 'It\'s not worth it, i\'m going to work'}  # Finish, head to work part
            },
            'start': {
                'Description': 'She looks up from her phone and smiles at you, but still seems to'
                               '\nbe mad... "Hi! I didn\'t see you there... you\'re ' + self.name + ', right?"',
                'Options': {'talkmore': '"Yeah! Just wanted to say good morning! I\'m actually on '
                                        '\nmy way to work right now, but good to see you!"',
                            'talkmore2': '"Sorry about that, figured I\'d talk to my neighbors finally'
                                         '\nI\'m usually in a rush to get to work every day"'}
            },
            'talkmore': {
                'Description': 'That was awkward, why am I so weird around people',
                'Options': {'older': 'Try talking to the older gentleman? Maybe that will go better',
                            'leave': 'I\'ll try talking to my neighbors another day, I should head to work'}
                # Finish, head to work part
            },
            'talkmore2': {
                'Description': '"That makes sense! Don\'t worry about it, I\'m the same way myself...'
                               '\nso where do you work ' + self.name + '?"',
                'Options': {'iworkat': '"I work at FinnCorp! I\'m a customer service rep there."'}
            },
            'iworkat': {
                'Description': '"Oh... you work there. Maybe you should go talk to my grandpa,'
                               '\nyou and your friends have been taking his money for years.'
                               '\npromising to install Finny into the apartment complex..."',
                'Options': {'imsorry': '"I\'m sorry, if it was up to me, everyone would have Finny."',
                            'notmyfault': '"I wouldn\'t say that\'s my fault... I just help people out'
                                          '\nwith their questions and problems."'}
            },
            'imsorry': {
                'Description': '"Well that\'s good to hear, sorry for lashing out, I have a strong hatred for'
                               'FinnCorp, nothing against you though. I should get going, have a good one."',
                'Options': {'older1': 'Maybe her grandpa might be a bit nicer',
                            'leave': 'Nope, I\'m just gonna head to work'}  # Finish, head to work part
            },
            'notmyfault': {
                'Description': '"Wow, seems like you all have that view point today, it was'
                               '\nhorrible talking to you, lets never do it again!"... she walks away.',
                'Options': {'older1': 'Ouch... her grandpa seems to still be happy, maybe '
                                      '\nI\'ll try being friendly with him',
                            'leave': 'That\'s enough social talk for my week, to work I go.'}
                # Finish, head to work part
            },
            'older': {
                'Description': 'You walk up to the older gentleman. He smiles at you'
                               '\nlike an old friend. "Hey there ' + self.name + '!"',
                'Options': {'olderTalk': '"Hi! How\'s your morning going so far sir?"',
                            'olderTalk2': '"Hello! I\'m on my way to work right now but'
                                          '\nhope you have a good one!"'}
            },
            'older1': {
                'Description': 'I hope her grandpa is a little nicer... he speaks,'
                               '\n"Hey there ' + self.name + '!, how are you!"',
                'Options': {'older1Talk': '"Not too bad! Just spoke with your niece...'
                                          '\nshes so nice."',
                            'older1Talk2': '"Pretty good! Headed to work myself, but just wanted'
                                           '\nto say good morning!"'}
            },
            'older1Talk': {
                'Description': '"Oh don\'t mind her, she\'s just a cranky teenager." He laughs as he says this.',
                'Options': {'neighborly': '"Yeah I understand, I figured I\'d take some time to talk to the'
                                          '\nneighbors before I go to work though!"',
                            'understand': '"I get it, FinnCorp hasn\'t exactly held up with their end of bargains"'}
            },
            'neighborly': {
                'Description': '"Well, I\'m very glad you did! I\'ve been meaning to ask you something recently'
                               '\nabout your job at FinnCorp!"',
                'Options': {'ohno': '"Sure, go ahead!',
                            'leave': 'Actually, speaking of that, I should probably get to work,'
                                     '\nbut we can talk later!"'}
            },
            'understand': {
                'Description': '"Well, actually, speaking of FinnCorp, I was wondering if I could ask you'
                               '\na quick question while you\'re here!',
                'Options': {'ohno': '"Sure, go right ahead"'}
            },
            'ohno': {
                'Description': '"Well... I\'ve been on hold for one of those fancy "Finnies" for quite'
                               '\nsome time, I have my heart condition, and my doctor says Finny helps to monitor'
                               '\nit, I\'ve sent FinnCorp so much money all these years, and I was just wondering'
                               '\nif maybe you could put in a good word for me!"... he lets out a sad chuckle.',
                'Options': {'liar': '"Sure, I\'ll let them know about you for sure."',
                            'honesty': '"I cant say for certain I can do anything, I am just a customer service rep."'}
            },
            'liar': {
                'Description': 'He perks up instantly, "I am so glad to hear that. I owe you ' + self.name + '!"',
                'Options': {'leave': '"Don\'t worry about it... I should probably head to work, see you later"'
                                     '\nThis is gonna weigh on my conscience all day...', }
            },
            'honesty': {
                'Description': 'He instantly sulks, "Oh... I\'m sorry to have bothered you then,'
                               'I trust FinnCorp with my money though, I know I\'ll get Finny soon enough!"',
                'Options': {'leave': '"I\'m sorry to disappoint, but yeah! I don\'t have Finny myself either...'
                                     '\nI should probably get to work though, see you later!'}  # Finished, go to work
            },
            'older1Talk2': {
                'Description': 'I\'m already tired of the whole family, I should just go.',
                'Options': {'leave': 'Walk to work.'}  # Finish, head to work
            },
            'olderTalk': {
                'Description': 'He responds "Not too bad! Don\'t worry about calling me Sir though,'
                               '\nI\'m just the old man living in the apartment."',
                'Options': {'benice': '"Well, it\'s great to officially meet! I\'ve been meaning'
                                      '\n to stop by and say hello."',
                            'leave': '"I\'m glad your day is going good! I should honestly head to work though,'
                                     '\nsee you later!"'}  # Finished, head to work
            },
            'benice': {
                'Description': '"I sit out here every day! It\'s nice to see your generation working so hard,'
                               '\nmy niece over there doesn\'t do much of anything except go to school and complain,'
                               '\ntypical teenagers..."',
                'Options': {'benicer': '"Yeah, FinnCorp definitely keeps me busy!"... so the young lady is his niece?',
                            'leave': '"Teenagers will be teenagers!, I should honestly get going to work anyways,'
                                     '\nsee you later!"'}
            },
            'benicer': {
                'Description': '"Now that you bring up FinnCorp, I\'ve been meaning to ask you something...'
                               '\nif you don\'t mind',
                'Options': {'ohno': 'A man on a mission, I respect that... "Sure, go ahead!"'}

            },
            'olderTalk2': {
                'Description': 'Don\'t think I have the energy to talk to him today, maybe'
                               '\nI could try talking to the younger girl again?',
                'Options': {'younger': 'Walk up to the younger lady again, maybe I can do this.',
                            'leave': 'Never mind, I should get to work anyways.'}  # Finish, head to work part
            },
            # WORK PART!
            'leave': {
                'Description': 'Neighborly talk is horrifying... time to head to work.',
                'Options': {'work': 'Walk to FinnCorp'}
            },
            'work': {
                'Description': 'As you walk up to the FinnCorp building, you see an unusual'
                               '\namount of security outside, they approach you, and ask to see'
                               '\nyour work ID, unusual...',
                'Options': {'inside': 'Head inside the building'}
            },
            'inside': {
                'Description': 'FinnCorp does not cheap out on design... Finn Daemon had '
                               '\na vision, that vision being black and red, everywhere.',
                'Options': {'shannon': 'Talk to Shannon, the receptionist',
                            'elevator': 'Enter the elevator to your office, no more social talk today.'}
            },
            'shannon': {
                'Description': 'Shannon knows everything that goes on in this building,'
                               '\nshe reports to Finn Daemon himself...',
                'Options': {'shannon1': '"How are you today Shannon?"',
                            'shannon2': '"Hey Shannon, any idea what\'s going on outside?'}
            },
            'shannon1': {
                'Description': 'Shannon looks up at you with annoyance, "How am I?, I have'
                               '\nsecurity running around outside, and a busy day, I don\'t'
                               '\nneed to answer that."',
                'Options': {'elevator': 'Oh my. "Okay, sorry to bother you, hope your day gets better"', }
            },
            'shannon2': {
                'Description': 'Shannon looks up at you with disgust, "That isn\'t your concern in the slightest'
                               '\nget to work already ' + self.name + '"',
                'Options': {'elevator1': 'Why do I talk to people... guess I\'ll listen and go to work.'}
            },
            'elevator': {
                'Description': 'You get in the elevator and hit your floor number, ready to sit down'
                               '\nand do your job. Alone. Thank God. The door opens to your floor.',
                'Options': {'timeforwork': 'Exit the elevator and walk to your desk.'}
            },
            'elevator1': {
                'Description': 'As you walk away, she mutters "I can\'t believe they get Finny, of all people..."'
                               '\nWhat does that mean? Guess I\'ll figure out soon enough, time for work.'
                               '\nYou get into the elevator, and hit your floor number, ready to work.',
                'Options': {'timeforwork': 'Exit the elevator and walk to your desk.'}
            },
            'timeforwork': {
                'Description': 'When you walk into your office area, you notice all the other desks are empty...'
                               '\nno one seems to be around.',
                'Options': {'desk': 'Go to your desk.',
                            'manageroffice': 'Go to your manager, Victoria Serpens, office.'}
            },
            'desk': {
                'Description': 'At your desk, you see your usual setup, a basic computer, a coffee stained desk'
                               '\nand your phone, used to communicate with customers. But among these items, you'
                               '\nsee a new item, an envelope with "' + self.name + '" on it.',
                'Options': {'envelope': 'Open the envelope.',
                            'manageroffice': 'Ignore the envelope and go to your managers office.'}
            },
            'manageroffice': {
                'Description': 'You knock on Victoria\'s office door, no one responds, but you are curious.',
                'Options': {'entertheoffice': 'Curiosity gets the best of you, enter the office.',
                            'desk': 'Whatever, maybe she\'s in a conference call, go back to your desk.'}
            },
            'envelope': {
                'Description': 'You open the envelope, expecting junk mail, but are shocked by the message inside'
                               '\n'
                               '\nSAY NO'
                               '\n'
                               '\nWhat does this mean... say no to what?'
                               '\nAfter reading this, you hear chatter in the meeting room.',
                'Options': {'meetingroom1': 'Enter the meeting room, it seems your coworkers are all inside'}
            },
            'entertheoffice': {
                'Description': 'Entering the office, you close the door, and find it empty'
                               '\nno Victoria, but there is an open laptop on her desk...',
                'Options': {'laptop': 'You\'re already in here, might as well snoop, look at the laptop.',
                            'desk': 'Nope, not worth it, go back to your desk'}
            },
            'laptop': {
                'Description': 'Looking at the laptop, you see her email is open, the email displayed says'
                               '\n'
                               '\n"Today is a hard day for all of us here at FinnCorp, but regardless, the'
                               '\nquestion must still be asked. Managers, continue with the original plan."'
                               '\n'
                               '\nHard day? What does that mean... and what question?'
                               '\n'
                               '\nSuddenly, you hear footsteps coming your way',
                'Options': {'oshit': 'Close the laptop and try to not look suspicious.',
                            'oshit2': 'Leave the laptop open, and move towards the front of the office.'}
            },
            'oshit': {
                'Description': 'Victoria opens the door, looks at you, and looks at her laptop, closed...'
                               '\nIt was open when you entered.'
                               '\n"What are you doing ' + self.name + '.'
                                                                           '\nShe looks mad.',
                'Options': {'madexcuses': '"I just got here, noticed the office was empty and wanted to see'
                                          '\nif you were around."'}
            },
            'oshit2': {
                'Description': 'Victoria opens the door, notices her laptop untouched, and you standing still,'
                               '\nclose to the door'
                               '\n"Hey ' + self.name + ' what are you doing in here?'
                                                            '\nShe doesn\'t seem to know you were snooping.',
                'Options': {'goodexcuses': '"Hey Victoria! I just got here, I noticed the office was'
                                           '\nempty, and just wanted to see if you were around at least."'},
            },
            'madexcuses': {
                'Description': 'Victoria looks you up and down.'
                               '\n"Mmmhmmm... get to the meeting room, we have important things to discuss.',
                'Options': {'meetingroom2': 'Don\'t makes things worse. Follow Victoria to the meeting room.'}
            },
            'goodexcuses': {
                'Description': 'Victoria smiles.'
                               '\n"Were all in the meeting room ' + self.name + ', exciting things to discuss,'
                                                                                     '\nFollow me!',
                'Options': {'meetingroom3': 'That went better than I thought it would.'
                                            '\nFollow Victoria into the meeting room.'}
            },
            'meetingroom1': {
                'Description': 'Guess I was late to the party, everyone is in the meeting room, what for?',
                'Options': {'takeaseat1': 'Take a seat amongst your coworkers.',
                            'manageroffice': 'Stop by Victoria\'s office.'}
            },
            'meetingroom2': {
                'Description': 'Victoria is mad, she knows I was snooping, why did I shut the laptop...'
                               '\nArriving at the meeting room, she opens the door and points inside.'
                               '\nNot another word said.',
                'Options': {'takeaseat2': 'Quickly get to a chair, no more snooping ever again.',
                            'desk': 'Stop by your desk, did you see a letter for you on it?'}
            },
            'meetingroom3': {
                'Description': 'Victoria didn\'t seem to notice my snooping, thank God.'
                               '\nWe enter the break room and she heads up to the front, smiling at'
                               '\neveryone as she walks.',
                'Options': {'takeaseat3': 'Sit down near the front, no use looking suspicious in the back.',
                            'desk': 'Stop by your desk, did you forget anything?'}
            },
            # Meeting room part
            'takeaseat1': {
                'Description': 'Taking a seat, you see Victoria at the front, stressed, but ready to give'
                               '\nanother boring presentation.',
                'Options': {'waitaround': 'Wait for the presentation to start',
                            'askaround1': 'Ted, your work "friend" sits next to you, ask him '
                                          '\nwhat the meeting is about.'}
            },
            'takeaseat2': {
                'Description': 'Victoria is clearly mad, this won\'t look too good on your yearly review.'
                               '\nShe walks up to the front, grabs her papers, and prepares for her presentation.',
                'Options': {'waitaround': 'Wait for the presentation to start.',
                            'askaround2': 'Ted, your work "friend" smirks at you... '
                                          '\n"Someone\'s in trouble..." he says'
                                          '"\nYeah don\'t ask, what is this meeting even about?"'}
            },
            'takeaseat3': {
                'Description': 'That was a close one. Victoria walks to the front, almost excitedly,'
                               '\nand prepares for her presentation.',
                'Options': {'waitaround': 'Wait for the presentation to start.',
                            'askaround3': 'Ted calls for you, "Hey ' + self.name + ' do you know what'
                                                                                    '\nthis meeting is about?"'}
            },
            'waitaround': {
                'Description': 'Victoria clears her throat after a short duration, and gathers everyone\'s attention'
                               '\n"I\'m sure your\'e all wondering why I called you in to this random meeting...'
                               '\nRest assured, this is good news!',
                'Options': {'askaround1': 'Ted, your work "friend" sits next to you, ask him '
                                          '\nwhat the meeting is about.'}
            },
            'askaround1': {
                'Description': 'test',
                'Options': {'finish': 'test finish the game'}
            },
            'askaround2': {
                'Description': ''
            },
            'askaround3': {
                'Description': ''
            },
            'finish': {
                'Description': 'finished.'
            }
        }
    def final_choice(self):
        print('Final Choice: ')
        print('A. Accept Finny into your home.')
        print('B. Reject Finny.')
        choice = input('Enter your choice (A/B): ').strip().upper()

        if choice == "A":
            self.progress = 1.1
            return
        elif choice == "B":
            self.progress = 1.2
            return

        else:
            print('Invalid Choice. Choose wisely.')
            return self.user

    def start(self):
        print("Act 1: Broke and Desperate")
        print()
        while not self.completed:
            location_info = self.act1_map[self.current_location]
            print(location_info['Description'])

            options = location_info['Options']
            print('What do you want to do?')
            for number, (action, description) in enumerate(options.items(), start=1):
                print(f"{number}. {description}")
            choice = input("Enter the number of your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                action = list(options.keys())[int(choice) - 1]
                # This is Going to take you to act2A
                if(action == 'finishA'):
                    self.progress = 1.1
                    return self.user
                #This is Going to take you to act2B
                if (action == 'finishB'):
                    self.progress = 1.2
                    return self.user
                self.handle_action(action)
            else:
                print("Invalid choice. Please enter a valid number.\n")

    def handle_action(self, action):
        if action in self.act1_map[self.current_location]['Options']:
            print(f'You chose {self.act1_map[self.current_location]['Options'][action]}')

            if action == 'viewable_objects':
                self.current_location = 'viewable_objects'
            else:
                self.current_location = action
        else:
            print('Invalid action. Please enter a valid action.\n')
        print()




