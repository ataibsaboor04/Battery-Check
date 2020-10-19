import psutil
import sys
from mymodules.notification import notify
from mymodules.time import from_seconds


def alert(text, percent, time=30):
    notify(text, f"Your battery is {percent}% charged",
           f"E:/Python Programs/Useful Scripts/Battery/battery.ico", time)


def main():
    battery = psutil.sensors_battery()
    percent = battery.percent
    if battery.power_plugged:
        if percent >= 95:
            alert("Please Plug-Out the Charger", percent)
        elif percent >= 88:
            main()

        sys.exit()
    else:
        if percent <= 35:
            alert("Please Plug-In the Charger", percent, 90)
        elif percent <= 60:
            alert("Please Plug-In the Charger", percent)
        sys.exit()


if __name__ == '__main__':
    main()
