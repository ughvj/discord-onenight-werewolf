from job.Job import Job

class Seer(Job):

    def __init__(self):
        super().__init__()
        super().setName('seer')
        super().setDisplayName('**占い師**')
        super().IamWerewolf(False)
