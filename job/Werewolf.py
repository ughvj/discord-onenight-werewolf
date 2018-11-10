class Werewolf(Job):
    
    def __init__(self, name, belongs):
        super().__init__(name, belongs)

    def actAtNight(self):
        return True
