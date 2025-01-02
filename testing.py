import random

def run_game():

    print("Welcome to my game!")
    names = ["Avi"]  # Avi is the player
    print("Hello, " + names[0] + "!")
    naughtylist = ["Player"]  # Avi is naughty and should not be kind to him
    print(naughtylist[0] + " you are now on the naughty list" + "!")
    num1 = 10
    num2 = 20
    print("Split those 30$ between " + names[0] + "!")
    Money = 19000
    gamble = 30000
    print("The total money is for a house  is " + str(Money) + "$")
    print("You can make money by working hard at a job or by stealing it.")
    steal = 10000
    work = 200
    print("You can make " + str(steal) + "$ by stealing it from a job but you will have a wanted star.")
    print("You can make " + str(work) + "$ by working hard at a simple job.")
    print("You can also make money by gambling but that is a tricky road.")
    selectedRoad = 0
    # prompt the user for the choice of road
    selectedRoad = int(input("Choose your option (0 for stealing, 1 for working, 2 for gambling, 3 for doing nothing): "))

    if selectedRoad == 0:
        print("You have decided to steal the money and will have a hard life.")
        print("You have now a wanted star and the police can find you.")
        print("You have now " + str(Money + steal) + "$.")
    elif selectedRoad == 1:
        print("You have chosen to work hard at a job which is bad for mental health and you go into debt.")
        print("You have now " + str(Money + work) + "$.")
        moneyreset = Money + work - gamble
        print("You gamble and now have " + str(moneyreset) + "$")

    elif selectedRoad == 2:
        print("You have chosen to gamble and waste away losing moohla.")
        print("You have now " + str(Money + gamble) + "$.")
    elif selectedRoad == 3:
        print("You have chosen to do no job and will be safe but broke.")
        print("You have now " + str(Money) + "$.")

    moneyreset = -300
    broke = -50000

    print("Do you want to continue playing the game?")
    continue_playing = input("Enter 'yes' to continue or 'no' to quit: ").strip().lower()

    if continue_playing == 'yes':
        print("Great! Let's continue the game.")
        # make better here later after done base stufff
    else:
        print("Thank you for playing the game, Adios mi Amigo!")

    if continue_playing == 'yes':
        print("You turn your life around and get an offer for a vet clinic helper.")
        salarymoney = random.randint(15000, 25000) * 4  # Random salary for 4 months between 60000 and 100000
        Money += salarymoney
        print("You have now 4 months salary " + str(salarymoney) + "$. Your total money is now " + str(Money) + "$.")

    # Fix salary issue to be better
    if continue_playing == 'yes':
        print("You have gained money, do you now want to buy a house?")
        buy_house = input("Enter 'yes' to buy a house or 'no' to continue: ").strip().lower()
        if buy_house == 'yes':
            if Money >= 19000:
                Money -= 19000
                Money -= 18800
                Money -= 10800

                print("Congratulations! You have bought a house. You have now " + str(Money) + "$ left.")
            else:
                print("Sorry, you don't have enough money to buy a house. You need 19000$.")
        else:
            print("You chose not to buy a house. You will live in a tent.")
            print("You move into a tent and try to make the best of it.")

        continue_playing = input("Do you want to continue playing the game? Enter 'yes' to continue or 'no' to quit: ").strip().lower()
    print("You move in and it's flooded, what do you do?")
    flood = input("Enter 'yes' to fix the flood or 'no' to continue: ").strip().lower()
    if flood == 'yes':
        Money -= 10000
        print("You have fixed the flood and have now " + str(Money) + "$ left.")
        print("You have now a house and are happy.")
        print("You meet a partner and they want to move in with you.")
        partner_move_in = input("Do you want your partner to move in with you? Enter 'yes' or 'no': ").strip().lower()
        if partner_move_in == 'yes':
            print("Your partner has moved in with you. You are now happy together and no longer alone.")
            print("You have a baby and are now a happy family.")
            keep_baby = input("Do you want to keep the baby? Enter 'yes' to keep or 'no' to not: ").strip().lower()
            if keep_baby == 'yes':
                print("You chose to keep the baby. You are now a happy family.")
                print("You have a baby and are now a happy family.")
                print("Your baby has died from a disease.")
                print("You are now sad and getting divorced.")
                remarry = random.choice(['yes', 'no'])
                if remarry == 'yes':
                    print("You remarry a millionaire and are now rich.")
                else:
                    print("You chose not to remarry and continue living alone.")
                    print("You are now alone and have no one to talk to.")
                    print("You are now sad and alone.")
                    print(" You start to deal weed and are now an adict seeking help.")
                    print("You have now died from getting shot by a oponent dealer.")
                    print("You have died. Game over.")
                    return
            
                print("You re marry a millionaire and are now rich.")
                print("You become drunk one night and decide to gamble.")
                print("Do you gamble or not?")
                gamble_choice = input("Enter 'yes' to gamble or 'no' to not: ").strip().lower()
                if gamble_choice == 'yes':
                    gamble_amount = random.randint(1000, 5000)
                    Money += gamble_amount
                    print("You chose to gamble and won " + str(gamble_amount) + "$. Your total money is now " + str(Money) + "$.")
                    print("Your partner has found out and is now mad at you.")
                    print("They get a gun and shoot you in the head.")
                    print("You have died. Game over.")
                    return
                else:
                    print("You chose not to gamble. Your total money remains " + str(Money) + "$.")
                    print("The next day you gamble.")
                    gamble_result = random.choice(['win', 'lose'])
                    if gamble_result == 'win':
                        gamble_amount = random.randint(1000, 5000)
                        Money += gamble_amount
                        gamble_result = random.choice(['win', 'lose'])
                        if gamble_result == 'win':
                            gamble_amount = random.randint(1000, 5000)
                            Money += gamble_amount
                            print("You chose to gamble and won " + str(gamble_amount) + "$. Your total money is now " + str(Money) + "$.")
                        else:
                            gamble_amount = random.randint(1000, 5000)
                            Money -= gamble_amount
                            print("You chose to gamble and lost " + str(gamble_amount) + "$. Your total money is now " + str(Money) + "$.")
                        print("You are now insanly rich and you and your partner move to the bahamas.")
                        print("You are now in the bahamas and now want another baby..")
                        print("You have another baby and are now a happy family.")
                        print("You have started a great car company and are now happy.")
                        print("You have been in a car crash.")
                        print("Your family survives and all become monks living the rich life.")
                        print("You have succeeded. Game over, good.")
                        return
                    else:
                        gamble_amount = random.randint(1000, 5000)
                        Money -= gamble_amount
                        print("You chose to gamble and lost " + str(gamble_amount) + "$. Your total money is now " + str(Money) + "$.")
                        print("Your partner becomes abuseive and you are now in a abusive relationship.")
                        print("You seek help and are now in a shelter.")
                        print("You are now in a shelter and now become a meth adict.")
                        print("You have died from a overdose.")
                        print("You have died. Game over.")
                        return
            else:
                print("You chose not to keep the baby. You continue living with your partner.")
                print("You dont have a baby and are now a happy couple.")
                print("Your partner cheats on you and has a baby with someone else.")
                print("You are now sad and getting divorced.")
                print("You hate your partner and want to kill them.")
                kill_partner = input("Do you want to kill your partner? Enter 'yes' or 'no': ").strip().lower()
                if kill_partner == 'yes':
                    print("You have killed your partner with a old meat cleaver. You are in jail.")
                    print(" A gaurd walks by and you grab his pistol and shoot him in the head.")
                    print("BANG! BANG! BANG!""Blood is everywhere, you watch your life unravel.")
                    print("You get shot by another officer and die.")
                    print("You have died. Game over.")
                    return
        else:
            print("You chose not to let your partner move in. You continue living alone.")
            print("You break up with your partner and are now alone.")
            print("You are now alone and have no one to talk to.")
            print("You are now sad and alone.")
            print(" You start to drink and are now an alcoholic seeking help.")
            print("You have now died from alcohol poisoning.")
            print("You have died. Game over.")

run_game()
