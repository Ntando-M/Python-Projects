import random
import winsound

Roll1 = random.sample(range(1,7),1)
Roll2 = random.sample(range(1,7),2)
Roll3 = random.sample(range(1,7),3)

loop = True
while loop == True:
    print("----------------------")
    print("Please choose between 1 or 2 or 3")
    option = str(input("Select number of dice:"))

    if option == "1":
        print(Roll1)
        winsound.PlaySound("dice.wav", winsound.SND_FILENAME)
        print("Next Turn")
        

    if option == "2":
        print(Roll2)
        winsound.PlaySound("dice.wav", winsound.SND_FILENAME)
        print("Next Turn")
       

    if option == "3":
        print(Roll3)
        winsound.PlaySound("dice.wav", winsound.SND_FILENAME)
        print("Next Turn")
        






