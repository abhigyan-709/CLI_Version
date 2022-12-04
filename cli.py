import pandas as pd
import numpy as np 
from datetime import datetime
import sys

def EquipmentDetails():
    global equipment_name
    global instrument_number

    validInt = False
    while not validInt:
        equipment_name = input("Please enter the euipment name: ")
        if equipment_name.isalpha():
            validInt = True
        else:
            print("The input is not valid Equipment Name")
    
    validInt2 = False
    while not validInt2:
        instrument_number = input("Please enter Number of Instruments: ")
        if instrument_number.isdigit():
            validInt2 =True
        else:
            print("Invalid instrument number.")

def inputDate():
    global from_date
    global to_date
    global no_days

    valid_int = False
    while not valid_int:
        try:
            fromDate = input("Enter from date (DD/MM/YYYY): ")
            toDate = input("Enter to Date (DD/MM/YYYY): ")
            from_date = datetime.strptime(fromDate,"%d/%m/%Y").date()
            to_date = datetime.strptime(toDate,"%d/%m/%Y").date()
            no_days = abs((from_date-to_date).days)
            print("Difference between Date: ", no_days)
            valid_int = True
        except ValueError:
            print("Wrong input format given, please try again!.")

def inputTime():
    global minutes
    global fromTime
    global from_time
    global toTime
    global to_time
    global delta
    valid_int = False

    while not valid_int:
        try:
            fromTime = input("Enter from time (HH:MM:SS): ")
            toTime = input("Enter to time (HH:MM:SS): ")
            from_time = datetime.strptime(fromTime, "%H:%M:%S")
            to_time = datetime.strptime(toTime, "%H:%M:%S")
            print('Start Time: ', from_time.time())
            print('End Time: ', to_time.time())
            delta = abs(from_time - to_time)
            seconds = delta.total_seconds()
            minutes = seconds / 60
            print("Difference between time in minutes: ", minutes)
            valid_int = True
        except ValueError:
            print("Wrong time format given, please try again.")


def inputTemp():
    global low_temp
    global high_temp
    global temp_diff
    
    low_temp = input("Enter the lowest temperature recorded: ")
    high_temp = input("Enter the highest temperature recorded: ")
        
def logicProcess():
    pass

def dataFrame():
    pass

def main():
    EquipmentDetails()
    inputDate()
    inputTime()
    inputTemp()

if __name__=="__main__":
    main()
