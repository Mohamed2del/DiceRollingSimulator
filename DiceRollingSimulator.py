import random
yes = 'y'
print ("        Welcome To Dice Rolling Simulator       ")
while (True):
    if (yes == 'y'):
        t = random.randint(1, 6)
        print (t)
        print('Roll Again ???! (Y) or (N) please')
        yes = input()
    elif (yes == 'n'):
        print('Bye Bye My Dear')
        break
    else :
        print("Sorry Wrong Input")
        print('Roll Again ???! (Y) or (N) please')
        yes = input()
