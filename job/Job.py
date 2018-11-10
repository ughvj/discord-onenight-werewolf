class Job():
    
    def __init__(self, name, belongs):
        self.name= name
        self.belongs = belongs
        self.using = False

    def getName(self):
        return self.name

    def actAtNight(self):
        return True

    def belongTo(self):
        return self.belongs

    def use(self):
        self.using = True

    def usingSomeone(self):
        return self.using
