from task import Task
from scheduler import Scheduler
from notification_manager import NotificationManager
from gui import SchedulerGUI

def main():
    scheduler = Scheduler(capacity = 16)
    notification_manager = NotificationManager()
    scheduler.add_listener(notification_manager)
    gui = SchedulerGUI(scheduler)

    gui.start_scheduler()

    #for i in range(5):
     #   task = Task("Unnamed task " + str(i), 1)
      #  scheduler.add_task(task)
    
    #scheduler.run()

if __name__ == "__main__":
    main()