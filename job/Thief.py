from job.Job import Job

class Thief(Job):

    def __init__(self):
        super().__init__()
        super().setName('thief')
        super().setDisplayName('**怪盗**')
        super().IamWerewolf(False)
