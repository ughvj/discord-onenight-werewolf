from job.Job import Job

class Werewolf(Job):

    def __init__(self):
        super().__init__()
        super().setName('werewolf')
        super().setDisplayName('**人狼**')
        super().IamWerewolf(True)
