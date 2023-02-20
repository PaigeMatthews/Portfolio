import time
from plyer import notification #using plyer to make the notification

if __name__ == "__main__":
        while True:
                notification.notify( #will give me an alert every 4 hours to commit my work to the repo
                        title = "Alert",
                        message = "Do your daily log and commit to repo.",
                        timeout = 10
                )
                time.sleep(14400) #14400 is 4 hours in seconds