import time
import datetime
import schedule

def fun():
    print("Inside fun at : ",datetime.datetime.now())

def main():
    print("Inside Marvellous Automation script at : ",datetime.datetime.now())

    schedule.every(20).seconds.do(fun)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()