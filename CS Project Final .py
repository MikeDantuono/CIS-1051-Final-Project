




def comicquest():
    print("You are now playing comicquest, this game will take you on an adventure with you being the deciding factor of how long you play and what choices you make!")
    print("You wake up in your bed. Enter A to continue lying in bed or enter B to get up.")
    user = input("Enter a letter A or B:")
    if user.upper() == "A":
        print("You stayed in bed most of the day watching videos on your phone. THE END!")
    if user.upper() == "B":
        print("After you get out of bed you go outside and can not decide whether you want to go for a walk in the park or in the city. Enter A to walk in the city or B to walk in the park.")
        scene1 = input("Enter A or B:")
        if scene1.upper() == "A":
            print("You walk through the city for a while, visiting your local bookstore, coffee shop, and pizza place when all of a sudden a ferocious dragon appears. You approach the area and see someone facing it with a sword. You have two Choices enter A to pick up sword and attack dragon or enter B to let the hero attack the dragon.")
            scene1a = input("Enter A or B:")
            if scene1a.upper() == "A":
                print("Once you see an opening to attack you have one of four options: Enter A: Attack it’s tail, Enter B: Attack it’s throat, Enter C: Attack it’s claw, Enter D: Hand the sword over to someone else and let them fight it.")
                scene2 = input("Enter A,B,C or D:")
                if scene2.upper() == "A":
                    print("The dragon was hurt by your attack but quickly noticed you and burnt you to ash.THE END!")
                if scene2.upper() == "B":
                    print("The dragon was slain in one mighty stab to the throat. After the death of the dragon you were awarded with fame, fortune and notoriety  beyond your wildest dreams. You became the hero by the Alias: “Dragon Slayer”")
                if scene2.upper() == "C":
                    print("The dragon was hurt by your attack but quickly noticed you and burnt you to ash.THE END!")
                if scene2.upper() == "D":
                    print("You hand the sword to another person but they run away in fear and as a result the whole city gets burned down by the dragon. Headlines from a neighboring city read, “Fool Gives Sword to a Coward, City Burned by Dragon”, THE END!")
            if scene1a.upper() == "B":
                print("The hero attacks the ferocious dragon but is suddenly hurt by a blast of fire!")
                print("You see this and have to react fast. Enter A if you want to attack the dragon or enter B if you want to run.")
                scene3 = input("Enter A or B:")
                if scene3.upper() == "A":
                    print("Once you see an opening to attack you have one of four options: Enter A: Attack it’s tail, Enter B: Attack it’s throat, Enter C: Attack it’s claw, Enter D: Hand the sword over to someone else and let them fight it.")
                    scene3a = input("Enter A,B,C or D:")
                    if scene3a.upper() == "A":
                        print("The dragon was hurt by your attack but quickly noticed you and burnt you to ash. THE END!")
                    if scene3a.upper() == "B":
                        print("The dragon was slain in one mighty stab to the throat. After the death of the dragon you were awarded with fame, fortune and notoriety  beyond your wildest dreams. You became the hero by the Alias: “Dragon Slayer” THE END!")
                    if scene3a.upper() == "C":
                        print("The dragon was hurt by your attack but quickly noticed you and burnt you to ash. THE END!")
                    if scene3a.upper() == "D":
                        print("You hand the sword to another person but they run away in fear and as a result the whole city gets burned down by the dragon. Headlines from a neighboring city read, “Fool Gives Sword to a Coward, City Burned by Dragon”, THE END!")
                if scene3.upper() == "B":
                    print("You were a coward and ran away. Now your whole city will burn to the ground. THE END!")

        if scene1.upper() == "B":
            print("As you walk around the park you see a group of people playing basketball. You can enter A to play with them or B to keep walking.")
            scene4 = input("Enter A or B:")
            if scene4.upper() == "A":
                print("You played basketball and made friends! THE END!")
            if scene4.upper() == "B":
                print("As you continue your walk, you see a chihuahua seemingly abandoned. You want to approach it to see its collar, but chihuahuas are vicious. Enter A to approach chihuahua or B to keep walking")
                scene5 = input("Enter A or B:")
            if scene5.upper() == "A":
                print("The chihuahua attacks! You punt the chihuahua across the field. THE END!")
            if scene5.upper() == "B":
                print("You walk past the chihuahua into the forest and you encounter a sword stuck inside of a stone. Enter A to try and pull the sword or enter B to do push ups to get stronger before pulling the sword.")
                scene6 = input("Enter A or B:")
                if scene6.upper() == "A":
                    print("You attempted to pull the sword but you are to weak and broke your back. THE END!")
                if scene6.upper() == "B":
                    count = int(input("Enter amount of pushups to do so you can lift the sword. Be careful if you do to little push ups you may still be to weak!"))
                    if count >= 10:
                        print("You picked up the sword!")
                        print("As you pick up the sword you see a dragon attacking the city. With no hesitation you run to the city to try and help. In the city you find the dragon causing havoc and it is doing immense damage to the city. Once you see an opening to attack you have one of four options, Choice A: Attack it’s tail, Choice B: Attack it’s throat, Choice C: Attack it’s claw, Choice D: Let someone else fight it")
                        scene7 = input("Enter A,B,C,or D:")
                        if scene7.upper() == "A":
                            print("The dragon was hurt by your attack but quickly noticed you and burnt you to ash. THE END!")
                        if scene7.upper() == "B":
                            print("The dragon was slain in one mighty stab to the throat. After the death of the dragon you were awarded with fame, fortune and notoriety  beyond your wildest dreams. You became the hero by the Alias: “Dragon Slayer” THE END!")
                        if scene7.upper() == "C":
                            print("The dragon was hurt by your attack but quickly noticed you and burnt you to ash. THE END!")
                        if scene7.upper() == "D":
                            print("You hand the sword to another person but they run away in fear and as a result the whole city gets burned down by the dragon. Headlines from a neighboring city read, “Fool Gives Sword to a Coward, City Burned by Dragon”, THE END!")       
                    else:
                        print("You broke your back attempting to pull the sword!THE END!")

run = True
while run == True:
    comicquest()
    restart = input("\nWould you like to play again (Y/N):\t")
    if restart.upper() == "N" or restart.upper() == "NO":
        print("Thank you for playing")
        run = False
    elif restart.upper() == "Y" or restart.upper() == "YES":
        run = True
    else:
        print("Invalid entry, the game is over")
        run = False
