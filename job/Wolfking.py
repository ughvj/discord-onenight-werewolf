from job.Job import Job

class Wolfking(Job):

    def __init__(self):
        super().__init__()
        super().setName('wolfking')
        super().setDisplayName('**大狼**')
        super().IamWerewolf(True)
