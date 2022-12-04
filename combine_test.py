#import datetime
from datetime import datetime

#dt1 = datetime.datetime(2022,1,1,10,00,00)
#dt2 = datetime.datetime(2022,1,30,17,00,00) 
dt = input("Enter from date (DD/MM/YYYY): ")
from_date = datetime.strptime("%d/%m/%Y", "%H:%M:%S")
tdelta = dt2 - dt1 
print(tdelta) 
print(from_date)



