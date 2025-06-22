import datetime
import time
import platform

def beep():
    if platform.system() == "Windows":
        import winsound
        frequency = 1000  
        duration = 500    
        winsound.Beep(frequency, duration)
    else:
        print('\a') 

def alarm_app():
    alarm_time = input("⏰ Enter alarm time (HH:MM:SS - 24hr format): ")
    print(f"Alarm set for {alarm_time}...")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}", end="\r")
        if current_time == alarm_time:
            print("\nAlarm Time Reached!")
            break
        time.sleep(1)

    print("Alarm is beeping! Press CTRL+C or close window to stop.")

    try:
        while True:
            beep()
            time.sleep(1) 
    except KeyboardInterrupt:
        print("\nAlarm stopped by user.")

alarm_app()
