import timeit
name = input("enter your namr : ")

answer = input("welcome "+name+" would you ike to go on an adventure ? (yes/no)  ").lower()
if not answer == "yes":
    quit()
else:
    print("greet were going to have some fun")

answer = input("you start your quest on the door steps of the forbidden forest\n your path forks left or right ? ").lower()
if answer == "left":
    lake = input("you arrive at alake you can either swim or walk across\n swim/walk ? ").lower()
    if lake == "swim":
        print("you swim besides a log which turns to be a crocodile it closes its teeth around you before you get a chanse to escape")
        quit()
    elif lake == "walk":
        bear = input("you hear the roar of an angry bear as it runs towards you \n will you run or stand and fight\n run/fight ? ").lower()
        if bear == "fight":
            print("stupid you had no chanse bravery isnot every thing your deaaaad !!")
            quit()
        elif bear == "run":
            gate = input("you arrive breathess at a gate you can either cimb or knock\n climb/knock ? ").lower()
            if gate == "climb":
                print("you dont see the golem centurian ubtil he spears throgh the gut")
                quit()
            elif gate == "knock":
                golem = input("a metal spear weilding golem apears before you and asks you a question\n what is the source of happiness?  ").lower()
                if golem == "content":
                    treasure = input("the golem opens the gate you walk into aroom filed with all kind of treasure \n take the treasure or leave it take/leave ? ").lower()
                    if treasure == "take":
                        print("your skin bister and your bone and skin starts to melts and as your dying in agony you hear the golem wistfullly saying \n i guess your not content after all ")
                        quit()
                    elif treasure == "leave":
                        print("the golem laughs and claps you on the back saying\n congratiolation you have passed the test since your aready content there is nothing i can do for you except et you walk with your life")
                        print("congratioation you have finished the game")
                        print(":) :) :) :) :)")

                    else:
                        print("you stare at the treasure for so long that the walls begin to age and crumble and buries you under it")
                        quit()
                else:
                    print("the spear weilding golem kills you with an ak47")
                    quit()
            else:
                print("the bear catches up to you and apparently he was hungry")
                quit()
        else:
            print("when you hesitated a snake bit you and you died in agony")
            quit()

    else:
        print("when you hesitated a snake bit you and you died in agony")
        print("you lose")
        quit()

elif answer == "right":
    cave = input("you stumble across anarrow cave woud you like to crawl through or keep walking on the path crawl/walk?").lower()
    if cave == "walk":
        print("the path leads you out of the forest right were you started you dont feel like going back since its almost supper time")
        print("you lose")
        quit()
    elif cave == "crawl":
        gate = input("you arrive breathess at a gate you can either cimb or knock\n climb/knock ? ").lower()
        if gate == "climb":
            print("you dont see the golem centurian ubtil he spears throgh the gut")
            quit()
        elif gate == "knock":
            golem = input(
                "a metal spear weilding golem apears before you and asks you a question\n what is the source of happiness?  ").lower()
            if golem == "content":
                treasure = input(
                    "the golem opens the gate you walk into aroom filed with all kind of treasure \n take the treasure or leave it take/leave ? ").lower()
                if treasure == "take":
                    print(
                        "your skin bister and your bone and skin starts to melts and as your dying in agony you hear the golem wistfullly saying \n i guess your not content after all ")
                    quit()
                elif treasure == "leave":
                    print(
                        "the golem laughs and caps you on the back saying\n congratiolation you have passed the test since your aready content there is nothing i can do for you except et you walk with your life")
                    print("congratioation you have finished the game")
                    print(":) :) :) :) :)")
                else:
                    print(
                        "you stare at the treasure for so long that the walls begin to age and crumble and buries you under it")
                    quit()
            else:
                print("the spear weilding golem kills you with an ak47")
                quit()
        else:
            print("the bear catches up to you and apparantly he was hungry")
            quit()
    else:
        print("you fall into a bottomless hole and you die of thirst falling")
        print("you lose")
        quit()


else:
    print("when you hesitated a snake bit you and you died in agony")
    quit()