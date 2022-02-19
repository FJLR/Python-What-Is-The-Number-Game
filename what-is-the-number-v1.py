#module

import random


#randrange wont include the 11
#randint it will include the 11

#variables can make using underscore

#r = random.randrange(11)
#print(r)

top_of_range = input("Hello type a number from 1 to 10 ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("Please type a number higher than zero next time...!")
        quit()

else:
    print("Type a number next time, thank you...!")
    quit()


random_number = random.randint(0, top_of_range)
#print(random_number)

score = 0

while True:
    score += 1
    user_guess = input("make a guess? ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time...!")
        continue

    if user_guess == random_number:
        print("You got it right...!")
        break
    else:
        if user_guess > random_number:
            print("you were above number")
        else:
            print("you were below the number")

    #else:
        #print("you did not get it this time")
          
print("you got in ", score, "guesses")               
