from job.Villager import Villager
from job.Werewolf import Werewolf
from job.Seer import Seer
from job.Thief import Thief
from job.Madman import Madman
from job.Suicider import Suicider
from job.Topvillager import Topvillager
from job.Wolfking import Wolfking

class JobMaster():

    def __init__(self, job_names):
        self.joblist = [Villager(), Werewolf(), Seer(), Thief(), Madman(), Suicider(), Topvillager(), Wolfking()]
        self.jobdict = {job.getName():job for job in self.joblist}

        self.jobs = [self.jobdict[jobname] for jobname in job_names]
        self.jobs_display = ' '.join([job.getDisplayName() for job in self.jobs])

    def getJobsList(self):
        return self.jobs

    def getJobsDisplay(self):
        return self.jobs_display
