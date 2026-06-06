import random
def computer_choice():
    options=['ROCK','PAPER,SCISSORS']
    return random.choice(options)
def determine_winner(user,computer):
    if user==computer:
        return 'tie'
    elif (user=='ROCK' and computer=='SCISSORS') or ( user=='PAPER' and computer=='ROCK') or (user=='SCISSORS' and computer=='PAPER'):
        return 'user'
    else:
        return 'computer'

user_score=0
computer_score=0
winning_score=2
print("Welcome to the Arena: Best of 3---")
while user_score < winning_score:
    print(f"Your score:,{user_score} \n Computer score:,{computer_score}")
    user_choice=input("Enter your choice[ROCK,PAPER,SCISSORS]:")
  #  if user_choice not in ['ROCK','PAPER,SCISSORS']:
   #     print("Invalid Choice! please enter a valid choice")
    comp_choice=computer_choice()
    print(f"Computer Choice:, {comp_choice}")
    result=determine_winner(user_choice,comp_choice)
    if result=='user':
        print("you win the round")
        user_score+=1
    elif result=="computer":
        print("computer wins this round")
        computer_score+=1
    else:
        `print("its a tie")
print("---Game Over---")
if user_score>computer_score:
    print("Congratulations🥳🥳! You Won the match 🏆")
else:
    print("The machines have won the match this time. 🤖🤖")                        