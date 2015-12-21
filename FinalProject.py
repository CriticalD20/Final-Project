one = input("Welcome to the Text-based The Long Night Recreation.")
two = input("A strange electromagnetic storm has crashed your plane in Northern Canada. How long can you survive?")
Time = 0
Freeze = 10

def Wait():
    print("The snow whistles, and the wind whips up your hair as you sit and wait. Sound of the forest can be heard. Howls echo through the trees, and chirps of birds are a rare occurance.")
    
def SeeWolf():
    print("You notice a lupine shape run past a few meters from you. It does not give you a second thought, and quickly leaves your sight.")

def WolfAttack():
    print("You hear howling, as the crunches of multiple paws racing through the snow surround you completely. The eyes of the wolves all around you spell certain death.")

        
def Freeze():
    print("As your vision dims and the cold completely fills your body, you fall, and lay in the snow. You feel tired, and your eyes slowly close. You are dead.")

def House():
    print("As you crest the hill, a small lodge comes into your vision.")

def Nightfall():
    print("The sun slowly drops below the treeline, and the darkness comes. You cannot see very well now, and the forest sounds seem much louder and sharper than normal.")

def North():
    print("You trudge through the snow past trees and small snow-mounds towards North.")
    CardinalChoice()
def South():
    print("You trudge through the snow past trees and small snow-mounds towards South.")
    CardinalChoice()
def East():
    print("You trudge through the snow past trees and small snow-mounds towards East.")
    CardinalChoice()
def West():
    print("You trudge through the snow past trees and small snow-mounds towards West.")
    CardinalChoice
def SearchPlane():
    print("You trudge through the snow to the plane, only to find that the fire does not allow you to access the plane. However, it does seem warmer here.")

def CardinalChoice():
    Cardinal_Direction = input("You check your compass, and you are facing North. What will you do? \n(a) Go North \n(b) Go East \n(c) Go South \n(d) Go West")
three = input("You find yourself in a clearing 200 meters in diameter. It is surrounded by snow-laden conifers, with no buildings in sight.")
four = input("You are standing in the middle next to your downed plane, flames still licking across the chasis, and a rut in the snow leads from the plane to about 40 meters to the right.")
first_choice = input("You check your compass, and you are facing North. What will you do? \n(a) Go North \n(b) Go East \n(c) Go South \n(d) Go West \n(e) Search the Plane \n(f) Wait an hour")
if first_choice.lower == "a":
    Freeze += 1
    Time += 1
    North()
elif first_choice.lower == "b":
    East()
    Time += 1
    Freeze += 1
elif first_choice.lower == "c":
    South()
    Time += 1
    Freeze += 1
elif first_choice.lower == "d":
    West()
    Time += 1
    Freeze += 1
elif first_choice.lower == "e":
    SearchPlane()
    Time += 1
elif first_choice.lower == "f":
    Wait()
    Time += 1
    Freeze += 1
else:
    print("That is not a valid choice. Please resart the program, and make sure not to include anything other than the letter of the choice in the input box.")
