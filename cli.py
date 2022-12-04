import pandas as pd
import numpy as np 
from datetime import datetime

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
    global from_date_time
    global to_date_time
    # global no_days

    valid_int = False
    while not valid_int:
        try:
            fromDate = input("Enter Start Date & Time in Given Format (DD/MM/YYYY HH:MM): ")
            toDate = input("Enter End Date & TIme in Give Format (DD/MM/YYYY HH:MM): ")
            from_date_time = datetime.strptime(fromDate,"%d/%m/%Y %H:%M")
            to_date_time = datetime.strptime(toDate, "%d/%m/%Y %H:%M")
            # no_days = abs((from_date-to_date).days)
            # print("Difference between Date: ", no_days) 
            valid_int = True
        except ValueError:
            print("Wrong input format given, please try again!.")

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
    inputTemp()

if __name__=="__main__":
    main()
