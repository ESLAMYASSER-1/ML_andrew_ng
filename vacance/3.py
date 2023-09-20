import random
C_choice= random.randint(1,3)
M_choice_String= input("choose 'Rock, Paper, scissors'?")

M_choice=1 if M_choice_String.lower() == "rock" else 2 if M_choice_String.lower() == "paper" else 3 if M_choice_String.lower() == "scissors" else 0

print("Computer choice: %s"%("rock"if C_choice==1 else "paper"if C_choice==2 else "scissors" ))
print("Your choice:%s"%(M_choice_String))
if (M_choice == 1 and C_choice == 3) or(M_choice == 2 and C_choice == 1)or(M_choice == 3 and C_choice == 2) :
    print("You win!!")
else:
    print("Computer wins -_-")
