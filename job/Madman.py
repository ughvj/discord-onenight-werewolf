from job.Job import Job

class Madman(Job):

    def __init__(self):
        super().__init__()
        super().setName('madman')
        super().setDisplayName('**狂人**')
        super().IamWerewolf(False)
