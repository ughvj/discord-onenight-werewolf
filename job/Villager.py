from job.Job import Job

class Villager(Job):
    
    def __init__(self, name, belongs):
        super().__init__(name, belongs)
