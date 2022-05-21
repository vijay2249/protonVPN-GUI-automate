import os
import time
import psutil
from pywinauto import Application, Desktop

# get the process pid of the application, if any then kill the processes
def find_and_kill_processes(process_name):
    for process in psutil.process_iter():
        try:
            if process_name.lower() in process.name().lower():
                os.system(f"taskkill /pid {i}")
                print("killing the existing process...")
        except:
            print("No such process currently running")

process_name = str(input("Enter process name: "))
find_and_kill_processes(process_name)

# since the pre processes are deleted, create a new instance of it
file_path = str(input("Enter app location to start the app:\n\t"))
app = Application(backend='uia').start(file_path)

# sometimes it takes sometime to load gui, so instead of waiting to load 
time.sleep(5) #sleep for 5 seconds for app gui to load

#this shows pywinauto.application.WindowSpecification object at <location>
print(app.ProtonVPN) 

main_window = app.ProtonVPN