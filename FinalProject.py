one = input("Welcome to the Text-based The Long Night Recreation.\n(Rress Enter)")
two = input("A strange electromagnetic storm has crashed your plane in Northern Canada. How long can you survive? \n(Press Enter)")

Freeze = 5
def Freezing():
    Freeze -= 1
    if Freeze == 0:
        print("The cold overcomes you, and you fall. Your vision darkens as the snow rushes up to meet you. You have died by frostbite.")
        
    else:
        print("The cold is starting to get to you. Find some shelter fast.")
def Wait():
    print("The snow whistles, and the wind whips up your hair as you sit and wait. Sound of the forest can be heard. Howls echo through the trees, and chirps of birds are a rare occurance.")
    Freezing()
    first_choice = input("You check your compass, and you are facing North. What will you do? \n(a) Go North \n(b) Go East \n(c) Go South \n(d) Go West \n(e) Search the Plane \n(f) Wait an hour \nChoice: ")

    if first_choice.lower() == "a":
        North()
    elif first_choice.lower() == "b":
        East()
        Freezing()
    elif first_choice.lower() == "c":
        South()
        Freezing()
    elif first_choice.lower() == "d":
        West()
        Freezing()
    elif first_choice.lower() == "e":
        SearchPlane()
    elif first_choice.lower() == "f":
        Wait()
        Freezing()
        
    else:
        print("That is not a valid choice. Please resart the program, and make sure not to include anything other than the letter of the choice in the input box.")
        
    
def SeeWolf():
    print("You notice a lupine shape run past a few meters from you. It does not give you a second thought, and quickly leaves your sight.")
    Freezing()
    
def WolfAttack():
    print("You hear howling, as the crunches of multiple paws racing through the snow surround you completely. The eyes of the wolves all around you spell certain death.")
    
    Freezing()
    
def House():
    print("As you crest the hill, a small lodge comes into your vision.")
    
    Freezing()
def Nightfall():
    print("The sun slowly drops below the treeline, and the darkness comes. You cannot see very well now, and the forest sounds seem much louder and sharper than normal.")
    
    Freezing()
def North():
    print("You trudge through the snow past trees and small snow-mounds towards North.")
    
    
    Freezing()
def South():
    print("You trudge through the snow past trees and small snow-mounds towards South.")
    
    
    Freezing()
def East():
    print("You trudge through the snow past trees and small snow-mounds towards East.")
    
    
    Freezing()
def West():
    print("You trudge through the snow past trees and small snow-mounds towards West.")
    
    
    Freezing()
def SearchPlane():
    print("You trudge through the snow to the plane, only to find that the fire does not allow you to access the plane. However, it does seem warmer here.")
    Freezing()
def CardinalChoice():
    Cardinal_Direction = input("You check your compass, and you are facing North. What will you do? \n(a) Go North \n(b) Go East \n(c) Go South \n(d) Go West")
    if Cardinal_Direction.lower() == "a":
        North()
        Freezing()
    if Cardinal_Direction.lower() == "b":
        East()
        Freezing()
    if Cardinal_Direction.lower() == "c":
        South()
        Freezing()
    else:
        West()
        Freezing()
three = input("You find yourself in a clearing 200 meters in diameter. It is surrounded by snow-laden conifers, with no buildings in sight.\n(Press Enter)")
four = input("You are standing in the middle next to your downed plane, flames still licking across the chasis, and a rut in the snow leads from the plane to about 40 meters to the right.\n(Press Enter)")
first_choice = input("You check your compass, and you are facing North. What will you do? \n(a) Go North \n(b) Go East \n(c) Go South \n(d) Go West \n(e) Search the Plane \n(f) Wait an hour \nChoice: ")
if first_choice.lower() == "a":
    North()
elif first_choice.lower() == "b":
    East()
    Freezing()
elif first_choice.lower() == "c":
    South()
    Freezing()
elif first_choice.lower() == "d":
    West()
    Freezing()
elif first_choice.lower() == "e":
    SearchPlane()
elif first_choice.lower() == "f":
    Wait()
    Freezing()
else:
    print("That is not a valid choice. Please resart the program, and make sure not to include anything other than the letter of the choice in the input box.")
