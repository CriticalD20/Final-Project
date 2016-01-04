one = input("Welcome to the Text-based The Long Night Recreation.")
two = input("A strange electromagnetic storm has crashed your plane in Northern Canada. How long can you survive?")

Freeze = 5
def Freezing():
    if Freeze = 0:
        print("The cold overcomes you, and you fall. Your vision darkens as the snow rushes up to meet you. You have died by frostbite.")
        
    else:
        print("The cold is starting to get to you. Find some shelter fast.")
def Wait():
    print("The snow whistles, and the wind whips up your hair as you sit and wait. Sound of the forest can be heard. Howls echo through the trees, and chirps of birds are a rare occurance.")
    Freeze -= 1
    Freezing()
    first_choice = input("You check your compass, and you are facing North. What will you do? \n(a) Go North \n(b) Go East \n(c) Go South \n(d) Go West \n(e) Search the Plane \n(f) Wait an hour \nChoice: ")
if first_choice.lower == "a":
    North()
elif first_choice.lower == "b":
    East()
    Freeze += 1
elif first_choice.lower == "c":
    South()
    Freeze += 1
elif first_choice.lower == "d":
    West()
    Freeze += 1
elif first_choice.lower == "e":
    SearchPlane()
elif first_choice.lower == "f":
    Wait()
else:
    print("That is not a valid choice. Please resart the program, and make sure not to include anything other than the letter of the choice in the input box.")
    
    
def SeeWolf():
    print("You notice a lupine shape run past a few meters from you. It does not give you a second thought, and quickly leaves your sight.")
    Freeze -= 1
    
def WolfAttack():
    print("You hear howling, as the crunches of multiple paws racing through the snow surround you completely. The eyes of the wolves all around you spell certain death.")
    
    Freeze -= 1
def Freeze():
    print("As your vision dims and the cold completely fills your body, you fall, and lay in the snow. You feel tired, and your eyes slowly close. You are dead.")
    
    Freeze -= 1
def House():
    print("As you crest the hill, a small lodge comes into your vision.")
    
    Freeze -= 1
def Nightfall():
    print("The sun slowly drops below the treeline, and the darkness comes. You cannot see very well now, and the forest sounds seem much louder and sharper than normal.")
    
    Freeze -= 1
def North():
    print("You trudge through the snow past trees and small snow-mounds towards North.")
    CardinalChoice()
    
    Freeze -= 1
def South():
    print("You trudge through the snow past trees and small snow-mounds towards South.")
    CardinalChoice()
    
    Freeze -= 1
def East():
    print("You trudge through the snow past trees and small snow-mounds towards East.")
    CardinalChoice()
    
    Freeze -= 1
def West():
    print("You trudge through the snow past trees and small snow-mounds towards West.")
    CardinalChoice
    
    Freeze -= 1
def SearchPlane():
    print("You trudge through the snow to the plane, only to find that the fire does not allow you to access the plane. However, it does seem warmer here.")
    Freeze -= 1
def CardinalChoice():
    Cardinal_Direction = input("You check your compass, and you are facing North. What will you do? \n(a) Go North \n(b) Go East \n(c) Go South \n(d) Go West")
    if Cardinal_Direction.lower == "a":
        North()
        Freeze -= 1
    if Cardinal_Direction.lower == "b":
        East()
        Freeze -= 1
    if Cardinal_Direction.lower == "c":
        South()
        Freeze -= 1
    else:
        West()
        Freeze -= 1
three = input("You find yourself in a clearing 200 meters in diameter. It is surrounded by snow-laden conifers, with no buildings in sight.")
four = input("You are standing in the middle next to your downed plane, flames still licking across the chasis, and a rut in the snow leads from the plane to about 40 meters to the right.")
first_choice = input("You check your compass, and you are facing North. What will you do? \n(a) Go North \n(b) Go East \n(c) Go South \n(d) Go West \n(e) Search the Plane \n(f) Wait an hour \nChoice: ")
if first_choice.lower == "a":
    North()
elif first_choice.lower == "b":
    East()
    Freeze += 1
elif first_choice.lower == "c":
    South()
    Freeze += 1
elif first_choice.lower == "d":
    West()
    Freeze += 1
elif first_choice.lower == "e":
    SearchPlane()
elif first_choice.lower == "f":
    Wait()
    Freeze += 1
else:
    print("That is not a valid choice. Please resart the program, and make sure not to include anything other than the letter of the choice in the input box.")
