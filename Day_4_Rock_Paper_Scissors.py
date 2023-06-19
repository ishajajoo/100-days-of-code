import random


print("What do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

you_chose = int(input("0/1/2\n"))
match you_chose:
    case 0:
        print(f"You chose rock {rock}")
    case 1:
        print(f"You chose paper {paper}")
    case 2: 
        print(f"You chose scissors {scissors}")

system_chose = random.randint(0, 2)
match system_chose:
    case 0:
        print(f"Computer chose rock {rock}")
        if you_chose==system_chose:
            print("It's a draw")
        elif you_chose=='scissors':
            print("Computer wins!")
        else:
            print("You win")

    case 1:
        print(f"Computer chose paper {paper}")
        if you_chose==system_chose:
            print("It's a draw")
        elif you_chose=='scissors':
            print("Computer wins")
        else:
            print("You win")
    case 2: 
        print(f"Computer chose scissors {scissors}")
        if you_chose==system_chose:
            print("It's a draw")
        elif you_chose=='paper':
            print("Computer wins")
        else:
            print("You win")