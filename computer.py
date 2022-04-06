import random
class Computer:
    def __init__(self):
        self.name = self.choose_random_name

    def choose_random_name(self):
        random_names = ['The Terminator', 'Master Chief', 'Cortana' ]
        random_name = random.choice(random_names)
        return random_name
        