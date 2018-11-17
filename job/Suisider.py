from job.Job import Job

class Suisider(Job):

    def __init__(self):
        super().__init__()
        super().setName('suisider')
        super().setDisplayName('**吊人**')
        super().IamWerewolf(False)
