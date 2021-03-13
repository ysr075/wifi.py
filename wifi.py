import os
import time
import random

def timer(seconds = 0.125):
    time.sleep(seconds)

def color():
    num = random.randint(1,9)
    os.system("color 0" + str(num))

def clear():
    os.system("cls")

def loading():
    print("<    loading.")
    timer()
    color()
    clear()
    print("<|   loading..")
    timer()
    color()
    clear()
    print("<|>  loading...")
    timer()
    color()
    clear()
    print("  >  loading...")
    timer()
    color()
    clear()
    print(" |>  loading..")
    timer()
    color()
    clear()
    print("<|>  loading.")
    timer()
    color()
    clear()

def directory():
    os.system("dir")

def main():
    while True:
        shell = input("root@ysr075:~# ")
        if (shell == "wifikey" or shell == "wifikeyprofile"):
            os.system("netsh wlan show profiles")
            wifi_name = str(input("wifi victim: "))
            os.system("netsh wlan show profiles " + wifi_name + " key=clear")
        elif (shell == "clear" or shell == "cls"):
            clear()
        elif (shell == "ls" or shell == "dir"):
            directory()

for i in range(0, 3):
    loading()
main()
