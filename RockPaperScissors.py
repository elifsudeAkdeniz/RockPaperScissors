import random
def rock_paper_scissors_ELIF_SUDE_AKDENIZ(users_score, computers_score):
    if computers_choice == "Rock":
        if users_choice.lower() == "rock":
            print("Draw!")
        elif users_choice.lower() == "paper":
            print("You got the point :)")
            users_score += 1
        elif users_choice.lower() == "scissors":
            print("I got the point :)")
            computers_score += 1

    elif computers_choice == "Paper":
        if users_choice.lower() == "paper":
            print("Draw!")
        elif users_choice.lower() == "scissors":
            print("You got the point :)")
            users_score += 1
        elif users_choice.lower() == "rock":
            print("I got the point :)")
            computers_score += 1

    elif computers_choice == "Scissors":
        if users_choice.lower() == "scissors":
            print("Draw!")
        elif users_choice.lower() == "rock":
            print("You got the point :)")
            users_score += 1
        elif users_choice.lower() == "paper":
            print("I got the point :)")
            computers_score += 1

    print(f"You: {users_score} - Computer: {computers_score}")
    return users_score, computers_score

print("""Rock, Paper, Scissors is a well-known game that can be played by two people. 
The rules are simple: rock crushes scissors, scissors cuts paper, and paper covers rock. 
In this game you will be asked to choose one of the three options.
Whoever wins two rounds wins the game. Good luck!""")
options = ["Rock", "Paper", "Scissors"]
lower_options = ["rock", "paper", "scissors"]
options2 = ["yes", "no"]
computers_score = 0
users_score = 0
round_count = 1
game_count = 1


while True:
    while users_score < 2 and computers_score < 2:
        print("****************************")
        print(f"GAME {game_count} ROUND {round_count}")
        users_choice = input("Rock, Paper, Scissors or exit: ")
        while users_choice.lower() not in lower_options:
            if users_choice.lower() == "exit":
                if round_count == 1:
                    print("Why did you even started the game if you didn't wanted to play??")
                    break
                print("It was fun playing with you! Bye bye")
                break
            print("Invalid entry")
            users_choice = input("Rock, Paper, Scissors or exit: ")
        if users_choice.lower() == "exit":
            break
        computers_choice = random.choice(options)
        print(computers_choice)
        round_count += 1
        users_score, computers_score = rock_paper_scissors_ELIF_SUDE_AKDENIZ(users_score,computers_score)

    game_count += 1
    round_count = 1

    if users_score == 2:
        print("Congratulations!!! You win!")
        print("---------------------------------")
        computers_answer = random.choice(options2)
        users_answer = input("Do you want to play another game? (yes/no): ")
        while users_answer.lower() not in options2:
            print("Invalid entry")
            users_answer = input("Do you wanna play another round? (yes/no): ")
        print("Computers answer: " + computers_answer)
        if computers_answer == "yes" and users_answer.lower() == "yes":
            print("If we both agree, then lets play another round")
        else:
            print("Maybe another time :(")
            break

    elif computers_score == 2:
        print("I WON :)) what a great day to be a winner")
        print("---------------------------------")
        computers_answer = random.choice(options2)
        users_answer = input("Do you want to play another game? (yes/no): ")
        while users_answer.lower() not in options2:
            print("Invalid entry")
            users_answer = input("Do you wanna play another round? (yes/no): ")
        print("Computers answer: " + computers_answer)
        if computers_answer == "yes" and users_answer.lower() == "yes":
            print("If we both agree, then lets play another round")
        else:
            print("Maybe another time :(")
            break

    else:
        break

    users_score = 0
    computers_score = 0





























