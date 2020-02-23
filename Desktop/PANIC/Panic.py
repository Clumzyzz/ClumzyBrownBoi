import pygame

#player name = Big D
#player attack = 20
#player health = 250
#player = [ "Big D, 20, 250"]

player = {"name": "Big D", "attack": 20, "health": 250}

#player2 name = BOSS
#player2 attack = 30
#player2 health = 500
#player2 = [ "BOSS, 30, 500"]

player2 = {"name": "BOSS", "attack": 10, "health": 300}

#player3 name = Militia
#player3 attack = 15
#player3 health = 150
#player3 = [ "Militia, 15, 150"]

player3 = {"name": "Militia", "attack": 15, "health": 150}

#player4 name = Vladmir
#player4 attack = 100
#player4 health = 1000

player4 = {"name": "Vladmir", "attack": 100, "health": 1000}


player_choice = input('Enter your choice [1-2] : ')
player_choice=int(player_choice)
print("Please select action")
print("1) Flee")
print("2) Help")
    
while True:
    
    if player_choice == 1:
        print("Sucks")       
    elif player_choice == 2:
        while True:
            
            player_choice2 = input('Enter your choice[3-4]:')
            print("3) Start on the first level")
            print("4) Or fight a really hard boss")
            print(player_choice2)
            
            if player_choice2 == "3":

                print("You have tickled the boss")
                player2["health"] = player2["health"] - player["attack"]
                print(player2["health"])
                print("Boss is pissed that have you insulted his manliness")
                print("Boss punches you in the balls")
                print("Big D throws up")
                player["health"] = player["health"] - player2["attack"]
                print(player["health"])

            if player["health"] <=0:
                print("Well you're dead")
                game_running = False
            
            if player2["health"] <=0:
                print("Well you actually beat him congrats, but I am not gonna let you get away with this")
                game_running = False
                                
            elif player_choice2 == "4":

                print("Well you just avoided the hardest boss and you are playing the actual game")
                print("After an hour you finally find a victim")
                
                print("1) Do you wish to attack this person")
                print("2) Do you wish to be a pussy cat and not attack this person")
                
            else:
                print("Please try again") 
            
            
        player_choice3 = input("Enter your choice [1-2]:")
            
        print(player_choice3)
            
        if player_choice3 == "1":

            print("Well thank for not being pussy cat and actually fighting somebody")
            player3["health"] = player3["health"] - player["attack"]
            print(player3["health"])
            print("Well Big D actually managed to get a good hit in")
            print("The guy hits you back")
            player["health"] = player["health"] - player3["attack"]
            print(player["health"])
            print(" Wow the guy is actually weaker than Big D, that's really sad")
                
        if player["health"] <=0:
            print("well you are not the clown you are the entire circus")
            game_running = False
            
        if player3["health"] <=0:
            print(" Well don't be too happy he is the easiest boss in the game")
            game_running = False
            
        elif player_choice3 == "2":

            print("Well since you were a pussy cat you are being punished, you are now fighting the hardest character in the game, Vladmir")
            player["health"] = player["health"] - player4["attack"]
            print(player["health"])
            print("I told you to not be a pussy cat now look what happens")
            print("Big D tries to attack back")
            player4["health"] = player4["health"] - player["attack"]
            print(player4["health"])
            print("YOU DID NOT LISTEN, KNOW DIE!!!!")

        if player["health"] <=0:
            print("You get what you deserve")
            game_running = False

        if player4["health"] <=0:
            print("Congrats PSYCHE!")
            game_running = False
                    
            



                  
