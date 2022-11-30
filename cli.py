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
    pass

def inputTemp():
    pass
        
def logicProcess():
    pass

def dataFrame():
    pass

def main():
    EquipmentDetails()
    inputDate()

if __name__=="__main__":
    main()
