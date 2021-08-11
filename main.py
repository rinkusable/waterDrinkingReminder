#import time
from plyer import notification
if __name__ == "__main__":
    notification.notify(
        title = "water drinking reminder",
        message = "Do your body have suuficient water"
                  " you have to drink sufficient water for better health."
                  "its your time to drink water",
       app_icon = "D:\python projects\drinkingWaterReminder\glass.ico",
        timeout = 5

    )
