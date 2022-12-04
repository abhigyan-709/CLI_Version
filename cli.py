import pandas as pd
import numpy as np 
from datetime import datetime
import matplotlib.pyplot as plt
import random

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

def inputFrequency():
    global intervals
    valid_int2 = False
    while not valid_int2:
        intervals = input("Enter Time Intervals in minutes at which device is running: ")
        if intervals.isdigit():
            valid_int2 = True
        else:
            print("Please enter the valid interval.")

def inputTemp():
    global low_temp
    global high_temp

    low_temp = input("Enter the lowest temperature recorded: ")
    high_temp = input("Enter the highest temperature recorded: ")
        
def logicProcess():
    global data
    global df 
    global lst 

    data = pd.date_range(start = from_date_time, end=to_date_time, freq=str(intervals)+'min')

    df = pd.DataFrame(
        {
            "Date": data
        }
    )
    df.index = np.arange(1, len(df) + 1)

    lst = []
    for i in range(len(df)):
        ran = random.uniform(float(low_temp), float(high_temp))
        ran2 = round(ran, 2)
        lst.append(ran2)
    
    df = df.assign(Temperature = lst)

def showDataSave():
    pass

def dataPlot():
    plt.plot(df["Date"], df["Temperature"])
    plt.show()

def main():
    EquipmentDetails()
    inputDate()
    inputFrequency()
    inputTemp()
    logicProcess()
    dataPlot()
    showDataSave()

if __name__=="__main__":
    main()
