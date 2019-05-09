
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from time import sleep
from threading import *

url=input("Enter your url: ")

def refresh1(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[1])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread1")
        print(count)
    print(count)


def refresh2(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[2])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread2")
        print(count)
    print(count)


def refresh3(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[3])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread3")
        print(count)
    print(count)



def refresh4(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[4])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread4")
        print(count)
    print(count)



def refresh5(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[5])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread5")
        print(count)
    print(count)



def refresh6(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[6])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread6")
        print(count)
    print(count)



def refresh7(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[7])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread7")
        print(count)
    print(count)



def refresh8(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[8])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread8")
        print(count)
    print(count)


def refresh9(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[9])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread9")
        print(count)
    print(count)


def refresh10(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[10])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread10")
        print(count)
    print(count)



def refresh11(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[11])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread11")
        print(count)
    print(count)


def refresh12(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[12])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread12")
        print(count)
    print(count)


def refresh13(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[13])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread13")
        print(count)
    print(count)


def refresh14(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[14])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread14")
        print(count)
    print(count)


def refresh15(impression):
    global count
    for i in range(impression):
        driver.switch_to_window(driver.window_handles[15])
        driver.refresh()
        sleep(2)
        count = count + 1
        print("thread15")
        print(count)
    print(count)




# t0= Thread(target=refresh0, args=(impression, ))
t1= Thread(target=refresh1, args=(impression, ))
t2= Thread(target=refresh2, args=(impression, ))
t3= Thread(target=refresh3, args=(impression, ))
t4= Thread(target=refresh4, args=(impression, ))
t5= Thread(target=refresh5, args=(impression, ))
t6= Thread(target=refresh6, args=(impression, ))
t7= Thread(target=refresh7, args=(impression, ))
t8= Thread(target=refresh8, args=(impression, ))
t9= Thread(target=refresh9, args=(impression, ))
t10= Thread(target=refresh10, args=(impression, ))
t11= Thread(target=refresh11, args=(impression, ))
t12= Thread(target=refresh12, args=(impression, ))
t13= Thread(target=refresh13, args=(impression, ))
t14= Thread(target=refresh14, args=(impression, ))
t15= Thread(target=refresh15, args=(impression, ))


# t0.start()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
