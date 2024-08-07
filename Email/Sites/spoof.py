import random

class Spoof:
    def __init__(self):
        self.ua_path = 'Assets/user_agents.txt'

    def user_agent(self):
        return random.choice(open(self.ua_path).readlines()).strip()