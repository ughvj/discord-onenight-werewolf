from job.Job import Job

class Suicider(Job):

    def __init__(self):
        super().__init__()
        super().setName('suicider')
        super().setDisplayName('**吊人**')
        super().IamWerewolf(False)
