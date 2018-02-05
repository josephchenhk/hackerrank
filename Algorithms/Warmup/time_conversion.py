# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:43:59 2018

@author: joseph.chen
"""

from datetime import datetime

def timeConversion(s):
    # This method uses the built-in functions
    in_time = datetime.strptime(s, "%I:%M:%S%p")
    out_time = datetime.strftime(in_time, "%H:%M:%S")
    return out_time

def timeConversion(s):
    # Let's forget about the datetime lib. Build it from scratch
    if s[8:]=="AM":
        hour, minute, second = s[0:8].split(":")
        if hour=="12":
            hour = "00"
        return ":".join([hour, minute, second])
    elif s[8:]=="PM":
        hour, minute, second = s[0:8].split(":")
        if hour!="12":
            hour = str(int(hour) + 12)
        return ":".join([hour, minute, second])


if __name__=="__main__":
    s = "12:45:54PM"
    result = timeConversion(s)
    print(result) # expect output: "19:05:45"
