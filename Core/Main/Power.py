# Import modules

import subprocess
from ctypes import byref, c_bool, windll
from ctypes.wintypes import DWORD


# Puts the computer to sleep 

def Hibernate():
 subprocess.Popen('shutdown -h /f', shell=True)

# Turns off the computer

def Shutdown():
 subprocess.Popen('shutdown -s /t 0 /f', shell=True)


# Restarts computer

def Restart():
 subprocess.Popen('shutdown -r /t 0 /f', shell=True)

# Ends user session

def Logoff():
 subprocess.Popen('shutdown -l /f', shell=True)


# Blue screen of death

def BSoD():
 windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(c_bool()))
 windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, byref(DWORD()))