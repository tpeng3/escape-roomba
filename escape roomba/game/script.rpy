# The script of the game goes in this file.

# init:
#     # uwu is the shorthand for 0,0,0,0 position
#     $ uwu = Position(xanchor=0, yanchor=0, xpos=0, ypos=0)

# The game starts here.
label start:
    # #has music box
    # $ hasmubox = False
    # # music box on = on
    # $ mubox = "nope"
    # # item/action, on = sure
    # $ ia = "nah"
    # # has compad
    # $ compad = "cool"
    # # resolute status, on = heckya
    # $ resolute = "notyet"
    # # brave level
    # $ braves = "2"
    # # fuel level
    # $ fuel = 6
    # #call the side gui
    # $ spic = "images/side/com/blank.png"
    # $ stxt = ""

    # # only used at the start
    # $ startcompad = "no"

    $ roomstate = "blank"
    scene black
    show screen room
    show screen phone

    l default "Let's see..."
    l "If there are two guys on the moon, and one killed the other with a rock, would that be fcked up or what?"

label click:
    $ roomstate = "bark"
    $ renpy.pause(hard=True)

label whodis:
    l "what is that."
    l "that's not roombasan"

    # This ends the game.
    return
