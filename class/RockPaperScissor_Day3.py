
choice = {"r","p","s"}
print("\n****\tRock Paper Scissor Game\t****\n")

comp_score = 0
user_score = 0

print("Rock (r), Paper (p), Scissor (s)")

while True:
    char = input("Play?[y/n]")
    if char == "n":
        break
    print("")
    user = input("Enter your choice: Rock (r)/  Paper (p)/  Scissor (s)").lower()[:1]
    if user not in choice:
        print("\nInvalid")
        continue

    computer = choice[1]
    print("Your Choice:",user, "Computer Choice:", computer,"Your Score:", user_score, "Computer Score:", comp_score)
    if user ==  computer:
        print("Tie")
    elif (user == "r" and computer == "s")or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
        print("You Won\n")
        user_score += 1
    else:
        print("You lose\n")
        comp_score += 1
print("Total Score:")
print("Your Score:", user_score, "Computer Score:", comp_score)
print("Thanks for playing!")
print("****\tGame Over\t****\n")