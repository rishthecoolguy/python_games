name = input("Type your name: ")
print(f"Welcome {name} to this amazing adventure ")

answer = input("You are on a dirt road it has come to an end and you can go left or right. Which way would you like"
               " to go?\n").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. (walk/swim)\n")

    if answer == "swim":
        print("You went back to the main road. You lose.")
    elif answer == "walk":
        print("You walked for many miles and ran out of water. You lost the game.")
    else:
        print("Not a valid option. You have just lost.")

elif answer == "right":
    answer = input("You come to a bridge it looks wobbly. Do you want to cross it or head back. (cross/head back)\n").lower()

    if answer == "head back":
        print("You go back to the main road")
    elif answer == "cross":
        answer = input("You crossed the bridge and meet a stranger. Do you talk to them (yes/no)?\n").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. You have just lost.")
    else:
        print("Not a valid option. You have just lost.")

else:
    print("Not a valid option. You have just lost.")

print(f"Thank you for trying {name}")
