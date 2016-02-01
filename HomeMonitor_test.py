#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ATangeman
#
# Created:     31/01/2016
# Copyright:   (c) ATangeman 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from googlevoice import Voice
from googlevoice.util import input
import os

def logIn(voice):
    print("Logging into GoogleVoice...")
    uName = "andrew@quarticsolutions.com"
    mskpswd = "WVc1a2NtVjM="
    voice.login(uName, mskpswd, None, True)
    del uName, mskpswd
    print("Logging successful.")
    return

def logOut(voice):
    voice.logout()

voice = Voice()
logIn(voice)
phoneNumber = '+16192139252'
text = "Hello, this is a test of your home monitoring system."\
       " This system will notify you when critical sensors inside your"\
       " home change."
voice.send_sms(phoneNumber, text)

sensortag=0

while sensortag != '1010':
    os.system("sudo /home/pi/433Utils/RPi_utils/RFSniffer >output.txt & pkill --signal SIGINT RFSniffer")
    with open("output.txt","r") as f:
        readf = f.read()
        for line in readf:
            pass
        last = line
        if (last == '1010'):
            voice.send_sms(phoneNumber, "Alert: Door is open")
        elif (last == '1011'):
            voice.send_sms(phoneNumber, "Alert: Door is closed")
        if f.closed == "False":
            f.close()

