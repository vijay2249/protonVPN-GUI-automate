import os
import time
import psutil
from pywinauto import Application, Desktop

class Kill_Pre_Processes():
    def __init__(self, name):
        self.process_name = name
    
    def find_and_kill():
        for proc in psutil.process_iter():
            try:
                if self.process_name.lower() in proc.name().lower():
                    os.system(f"taskkill /pid {proc.pid}")
            except:
                pass
        print("All pre running processes are killed...")

