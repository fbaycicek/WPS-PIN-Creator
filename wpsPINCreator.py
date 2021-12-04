#Code=UTF-8

import random
from threading import Thread
import datetime
from time import sleep

i="""
--------------------------------------------------
                WPS PIN MAKER
    CREATE WPS PIN LISTS FOR WI-FI (BRUTE-FORCE)
--------------------------------------------------
"""
print(i)
print(">>>default(1000)")
line = input(">>>How Much Do You Want To Line: ")
list_name = input(">>PIN List Name: ")
start = input(">>>Enter To Start: ...")
x = 0

def pin_Maker():

    try:
        if start == "":
            if line == "":
                for pin in range(5000):

                    random_pin = '{}{}{}{}{}{}{}{}'.format(*__import__('random').sample(range(0,9),8))
                    doctype = "{}.txt".format(list_name)
                    save = open(doctype,"a")
                    save.write("{}\n".format(random_pin))
                    print(random_pin)

                save.close()
                
            elif line != "":
                print(line)
                sleep(1)
                int_line = int(line)
                global x
                while True:

                    random_pin = '{}{}{}{}{}{}{}{}'.format(*__import__('random').sample(range(0,9),8))
                    doctype = "{}.txt".format(list_name)
                    save = open(doctype,"a")
                    save.write("{}\n".format(random_pin))
                    print(random_pin)
                    x+=1
                    if x == int_line:

                        break
                    else:
                        pass
            
                save.close()

            with open("{}.txt".format(list_name), "r") as c:
                line_i = c.read().count("\n")
                line_i_w = "PIN List Line: {}".format(str(line_i))
                print(line_i_w)
            print("[Create Succesfuly")
            input("Enter To Exit  or  CTRL+C")

        elif start == "e" or start == "E" or start == "exit" or start == "Exit":
            print("Bye ^^")

    except:
        print("An Error Occurred, Try Again! ")

def exit():
    print("Bye ^^")

if line == "e" or line == "E":
    exit()
elif line !="e" or line !="E":
    create = Thread(target=pin_Maker)
    create.start()