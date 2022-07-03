import schedule as sch
import time

def job():
    print("I'm working ...")

sch.every(10).seconds.do(job)

while True:
    sch.run_pending()
    time.sleep(1)