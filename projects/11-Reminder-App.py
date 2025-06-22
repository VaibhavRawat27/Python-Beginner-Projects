import time
import os
import platform

def beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 1000)
    else:
        print('\a') 

def reminder_app():
    print("Welcome to Reminder App!")
    message = input("Enter your reminder message: ")

    print("Set time for reminder:")
    minutes = int(input("Minutes: ") or 0)
    seconds = int(input("Seconds: ") or 0)

    total_seconds = minutes * 60 + seconds
    if total_seconds <= 0:
        print("Time must be greater than zero.")
        return

    print(f"\nReminder set for {minutes}m {seconds}s. Waiting...")

    time.sleep(total_seconds)

    print("\nReminder Alert!")
    print(f"{message}")
    beep()

if __name__ == "__main__":
    reminder_app()
