import time
import os
import platform

def beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 1000)
    else:
        print('\a')

def countdown_timer():
    try:
        total_seconds = int(input("Enter time in seconds: "))
        if total_seconds <= 0:
            print("Please enter a time greater than 0.")
            return

        print("\nCountdown Started:")

        while total_seconds:
            mins, secs = divmod(total_seconds, 60)
            hours, mins = divmod(mins, 60)
            timer_display = f"{hours:02d}:{mins:02d}:{secs:02d}"
            print(timer_display, end="\r")
            time.sleep(1)
            total_seconds -= 1

        print("00:00:00")
        print("Time's up!")
        beep()

    except ValueError:
        print("Invalid input. Please enter numeric value.")

countdown_timer()
