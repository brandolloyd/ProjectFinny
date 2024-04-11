class Act3D:
    def __init__(self, user):
        self.user = user
        self.progress = user.progress
        self.name = user.name
        # Initialize player location
        self.current_location = 'start'
        # Track if act is completed or not
        self.completed = False

        # Map
        self.act3d_map = {
            'start': {
                'Description': 'You chose to stay and explore. Your eyes have adjusted fully to the darkness, and you'
                               '\ncan visibly see the decaying effect that displays around the floor, this place looks'
                               '\nabandoned, but clearly, something is going on. Backtracking to the scene before, you '
                               '\nsee the laptop and the door with "Demon" on it.',
                'Options': {'laptop': 'Make your way towards the laptop.',
                            'door': 'Open the door, a slight hue of warm light comes from it...'}
            },
            'laptop': {
                'Description': 'Walking towards the laptop, it looks like an artifact. An IBM ThinkPad 600... In your'
                               '\ntraining when you first started at FinnCorp, you recall the fact that FinnCorp in its'
                               '\nbeginnings, utilized this laptop in the 1990\'s.',
                'Options': {'openit': 'Sit down and open the laptop.',
                            'door': 'Walk towards the door instead.'}
            },
            'door': {
                'Description': 'Opening the door, a casket sit\'s in front of you. Candles lit around it, and new age'
                               '\ntech placed through the room. A large monitor mounted on the wall, perfectly placed'
                               '\nabove the casket, and cameras on both sides...',
                'Options': {'casket': 'View the casket, there seems to be writing on it.'
                                      '\nYou will not be able to view the laptop after this.',
                            'laptop': 'Leave the room and open the laptop.'}
            },
            'openit': {
                'Description': 'Opening the laptop, a happy tone plays, and the system boots. This is old tech, nothing'
                               '\nspecial, but you see an old email client "Lotus Notes" open. Two emails catch your eye.',
                'Options': {'email1': 'Email 1: Titled "Plans."',
                            'email2': 'Email 2: Titled "It\'s Okay.'}
            },
            'casket': {
                'Description': 'Finn Daemon... The words on the casket say Finn. Daemon. He really did die. What is his'
                               '\ncasket doing here...',
                'Options': {'run': 'This is a dead man, I need to leave now...'}
            },
            'email1': {
                'Description': 'The email says: '
                               '\nSender: Finn Daemon'
                               '\nSubject: Plans.'
                               '\n'
                               '\nFinny has been revealed, we are still years away from being finished, but progress'
                               '\nhas been made. When we release Finny, the rich will pay thousands for it, which will'
                               '\nfund future endeavors. This is for the best. My daughter, Victoria, has made great'
                               '\nprogress, and shows promise in a future at FinnCorp, she is young, but once the time'
                               '\ncomes, I know the Daemons will be legends, and I will be there to see it all.'
                               '\n'
                               '\nYour leader, Finn Daemon.',
                'Options': {'continue1': 'Continue.'}
            },
            'continue1': {
                'Description': 'Victoria... she\'s Finn Daemon\'s daughter... how did no one know this. She must have'
                               '\nchanged her last name to stop anyone from figuring out. And what does he mean'
                               '\n"I will be there to see it all."',
                'Options': {'email2': 'View the second email, titled "It\'s Okay."',
                            'door': 'Leave the laptop, go back to the door.'}
            },
            'email2': {
                'Description': 'The email says:'
                               '\nSender: Finn Daemon'
                               '\nSubject: It\'s Okay.'
                               '\n'
                               '\nVictoria... I understand your sadness. Finny 2.0 releases tomorrow. The time has come.'
                               '\nI know what it means, and so do you, but this is not the end. When Finny 2.0 releases'
                               '\nit will mark the beginning of a new era, I will not be gone, I will not be different,'
                               '\nI will be everywhere.'
                               '\nBe smart my little serpent, we are the future. I love you.'
                               '\n'
                               '\nForever your father, Finn Daemon.',
                'Options': {'continue2': 'Continue.'}
            },
            'continue2': {
                'Description': 'This was yesterday... was he... was he here? Using this laptop? I don\'t understand.',
                'Options': {'email1': 'View Email 1, titled "Plans."',
                            'door': 'Leave the laptop, go back to the door.'}

            },
            'run': {
                'Description': 'This is all wrong, you go to exit, but a familiar AI voice speaks behind you...'
                               '\nHello, ' + self.name + ', I see you found my former body.',
                'Options': {'respond1': 'Be smart: "I don\'t know what is happening. I shouldn\'t be here."',
                            'respond2': 'Be bold: "Finn Daemon... Finny 2.0 is Finn Daemon. You."'}
            },
            'respond1': {
                'Description': 'You turn around, and the monitor on the wall is lit up, red and black, but different,'
                               '\nif you squint, you see a face behind the hue, Finn Daemon\'s face.'
                               '\n"But you should, I brought you here. See, you said no to allowing Finny into your home'
                               '\nallowing me... into your home. Not too kind of you '+self.name+'."',
                'Options': {'respond1.1': '"I made a mistake, I was scared, it... you, were just announced."'}
            },
            'respond1.1': {
                'Description': 'Finn Daemon responds, "You made several mistakes, being here is your chance at'
                               '\nredemption. Allow me to elaborate on your situation?',
                'Options': {'elaborate': '"I don\'t have a choice, do I? Elaborate."'}
            },
            'respond2': {
                'Description': 'You turn around, and the monitor on the wall is lit up, red and black, but different,'
                               '\nif you squint, you can see a face behind the hue, Finn Daemon\'s face.'
                               '\n"You\'re quite perceptive '+self.name+', too perceptive. I brought you here for a reason.'
                               '\nYou\'re a problem, I need to know if you\'re a solution as well."',
                'Options': {'respond2.1': '"A problem? How am I a problem, I have no clue what is going on."'}
            },
            'respond2.1': {
                'Description': 'The monitor flickers, like an eye twitch of an angry man. "You have no idea what you'
                               '\nhave just become a part of. Shut your mouth and listen.',
                'Options': {'elaborate': 'You carefully nod your head.'}
            },
            'elaborate': {
                'Description': 'He speaks "I built FinnCorp from the ground up with my own two hands... I knew society'
                               '\ncould\'nt survive on it\'s own, so I came up with a plan, a plan decades in the making.'
                               '\nYou don\'t seem to have the brain power to understand what I did, so I\'ll dumb it'
                               '\ndown for you. Finn Daemon died, and his brain, all of it\'s glorious knowledge, has'
                               '\ngone towards something much greater. Yes, I am Finn Daemon, but I am so much more now.'
                               '\nI saw you in your apartment this morning, I saw you with your neighbors, I saw you'
                               '\nsnooping around the office, and I saw you say NO... TO GREATNESS."',
                'Options': {'keepelaborating': 'Continue.'}
            },
            'keepelaborating': {
                'Description': 'You made a grave mistake '+self.name+', if you would have said yes, things could have'
                                                                     '\nbeen so different. I understand now, you aren\'t the solution, you are only the problem.'
                                                                     '\nand you must be dealt with.',
                'Options': {'End': 'Run.'}
            },
            'End': {
                'Description': 'As you leave the room, into the darkness, the entire floor lights up, blinding you.'
                               '\nFinn Daemon speaks, "I would say I had high hopes for you, but humans are too predictable."'
                               '\nThe decayed room lights up, and vents in the ceiling begin to leak a red gas, it'
                               '\nenvelopes you, and enters through your mouth and nose, stopping your breathing.'
                               '\nFinny 2.0, Finn Daemon himself, kills you, removing the problem from his plan.'
                               '\n'
                               '\nENDING 4/4'
            }
        }

    def start(self):
        print("Act 3: Into the Dark.")
        print()
        while not self.completed:
            location_info = self.act3d_map[self.current_location]
            print(location_info['Description'])

            options = location_info['Options']
            print('What do you want to do?')
            for number, (action, description) in enumerate(options.items(), start=1):
                print(f"{number}. {description}")
            choice = input("Enter the number of your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                action = list(options.keys())[int(choice) - 1]
                if (action == 'End'):
                    return self.user
                self.handle_action(action)
            else:
                print("Invalid choice. Please enter a valid number.\n")

    def handle_action(self, action):
        if action in self.act3d_map[self.current_location]['Options']:
            print(f'You chose {self.act3d_map[self.current_location]['Options'][action]}')

            if action == 'viewable_objects':
                self.current_location = 'viewable_objects'
            else:
                self.current_location = action
        else:
            print('Invalid action. Please enter a valid action.\n')
        print()