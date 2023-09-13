from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)) :
        try : 
            if partest[i] != usertest[i]:
                error = error + 1
        except :
            error = error + 1
    return error



def Speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)


while True :
    ck = input(" Ready to test : yes/no :")
    if ck == "yes" :
            test = ["Now, when you open the HTML file in a web browser, you'll have a simple web-based game interface that allows you to level up, upgrade strength, and increase the score of the character. You can further enhance and customize the game's functionality and appearance based on your requirements.","To convert the Python-based game into a web-based game using HTML, CSS, and JavaScript, you'll need to create a front-end interface for the game. Here's a basic example of how you can achieve this:"]
            test1 = r.choice(test)
            print("******* typing Speed *******")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input(" Enter : ")
            time_2 = time()

            print('Speed : ',Speed_time(time_1, time_2, testinput),"w/sec")
            print("Error : ", mistake(test1, testinput))
    elif ck == "no" :
        print("Thank You!")
        break
    else :
        print(" Wrong Input ")