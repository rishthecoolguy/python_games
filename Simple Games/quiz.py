print("Welcome to my quiz! Hope you enjoy.")

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    quit()

print("OK! Lets Play.")
score = 0


answer = input("What does CPU stand for?\n")
if answer.lower() == "central processing unit":
    print("Great Job! That's the correct answer!")
    score += 1
else:
    print("Sorry, you got that wrong. Better luck next time.")

answer = input("What does RAM stand for?\n")
if answer.lower() == "random access memory":
    print("Great Job! That's the correct answer!")
    score += 1
else:
    print("Sorry, you got that wrong. Better luck next time.")

answer = input("What does LAN stand for?\n")
if answer.lower() == "local area network":
    print("Great Job! That's the correct answer!")
    score += 1
else:
    print("Sorry, you got that wrong. Better luck next time.")

answer = input("What does GPU stand for?\n")
if answer.lower() == "graphics processing unit":
    print("Great Job! That's the correct answer!")
    score += 1
else:
    print("Sorry, you got that wrong. Better luck next time.")

answer = input("True or False. A computer always has to be plugged in.\n")
if answer.lower() == "false":
    print("Great Job! That's the correct answer!")
    score += 1
else:
    print("Sorry, you got that wrong. Better luck next time.")

print(f"Great Job! You got {score} questions correct.")


