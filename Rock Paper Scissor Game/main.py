import random 
item_list = ["rock", "paper", "scissor"]

user_choice = input("What do you choose? Type 'rock', 'paper' or 'scissor': ").lower()
comp_choice = random.choice(item_list)

print(f"user choice: {user_choice} , computer choice: {comp_choice}")

if user_choice == comp_choice:
    print("It's a draw!")
    
elif user_choice == "rock":
    if comp_choice == "paper":
        print("Paper covers Rock Computer Win")
    else:
        print("Rock smashes Scissor You win")
        
elif user_choice == "paper":
    if comp_choice == "scissor":
        print("Scissor cuts Paper Computer Win")
    else:
        print("Paper covers Rock You win")   
             
elif user_choice == "scissor":
    if comp_choice == "rock":
        print("Rock smashes Scissor Computer Win")
    else:
        print("Scissor cuts Paper You win")