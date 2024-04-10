class Act3C:
    def __init__(self, user):
        self.progress = user.progress
        self.name = user.name
        # Initialize player location
        self.current_location = 'start'
        # Track if act is completed or not
        self.completed = False

        # Map
        self.act1_map = {}