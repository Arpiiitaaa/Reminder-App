import time
from plyer import notification

if __name__ == "__main__":
    while True:
      notification.notify(
          title = "Water Time!",
          message = "You'll end up being dehydrated; DRINK WATERRRR",
          app_icon = "D:\",
          timeout = 10
      )
      time.sleep(60*60)

