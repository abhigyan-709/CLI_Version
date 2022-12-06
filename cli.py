import pandas as pd
import numpy as np 
from datetime import datetime
import matplotlib.pyplot as plt
import random
import matplotlib.dates as mdates

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

    valid_int3 = False
    while not valid_int3:
        try:
            low_temp = float(input("Enter the lowest temperature recorded: "))
            high_temp = float(input("Enter the highest temperature recorded: "))
            valid_int3 = True
        except:
            print("Please enter the valid temperature.")
        
def logicProcess():
    global data
    global df 
    global lst 

    for j in range(int(instrument_number)):

        data = pd.date_range(start = from_date_time, end=to_date_time, freq=str(intervals)+'min')

        df = pd.DataFrame(
            {
                "Date": data
            }
        )
        df.index = np.arange(1, len(df) + 1)

        lst = []
        # for j in range(int(instrument_number)):
        for i in range(len(df)):
            ran = random.uniform(float(low_temp), float(high_temp))
            ran2 = round(ran, 2)
            lst.append(ran2)
            
        df = df.assign(Temperature = lst)

        #df.plot(df["Date"], df["Temperature"])
        #df.plot(xlabel="Date & Time", ylabel="Temperature")
        plt.xlabel('Date & Time')
        plt.ylabel('Temperature')
        plt.style.use('Solarize_Light2')
        plt.title('Dates v/s Temperature Graph of Sensors')

        fig, ax = plt.plot()
        fig.autofmt_xdate()
        plt.plot(df["Date"], df["Temperature"])
        xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
        ax.xaxis.set_major_formatter(xfmt)


def showDataSave():
    global df2
    df2 = pd.DataFrame()
    df2['Date'] = [d.date() for d in df['Date']]
    df2['Time'] = [d.time() for d in df['Date']]
    df2 = df2.assign(Temperature = lst)
    print(df2)

def dataPlot():
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
