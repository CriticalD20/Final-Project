
one = input("Welcome to the Text-based The Long Night Recreation.\n(Press Enter)")
two = input("A strange electromagnetic storm has crashed your plane in Northern Canada. How long can you survive? \n(Press Enter)")

Freeze = 8
def FirstChoice():
    first_choice = input("You check your compass, and you are facing North. What will you do? \n(a) Go North \n(b) Go East \n(c) Go South \n(d) Go West \n(e) Search the Plane \n(f) Wait an hour \nChoice: ")
    if first_choice.lower() == "a":
        Freezing()
        North()
    elif first_choice.lower() == "b":
        Freezing()
        East()
 
    elif first_choice.lower() == "c":
        Freezing()
        South()
    
    elif first_choice.lower() == "d":
        Freezing()
        West()
    
    elif first_choice.lower() == "e":
        SearchPlane()
        
    elif first_choice.lower() == "f":
        Freezing()
        Wait()
    
def Freezing():
    Freeze -= 1
    if Freeze == 0:
        printz = input("The cold overcomes you, and you fall. Your vision darkens as the snow rushes up to meet you. You have died by frostbite.")
        
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
        
def Nothing():
    print("As you trudge through the woods, nothing seems out of the ordinary.")
    Freezing()
    CardinalChoice2()
def CardinalChoice2():
    printt = input("You sense of direction has been lost from walking through the woods. Which direction would you like to try to go?\n(a) North\n(b) East\n(c) South\n(d) West \nChoice:")
    if printt == "a":
        Freezing()
        SeeWolf()
    elif printt.lower() == "b" :
        Freezing()
        CardinalChoice2()
    elif printt.lower() == "c":
        Freezing()
        CardinalChoice2()
    elif printt.lower() == "d":
        Freezing()
        CardnialChoice2()
    else:
        print("That is not a valid choice. Please resart the program, and make sure not to include anything other than the letter of the choice in the input box.")
def PossibleWolf2():
    choiceW = input("After seeing the wolf you come to a clearing. Which direction would you like to go?\n(a) North\n(b) East\n(c) South\n(d) West")
    if choiceW.lower == "a":
        print("You trudge through the snow past trees and small snow-mounds towards North.")
        Freezing()
        WolfAttack()
    elif choiceW == "b":
        print("You trudge through the snow past trees and small snow-mounds towards East.")
        House()
    elif choiceW == "c":
        print("You trudge through the snow past trees and small snow-mounds towards South.")
        Freezing()
        WolfAttack()
    elif choiceW == "d":
        print("You trudge through the snow past trees and small snow-mounds towards West.")
        Freezing()
        WolfAttack()
    else:
        print("That is not a valid choice. Please resart the program, and make sure not to include anything other than the letter of the choice in the input box.")
def PossibleWolf():
    choiceZ = input("After seeing the wolf you come to a clearing. Which direction would you like to go?\n(a) North\n(b) East\n(c) South\n(d) West")
    if choicez.lower == "a":
        print("You trudge through the snow past trees and small snow-mounds towards North.")
        Freezing()
        WolfAttack()
    elif choicez == "b":
        print("You trudge through the snow past trees and small snow-mounds towards East.")
        Freezing()
        WolfAttack()
    elif choicez == "c":
        print("You trudge through the snow past trees and small snow-mounds towards South.")
        Freezing()
        WolfAttack()
    elif choicez == "d":
        print("You trudge through the snow past trees and small snow-mounds towards West.")
        Freezing()
        PossibleWolf2()
    else:
        print("That is not a valid choice. Please resart the program, and make sure not to include anything other than the letter of the choice in the input box.")
def SeeWolf():
    Freezing
    print("You notice a lupine shape run past a few meters from you. It does not give you a second thought, and quickly leaves your sight.")
    CardinalChoice2()
def WolfAttack():
    print("You trudge through the snow, and all of a sudden a noise break the silence. You hear howling, as the crunches of multiple paws racing through the snow surround you completely. The eyes of the wolves all around you spell certain death.")
    
def House():
    print("As you crest the hill, a small lodge comes into your vision. You race towards the warmth and your only way of survival.")
    WIN = input("You have completed the Text-Based The Long Night Recreation Game. Congratulations! Don't tell your friends how to win though   ;D")
def North():
    print("You trudge through the snow past trees and small snow-mounds towards North.")
    Freezing()
    CardnialCHoice2
def South():
    print("You trudge through the snow past trees and small snow-mounds towards South.")
    Freezing()
    SeeWolf()
def East():
    print("You trudge through the snow past trees and small snow-mounds towards East.")
    Freezing()
    CardinalChoice2()
def West():
    print("You trudge through the snow past trees and small snow-mounds towards West.")
    Freezing()
   CardinalChoice2()
def SearchPlane():
    print("You trudge through the snow to the plane, only to find that the fire does not allow you to access the plane. However, it does seem warmer here.")
    FirstChoice()
def CardinalChoice():
    Cardinal_Direction = input("You check your compass, and you are facing North. What will you do? \n(a) Go North \n(b) Go East \n(c) Go South \n(d) Go West")
    if Cardinal_Direction.lower() == "a":
        Freezing()
        North()
        
    elif Cardinal_Direction.lower() == "b":
        Freezing()
        East()
        
    elif Cardinal_Direction.lower() == "c":
        Freezing()
        South()
        
    elif Cardinal_Direction.lower() == "d":
        Freezing()
        West()
    else:
        print("That is not a valid choice. Please resart the program, and make sure not to include anything other than the letter of the choice in the input box.")
three = input("You find yourself in a clearing 200 meters in diameter. It is surrounded by snow-laden conifers, with no buildings in sight.\n(Press Enter)")
four = input("You are standing in the middle next to your downed plane, flames still licking across the chasis, and a rut in the snow leads from the plane to about 40 meters to the right.\n(Press Enter)")
first_choice = input("You check your compass, and you are facing North. What will you do? \n(a) Go North \n(b) Go East \n(c) Go South \n(d) Go West \n(e) Search the Plane \n(f) Wait an hour \nChoice: ")
if first_choice.lower() == "a":
    Freezing()
    North()
elif first_choice.lower() == "b":
    Freezing()
    East()
 
elif first_choice.lower() == "c":
    Freezing()
    South()
    
elif first_choice.lower() == "d":
    Freezing()
    West()
    
elif first_choice.lower() == "e":
    SearchPlane()
    
elif first_choice.lower() == "f":
    Freezing()
    Wait()
    
else:
    print("That is not a valid choice. Please resart the program, and make sure not to include anything other than the letter of the choice in the input box.")
