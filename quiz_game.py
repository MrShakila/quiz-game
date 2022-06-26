print('Hello Welcome To My Game')

playing = input("Do You Want To Play? ")

if playing.lower() != "Yes":
    quit()

print("Okay Let's Play :) ")
score = 0
answer = input("What does Cpu  stands For? ")

if answer.lower() == "central":
    print("Correct")
    score+=1
else: print("Incorrect")


if answer.lower() == "central":
    print("Correct")
    score+=1
else: print("Incorrect")

if answer.lower() == "central":
    print("Correct")
    score+=1
else: print("Incorrect")

if answer.lower() == "central":
    print("Correct")
    score+=1
else: print("Incorrect")

if answer.lower() == "central":
    print("Correct")
    score+=1
else: print("Incorrect")


print("You Got " +str(score)+"Quessions Correct")