from datetime import datetime
import sys
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
            

def main():
    inputDate()

if __name__=="__main__":
    main()

