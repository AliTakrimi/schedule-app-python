import schedule as sch
import time

def job():
    print("I'm working ...")

def greeting():
    print("How are you?")

sch.every(10).seconds.do(job)
sch.every(20).seconds.do(greeting)


while True:
    sch.run_pending()
    time.sleep(1)