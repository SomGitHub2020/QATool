from apscheduler.schedulers.background import BackgroundScheduler
from autoproc import getQAConfigDetails

def start():
    #Read trigger Rate from qaconfig model and pass this to below 3rd param. 
    scheduler = BackgroundScheduler()
    scheduler.add_job(getQAConfigDetails.getQACofig, 'interval', seconds=30)
  #  scheduler.add_job(talkToMIIQASystem.sendTrigger, 'interval', minutes=1)
  #  scheduler.add_job(talkToABAPQASystem.sendTrigger, 'interval', minutes=1)
    scheduler.start()