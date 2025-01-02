import random

print("Welcome to the game of Life")
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"]

print("Choose your name:")
for i, name in enumerate(names, 1):
    print(f"{i}. {name}")

choice = int(input("Enter the number corresponding to your name: "))

if 1 <= choice <= len(names):
    player_name = names[choice - 1]
    print(f"Welcome, {player_name}!")
else:
    print("Invalid choice. Please restart the game and choose a valid number.")
    exit()

print("Thank you for choosing a name. Now choose a career.")
careers = ["Doctor", "Engineer", "Artist", "Scientist", "Teacher", "Lawyer", "Musician", "Athlete"]

print("Choose your career:")
for i, career in enumerate(careers, 1):
    print(f"{i}. {career}")

career_choice = int(input("Enter the number corresponding to your career: "))

if 1 <= career_choice <= len(careers):
    player_career = careers[career_choice - 1]
    print(f"Congratulations, {player_name}! You have chosen to be a {player_career}.")
    print("You get $200 to start out.")
    total_money = 200
else:
    print("Invalid choice. Please restart the game and choose a valid number.")
    exit()

print(f"Now, {player_name}, it's time to start your job as a {player_career}.")
# Add job starting logic here
if player_career == "Doctor":
    print("You start working at the hospital, treating patients.")
elif player_career == "Engineer":
    print("You start working at a tech company, developing new software.")
elif player_career == "Artist":
    print("You start creating beautiful paintings and sculptures.")
elif player_career == "Scientist":
    print("You start conducting experiments in the lab.")
elif player_career == "Teacher":
    print("You start teaching students in a school.")
elif player_career == "Lawyer":
    print("You start working at a law firm, defending clients.")
elif player_career == "Musician":
    print("You start composing and performing music.")
elif player_career == "Athlete":
    print("You start training and competing in sports events.")
else:
    print("Unknown career. Please restart the game and choose a valid career.")

print(f"{player_name} is now starting their first day as a {player_career}.")
print("You walk into work and get started helping a co-worker with a task.")
print("Nice job, you already have made a friend!")

# Ask if the user wants their salary now
salary_choice = input("Do you want to receive your salary now? (yes/no): ").strip().lower()

if salary_choice == "yes":
    print(f"Congratulations, {player_name}! You have received your first salary as a {player_career}.")
    total_money += 200
    print("+ $200")
    print(f"Your total bank account is currently ${total_money}")
else:
    print(f"Alright, {player_name}. You can receive your salary later.")
    print("You have received $10 as a small advance.")
    total_money += 10
    print(f"Your total bank account is currently ${total_money}")

# Ask if the user wants to go home or keep working
print("\nWhat would you like to do next?")
print("1. Keep working")
print("2. Go home")

next_choice = int(input("Enter the number corresponding to your choice: "))

if next_choice == 1:
    print(f"{player_name} continues working as a {player_career}.")
    print("You complete more tasks and gain more experience.")
    total_money += 200
    print("+ $200")
    if random.choice([True, False]):
        total_money += 10
        print("+ $10 bonus")
    print("Then you go home and rest.")
    print(f"Your total bank account is ${total_money}.")
elif next_choice == 2:
    print(f"{player_name} decides to go home and rest.")
    print(f"Your total bank account amount is ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")

print("1. Wake up early and go to work")
print("2. Sleep in and take the day off")

wakeup_choice = int(input("Enter the number corresponding to your choice: "))

if wakeup_choice == 1:
    print(f"{player_name} wakes up early and heads to work as a {player_career}.")
    total_money += 200
    print("+ $200")
    if random.choice([True, False]):
        total_money += 10
        print("+ $10 bonus")
    print(f"Your total bank account is now ${total_money}.")
elif wakeup_choice == 2:
    print(f"{player_name} decides to sleep in and take the day off.")
    print(f"Your total bank account remains ${total_money}.")
    print("Your Boss gets mad and doesnt give you any cash bonuses.")
else:
    print("Invalid choice. Please choose a valid option.")

print("1. Get day's salary.")
print("2. Get day's salary and ask for bonus.")

salary_day_choice = int(input("Enter the number corresponding to your choice: "))

if salary_day_choice == 1:
    total_money += 200
    print(f"{player_name} receives the day's salary of $200.")
    print(f"Your total bank account is now ${total_money}.")
elif salary_day_choice == 2:
    total_money += 200
    print(f"{player_name} receives the day's salary of $200 and asks for a bonus.")
    print("Your boss is impressed with your work and gives you a $100 bonus.")
    total_money += 100
    print(f"Your total bank account is now ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")

print("You decide to buy a house and stop living with your Mom.")
print("\nWould you like to buy a house?")
print("1. Yes")
print("2. No")
housebuy_choice = int(input("Enter the number corresponding to your choice: "))

if housebuy_choice == 1:
    if total_money >= 500:
        print(f"Congratulations, {player_name}! You have enough money to buy a house.")
        total_money -= 500
        print("- $500")
        print(f"You have successfully bought a house. Your remaining balance is ${total_money}.")
    else:
        print(f"Sorry, {player_name}. You do not have enough money to buy a house. You need $500 but you only have ${total_money}.")
elif housebuy_choice == 2:
    print(f"{player_name} decides not to buy a house right now.")
    print(f"Your total bank account remains ${total_money}.")
    print("You can still purchase a house later.")
else:
    print("Invalid choice. Please choose a valid option.")

print("\nWould you like to buy a car?")
print("1. Yes")
print("2. No")

try:
    carbuy_choice = int(input("Enter the number corresponding to your choice: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if carbuy_choice == 1:
    if total_money >= 200:
        print(f"Congratulations, {player_name}! You have enough money to buy a car.")
        total_money -= 300
        print("- $300")
        print(f"You have successfully bought a car. Your remaining balance is ${total_money}.")
    else:
        print(f"Sorry, {player_name}. You do not have enough money to buy a car. You need $300 but you only have ${total_money}.")
elif carbuy_choice == 2:
    print(f"{player_name} decides not to buy a car right now.")
    print(f"Your total bank account remains ${total_money}.")
    print("You can still purchase a car later.")
else:
    print("Invalid choice. Please restart the game and choose a valid option.")
    exit()

print("You are driving home and you hit another driver.")
print("They want to sue you for reckless driving.")
print("1. Settle out of court for $100")
print("2. Fight the case in court")

carcrash_choice = int(input("Enter the number corresponding to your choice: "))

if carcrash_choice == 1:
    if total_money >= 100:
        total_money -= 100
        print(f"You settled out of court for $100. Your remaining balance is ${total_money}.")
    else:
        print(f"You don't have enough money to settle. Your balance is ${total_money}.")
elif carcrash_choice == 2:
    print("You decided to fight the case in court. The outcome is uncertain.")
    if random.choice([True, False]):
        print("You won the case! No money lost.")
    else:
        print("You lost the case and have to pay $200 in damages.")
        if total_money >= 300:
            total_money -= 200
            print(f"Your remaining balance is ${total_money}.")
        else:
            print(f"You don't have enough money to pay the damages. Your balance is ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")

print("\nWould you like to try for a job rank up?")
print("1. Yes")
print("2. No")

rankup_choice = int(input("Enter the number corresponding to your choice: "))

if rankup_choice == 1:
    print(f"{player_name} decides to try for a job rank up.")
    if random.choice([True, False]):
        print("Congratulations! You have been promoted.")
        total_money += 1000
        print("+ $300 salary increase")
        print(f"Your total bank account is now ${total_money}.")
    else:
        print("Unfortunately, you did not get the promotion this time.")
        print(f"Your total bank account remains ${total_money}.")
elif rankup_choice == 2:
    print(f"{player_name} decides not to try for a job rank up right now.")
    print(f"Your total bank account remains ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")

print("\nWould you like to buy a used sports car for $150?")
print("Its a 1996 Bmw Z4 coupe spyder with a turbochargered v4 engine.")
print("Its worth it the seller tells you.")
print("1. Yes")
print("2. No")

try:
    sports_car_choice = int(input("Enter the number corresponding to your choice: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if sports_car_choice == 1:
    if total_money >= 150:
        print(f"Congratulations, {player_name}! You have enough money to buy a used sports car.")
        total_money -= 150
        print("- $150")
        print(f"You have successfully bought a used sports car. Your remaining balance is ${total_money}.")
    else:
        print(f"Sorry, {player_name}. You do not have enough money to buy a used sports car. You need $150 but you only have ${total_money}.")
elif sports_car_choice == 2:
    print(f"{player_name} decides not to buy a used sports car right now.")
    print(f"Your total bank account remains ${total_money}.")
    print("You can still purchase a used sports car later.")
else:
    print("Invalid choice. Please choose a valid option.")

# Finding a partner and moving in
print("\nYou meet someone special and they ask if they can move in with you.")
print("1. Yes")
print("2. No")

partner_choice = int(input("Enter the number corresponding to your choice: "))

if partner_choice == 1:
    print(f"{player_name} decides to let their partner move in.")
    print("You both share expenses and save money.")
    total_money += 100
    print("+ $100")
    print(f"Your total bank account is now ${total_money}.")
elif partner_choice == 2:
    print(f"{player_name} decides not to let their partner move in right now.")
    print(f"Your total bank account remains ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")

print ("You get older and realise you want to have a kid before you get to old.")
print("Your partner wants to have a baby but only if it is a boy.")
print("You decide to have a baby.")
baby_gender = random.choice(["boy", "girl"])

if baby_gender == "boy":
    print("Congratulations! You have a baby boy.")
    print("You and your partner celebrate extremly happy about this news!")
    total_money -= 100
    print("- $100 for baby expenses")
    print(f"Your total bank account is now ${total_money}.")
else:
    print("Congratulations! You have a baby girl.")
    total_money -= 100
    print("- $100 for baby expenses")
    print(f"Your total bank account is now ${total_money}.")
    print("Your partner is initially disappointed but grows to love your baby girl.")
    print("Your partner realises a baby is a baby and is happy no matter the child.")
    print("\n")

print ("As you are heading to work one day you hit a slipperly patch on the road and skidout crashing into a tree.")
print("You are rushed to the hospital and have 1 broken leg, and a shattered rib.")
print("The hospital bill is $500.")

total_money -= 500
print("- $500 for hospital bill")
print("Luckliy you have insurance and only have to pay $100 and your boss feels bad and gives you 200$.")
total_money -= 100
total_money += 600
print("+ $200 from boss")
print(f"Your total bank account is now ${total_money}.")    
print("\n")  
print("Your aunt Lindaa dies and leaves you $1000 in her will, making you be able to buy a new car for yourself.")
total_money += 1000
print("You buy a 2012 lecuxus RX 350 for $500.")
total_money -= 500
print("- $500 for car")
print(f"Your total bank account is now ${total_money}.")
print("\n")


print("You decide to take a vacation to the Bahamas.")
print("You spend $500 on the trip.")
total_money -= 500
print("- $500 for vacation")
print(f"Your total bank account is now ${total_money}.")
print("\n")

print("\nWould you like to take a $500 loan?")
print("1. Yes")
print("2. No")

try:
    loan_choice = int(input("Enter the number corresponding to your choice: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if loan_choice == 1:
    print(f"{player_name} decides to take a $500 loan.")
    total_money += 500
    print("+ $500")
    print(f"Your total bank account is now ${total_money}.")
    print("Remember, you will need to pay back the loan with interest.")
elif loan_choice == 2:
    print(f"{player_name} decides not to take a loan right now.")
    print(f"Your total bank account remains ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")

# Player receives a salary of $3000
print(f"{player_name}, you receive a salary of $3000.")
total_money += 3000
print("+ $3000")
print(f"Your total bank account is now ${total_money}.")

# Pay back the loan if taken
if loan_choice == 1:
    print("It's time to pay back your $500 loan with $50 interest.")
    if total_money >= 550:
        total_money -= 550
        print("- $550")
        print(f"Your loan has been paid off. Your remaining balance is ${total_money}.")
    else:
        print("You don't have enough money to pay back the loan. You need $550.")

# Ask if the player wants to move into a nice middle-class house
print("\nWould you like to move into a nice middle-class house for $1000?")
print("1. Yes")
print("2. No")

try:
    house_move_choice = int(input("Enter the number corresponding to your choice: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if house_move_choice == 1:
    if total_money >= 1000:
        print(f"Congratulations, {player_name}! You have enough money to move into a nice middle-class house.")
        total_money -= 1000
        print("- $1000")
        print(f"You have successfully moved into a nice middle-class house. Your remaining balance is ${total_money}.")
    else:
        print(f"Sorry, {player_name}. You do not have enough money to move into a nice middle-class house. You need $1000 but you only have ${total_money}.")
elif house_move_choice == 2:
    print(f"{player_name} decides not to move into a nice middle-class house right now.")
    print(f"Your total bank account remains ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")
    print("\n")

# Player decides to invest in the stock market
print("\nWould you like to invest in the stock market?")
print("1. Yes")
print("2. No")
print("3. I don't know")

stock_choice = int(input("Enter the number corresponding to your choice: "))
if stock_choice == 1:
    print(f"{player_name} decides to invest in the stock market.")
    stock_investment = random.randint(0, 1000)
    total_money += stock_investment
    print(f"You invested ${stock_investment} in the stock market.")
    print(f"Your total bank account is now ${total_money}.")
elif stock_choice == 2:
    print(f"{player_name} decides not to invest in the stock market right now.")
    print(f"Your total bank account remains ${total_money}.")
elif stock_choice == 3:
    print(f"{player_name} is unsure about investing in the stock market.")
    print(f"Your total bank account remains ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")
    print("\n")

print("Somehow you get a promotion and a raise of $500.")
total_money += 500
print("+ $500")
print(f"Your total bank account is now ${total_money}.")
print("\n")
print("You are driving down the road and you see a Porchse 911 for sale for 300$")
print("Luckily the guy happily trades you the car for your old Lexus 350 with a 100$ price.")
total_money -= 100
print("- $100 for car trade")
print(f"Your total bank account is now ${total_money}.")
print("You realize the car has a turbocharged V6 engine and is worth $5000.")

print("\nWould you like to sell the engine for $5000?")
print("1. Yes")
print("2. No")

try:
    sell_engine_choice = int(input("Enter the number corresponding to your choice: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if sell_engine_choice == 1:
    print(f"{player_name} decides to sell the engine for $5000.")
    total_money += 5000
    print("+ $5000")
    print(f"Your total bank account is now ${total_money}.")
elif sell_engine_choice == 2:
    print(f"{player_name} decides not to sell the engine right now.")
    print(f"Your total bank account remains ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")
    print("\n")

print("As you are driving down the road you see a 2020 Tesla Model S for sale for 500$")
print("Happy to see such a great deal you dont pay attention to the road and crash into a pedestrian family killing the 2 daughters and the mother.")
print("\n") 
print("You are arrested and charged with manslaughter.")
print("You are sentenced to 10 years in prison.")
print("You lose all your money and your house.")
print("You are left with nothing.")
print("\n")



# After serving your sentence, you are released from prison
print("You get out of jail after serving your sentence.")
print("You decide to start your life over with a fresh start.")
total_money = 0
print(f"Your total bank account is now ${total_money}.")
print("\n")

print("\nWhat would you like to do next?")
print("1. Work at Burger King")
print("2. Become homeless")

next_choice = int(input("Enter the number corresponding to your choice: "))

if next_choice == 1:
    print(f"{player_name} decides to work at Burger King.")
    print("You start earning a small salary and slowly rebuild your life.")
    total_money += 100
    print("+ $100")
    print(f"Your total bank account is now ${total_money}.")
elif next_choice == 2:
    print(f"{player_name} becomes homeless.")
    print("You struggle to find food and shelter.")
    print("Life is tough, but you try to survive each day.")
    print("You have no money and no home.")
    print("You are left with nothing.")
    print("Game Over.")
else:
    print("Invalid choice. Please choose a valid option.")

print("After working at Burgerkind you manage to make 400$, enough to buy a used minivan to sleep in.")
print("\nWould you like to buy a used minivan for $400 to sleep in?")
print("1. Yes")
print("2. No")

try:
    minivan_choice = int(input("Enter the number corresponding to your choice: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if minivan_choice == 1:
    if total_money >= 400:
        print(f"Congratulations, {player_name}! You have enough money to buy a used minivan.")
        total_money -= 400
        print("- $400")
        print(f"You have successfully bought a used minivan. Your remaining balance is ${total_money}.")
        print("You now have a place to sleep and keep your belongings.")
    else:
        print(f"Sorry, {player_name}. You do not have enough money to buy a used minivan. You need $400 but you only have ${total_money}.")
elif minivan_choice == 2:
    print(f"{player_name} decides to keep sleeping in the old shelter.")
    print(f"Your total bank account remains ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")
    print("/n")

print("Life goes on and you meet a person who you fall in love with and slowly get married.")
print("Its not fancy but you get married at court and do your honeymoon at the local beach motel.")
print("You are happy and content with your life.")
print("You have a small job and a small house.")
print("You are happy.")
print("/n")

print("You decide to get a lottery ticket and you win 20000$.")
total_money += 20000
print("+ $20000")
print(f"Your total bank account is now ${total_money}.")
print("/n")

print("\nWould you like to buy a nice house in a rich area for $7000?")
print("1. Yes")
print("2. No")

try:
    rich_house_choice = int(input("Enter the number corresponding to your choice: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if rich_house_choice == 1:
    if total_money >= 7000:
        print(f"Congratulations, {player_name}! You have enough money to buy a nice house in a rich area.")
        total_money -= 7000
        print("- $7000")
        print(f"You have successfully bought a nice house in a rich area. Your remaining balance is ${total_money}.")
    else:
        print(f"Sorry, {player_name}. You do not have enough money to buy a nice house in a rich area. You need $7000 but you only have ${total_money}.")
elif rich_house_choice == 2:
    print(f"{player_name} decides not to buy a nice house in a rich area right now.")
    print(f"Your total bank account remains ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")

print("\nWould you like to buy a new BMW X5 Competition for $3000?")
print("1. Yes")
print("2. No")

try:
    bmw_choice = int(input("Enter the number corresponding to your choice: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if bmw_choice == 1:
    if total_money >= 3000:
        print(f"Congratulations, {player_name}! You have enough money to buy a new BMW X5 Competition.")
        total_money -= 3000
        print("- $3000")
        print(f"You have successfully bought a new BMW X5 Competition. Your remaining balance is ${total_money}.")
    else:
        print(f"Sorry, {player_name}. You do not have enough money to buy a new BMW X5 Competition. You need $3000 but you only have ${total_money}.")
elif bmw_choice == 2:
    print(f"{player_name} decides not to buy a new BMW X5 Competition right now.")
    print(f"Your total bank account remains ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")
    print("\n")

print("You start to drive on the highway and see a guy in a Dodge Charger Hellcat wanting to race for $1000.")
print("Do you want to race?")
print("1. Yes")
print("2. No")

try:
    race_choice = int(input("Enter the number corresponding to your choice: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if race_choice == 1:
    print(f"{player_name} decides to race the Dodge Charger Hellcat.")
    if random.choice([True, False]):
        print("Congratulations! You won the race and earned $1000.")
        total_money += 1000
        print("+ $1000")
    else:
        print("Unfortunately, you lost the race and had to pay $1000.")
        total_money -= 1000
        print("- $1000")
    print(f"Your total bank account is now ${total_money}.")
elif race_choice == 2:
    print(f"{player_name} decides not to race the Dodge Charger Hellcat.")
    print(f"Your total bank account remains ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")
    print("\n")

print("You decide to take a vacation to Hawaii.")
print("You spend $2000 on the trip.")
total_money -= 2000
print("- $2000 for vacation")
print(f"Your total bank account is now ${total_money}.")
print("\n")

print("You decide to buy a new house in the countryside for $5000.")
total_money -= 5000
print("- $5000 for house")
print(f"Your total bank account is now ${total_money}.")
print("The house is beautiful and has a large garden but you realise how your going into debt.")
print("\n")

print("\nWould you like to work at a car dealership?")
print("1. Yes")
print("2. No")

try:
    dealership_choice = int(input("Enter the number corresponding to your choice: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if dealership_choice == 1:
    print(f"{player_name} decides to work at a car dealership.")
    print("You start earning a commission on each car you sell.")
    total_money += 500
    print("+ $500")
    print(f"Your total bank account is now ${total_money}.")
elif dealership_choice == 2:
    print(f"{player_name} decides not to work at a car dealership right now.")
    print(f"Your total bank account remains ${total_money}.")
else:
    print("Invalid choice. Please choose a valid option.")
    print("\n")

print("You decide to buy a new Tesla Model 3 for $4000 because your Bmw breaks down for good.")
total_money -= 4000
print("- $4000 for car")
print("trade in your old Bmw for 3500$")
total_money += 3500
print("+ $3500 for trade in")
print(f"Your total bank account is now ${total_money}.")
print("\n")

print("You sell a ford mustang for 50000$ and get a 9000$ commission.")
total_money += 9000
print("+ $9000")
print(f"Your total bank account is now ${total_money}.")
print("\n")


















 
    
