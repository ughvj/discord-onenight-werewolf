from job.Job import Job

class Topvillager(Job):

    def __init__(self):
        super().__init__()
        super().setName('topvillager')
        super().setDisplayName('**村長**')
        super().IamWerewolf(False)
