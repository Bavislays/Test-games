print("Welcome to the Abyss.")

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

Begin = ("Welcome to the Abyss.")

       

print("""
      Do you dare enter the Abyss?
      ("Well it not up to you, you are already here.") 
        ("You are standing in a dark room, you can't see anything.")
 ("You can hear the sound of water dripping.")
      ("You can smell the dampness in the air.")
    ("You hear a voice in the distance, it is calling your name.")
("You can't see anything, but you can feel the presence of something.)
   (Its feel like its looking at you.")
   ("You can feel the fear creeping up on you.")
     ("What do you do?")... 

      """)

print("Press 1 to run, 2 to hide, and 3 to yell.")

action = int(input("Enter your action: "))

if action == 1:
    print("""
          
          You decide to run. You stumble through the darkness, trying to find a way out.")
   ("You trip over something and fall to the ground.")
  ("You hear a low growl in the darkness.")
    ("And then you feel sharp teeth sinking into your flesh.")
        ("And then you wake up.
          
        """)
elif action == 2:
    print("You decide to hide. You crouch down and try to make yourself as small as possible.")
    print("You hear footsteps approaching.")
    print("You hold your breath, trying to stay silent.")
    print("The footsteps pass by, and you breathe a sigh of relief.")
    print("You wait for what feels like an eternity, but nothing else happens.")
    print("You look around and relize you are not alone.")
    print("You can see the eyes of a creature looking at you.")
    print("And then you wake up.")
elif action == 3:
    print("You decide to yell. Your voice echoes through the darkness, but there is no response.")
    print("You yell again, louder this time.")
    print("You hear a low growl in the darkness.")
    print("You feel something brush against your leg.")
    print("You feel sharp teeth sinking into your flesh.")
    print("And then you wake up.")
else:
    print("Invalid action. Please restart the game and choose a valid action.")

print("You wake up in a cold sweat, your heart pounding in your chest.")
print("You look around and see that you are safe in your own bed.")
print("It was just a dream.")
print("Or was it?")

print("You look down at your watch and see that it is 3:33 AM.")
print("You shiver, feeling a chill run down your spine.")
print("You try to shake off the feeling of dread that clings to you.")
print("You tell yourself that it was just a dream, nothing more.")
print("But deep down, you know that something is not right.")
print("You know that the Abyss is waiting for you.")
print("And it won't be satisfied with just a dream.")
print("You fall back asleep and wake up at 9:00 AM.")
print("You go about your day, trying to forget about the dream.")
print("But the feeling of unease lingers, like a shadow at the edge of your vision.")
print("You try to push it away, but it won't go.")
print("You know that you will have to face the Abyss again.")
print("And this time, it won't be a dream.")
print("It will be real.")
print("And it will be waiting for you.")
print("You turn a corner and see a dark figure looking at you but somethings seems off about them.")
print("You feel a chill run down your spine.")
print("They run towards you and you feel a sharp pain in your chest.")

print("Press 1 to scream, 2 to run, and 3 to fight.")


action = int(input("Enter your action: "))
if action == 1:
    print("You scream, but no sound comes out.")
    print("The figure reaches you and you feel a sharp pain in your chest.")
    print("And then you don't wake up.")
    print("You are now in the Abyss.")
    print("You are standing in a dark room, surrounded by your family and friends.")
    print("They are all looking at you with sad eyes.")
    print("You feel a sense of dread wash over you.")
    print("You see them start to fade away, one by one.")
    print("And then you are alone.")


elif action == 2: 
    print("You run, but the figure is faster.")
    print("You feel a sharp pain in your chest.")
    print("And then you dont wake up.")
    print("You are sitting in your office chair at Albertsson Hansen Architecture ")
    print("You see your boss walking towards you.")
    print("He looks angry.")
    print("He starts yelling at you, but you can't hear what he is saying.")
    print("You feel a sharp pain in your chest.")
    print("You fall over and wake up in the Abyss again.")
    print("You see a little girl standing in front of you.")
    print("She is holding a teddy bear.")
    print("she opens her mouth and you see rows of horriblly sharp teeth.")
    print("You feel a sharp pain in your chest.")
    print("And then you are alone.")

elif action == 3:
    print("You fight back, but the figure is too strong.")
    print("You feel a sharp pain in your chest.")
    print("And then you wake up.")

    print("This time, you don't wake up in your bed.")
    print("You wake up in the Abyss.")
    print("You are standing in a dark room, surrounded by darkness.")
    print("You can't see anything, but you can feel the presence of something.")
    print(" All of a sudden your standing on 81 Vine St, Seattle.")
    print("You see your friends and family standing in front of you about 50 feet away.")
    print("They are all looking at you with sad eyes.")
    print("You feel a sense of dread wash over you.")
    print("You see them start to fade away, one by one.")
    print("And then you are alone.")

   
    print("You realize that you are trapped in the Abyss.")
    print("Press 1 to stay in the Abyss, 2 to try to leave.")

    final_action = int(input("Enter your action: "))

    if final_action == 1:
        print("You decide to stay in the Abyss.")
        print("You know that you will never escape.")
        print("You know that you will be alone forever.")
        print("You know that you will never wake up.")
        print("You know that you are lost.")
        print("And you know that you are doomed.")
        print("You feel a sharp pain in your chest.")
        print("You realize that the only way out is to get woken up by someone else in the real world.")
        print("You hear your phone ring and then you answer")
        print("It tells you to close your eyes.")
        print("You wake up in a van speeding down the freeway chained to the wall.")
    elif final_action == 2:
        print("You decide to try to leave the Abyss.")
        print("You focus all your willpower on waking up.")
        print("You feel a sharp pain in your chest.")
        print("And then you wake up in your bed, gasping for air.")
        print("You look around and see that you are safe.")
        print("It was just a dream you tell yourself.")
        print("But deep down, you know that the abyss is still waiting for you.")
        print(" Suddenly you are in a van speeding down the freeway chained to the wall.")
    else:
        print("Invalid action. Please restart the game and choose a valid action.")
print("Thank you for playing the Abyss.")


print("Press 1 to try to jump out of the van, 2 to stay inside.")

van_action = int(input("Enter your action: "))

if van_action == 1:
    print("You decide to try to jump out of the van.")
    print("You struggle against the chains, but they are too strong.")
    print("You feel a sharp pain in your chest.")
    print("You the realise your on the side of the road.")

if van_action == 2:
    print("You stay inside the van as you turn onto a bumpy road.")
    print("You here the doors unlocking and the doors open.")
