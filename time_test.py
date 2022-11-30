from datetime import datetime

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


def main():
    inputTime()

if __name__=="__main__":
    main()