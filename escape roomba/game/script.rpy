# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    
    # uwu is the shorthand for 0,0,0,0 position
    $ uwu = Position(xanchor=0, yanchor=0, xpos=0, ypos=0)
    image c = "images/sprite/c.png"
    image c h = "images/sprite/c hell.png"

    image p612 = "images/bg/p612/base.jpg"
    image p612_f:
        "images/bg/p612/f1.png"
        0.5
        "images/bg/p612/f2.png"
        0.5
        repeat
    image p612_f h = "images/bg/p612/f3.png"
    image p612_s:
        "images/bg/p612/s1.png"
        0.6
        "images/bg/p612/s2.png"
        0.6
        repeat
    image p612_s h = "images/bg/p612/s3.png"
    image p612_be = "images/bg/p612/bed.png"
    image p612_be h = "images/bg/p612/bed h.png"
    image p612_m:
        "images/bg/p612/mbox.png"
        0.4
        "images/bg/p612/mbox1.png"
        0.4
        repeat
    image p612_m h = "images/bg/p612/mbox h.png"
    image p612_bo = "images/bg/p612/books.png"
    image p612_bo h = "images/bg/p612/books h.png"
    image p612_sm:
        "images/bg/p612/smoke1.png"
        0.7
        "images/bg/p612/smoke2.png"
        0.7
        repeat
    image ship = "images/bg/ship.png"
    image ship h = "images/bg/ship h.png"
    
define c = Character("Carmen")


# The game starts here.

label start:
    #has music box
    $ hasmubox = False
    # music box on = on
    $ mubox = "nope"
    # item/action, on = sure
    $ ia = "nah"
    # has compad
    $ compad = "cool"
    # resolute status, on = heckya
    $ resolute = "notyet"
    # brave level
    $ braves = "2"
    # fuel level
    $ fuel = 6
    #call the side gui
    $ spic = "images/side/com/blank.png"
    $ stxt = ""

    # only used at the start
    $ startcompad = "no"

    # variables for the p612 screens to enable hovering, those are image names
    $ p612_beh = "p612_be"
    $ p612_sh = "p612_s"
    $ p612_fh = "p612_f"
    $ p612_boh = "p612_bo"
    $ p612_mh = "p612_m"
    $ p612_shiph = "ship"
    
    # beginning screen that starts with nothing showing
    show screen fakey
    scene p612 at uwu
    show p612_sm at uwu
    show p612_f at uwu
    show p612_s at uwu
    #i hate these long position things i wonder if there's a better way to shorten it so i don't have to copy paste it all the time
    show p612_bo at Position(xanchor=0, yanchor=0, xpos=456, ypos=390)
    show p612_be at Position(xanchor=0, yanchor=0, xpos=122, ypos=368)
    show p612_m at Position(xanchor=0, yanchor=0, xpos=193, ypos=270)
    show ship at Position(xanchor=0, yanchor=0, xpos=239, ypos=46)
    with dissolve

    show c at left
    with dissolve

    c "Let's see..."
    # "cool" is just like. a true. bad coding practice probably...
    $ startcompad = "cool"
    c "ComPad, here."
    $ fuel = 5
    c "Fuel, filled."
    c "Food and water, packed."
    c "Spaceship, ready to go."
    c "Hmmm... I think that's everything."
    c "My first space expedition... I hope everything goes okay..."
    c "(dev note: only the bed and one star is interactable rn)"

    hide screen fakey
    #normal side screen where everything is already there
    show screen sidey
    with None

label p612s:
    # For some reason after clicking on an object it shows the hovered image? so
    # these are here to reset it...
    $ p612_beh = "p612_be"
    $ p612_sh = "p612_s"
    $ p612_fh = "p612_f"
    $ p612_boh = "p612_bo"
    $ p612_mh = "p612_m"
    $ p612_shiph = "ship"
    # stxt is side text that displays When Not Hovering Over Anything
    $ stxt = "Planet 612. \n \nLargely uninhabited, save for a species of plant indigenous only to the planet, and one rabbit."
    hide c at left
    window hide
    with dissolve
    hide p612_f at uwu
    hide p612_s at uwu
    hide p612_bo at Position(xanchor=0, yanchor=0, xpos=456, ypos=390)
    hide p612_be at Position(xanchor=0, yanchor=0, xpos=122, ypos=368)
    hide p612_m at Position(xanchor=0, yanchor=0, xpos=193, ypos=270)
    hide ship at Position(xanchor=0, yanchor=0, xpos=239, ypos=46)
    # above i'm hiding the static images, below i'm showing the Real Deal that interact when hovered over... for now it's just the bed tho
    show screen p612_s
    show screen p612_f
    show screen p612_bo
    show screen p612_be
    show screen p612_m
    show screen p612_ship
    show screen p612
    $ renpy.pause(hard=True)

label p612d_bed:
    $stxt = "A bed made of cotton and polyester. \n \nMade for sleeping."
    hide screen p612_s
    hide screen p612_f
    hide screen p612_bo
    hide screen p612_be
    hide screen p612_m
    hide screen p612_ship
    hide screen p612
    show p612_f at uwu
    show p612_s at uwu
    show p612_bo at Position(xanchor=0, yanchor=0, xpos=456, ypos=390)
    show p612_be at Position(xanchor=0, yanchor=0, xpos=122, ypos=368)
    show p612_m at Position(xanchor=0, yanchor=0, xpos=193, ypos=270)
    show ship at Position(xanchor=0, yanchor=0, xpos=239, ypos=46)
    window show
    show c at left
    c "Oh my god! It's a bed! Wow!"
    c "DUDE MY BRAIN IS SO FRIED I CAN'T EVEN THINK OF DIALOGUE ANYMORE"
    jump p612s

label p612d_stars:
    $stxt = "STARSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS"
    hide screen p612_s
    hide screen p612_f
    hide screen p612_bo
    hide screen p612_be
    hide screen p612_m
    hide screen p612_ship
    hide screen p612
    show p612_f at uwu
    show p612_s at uwu
    show p612_bo at Position(xanchor=0, yanchor=0, xpos=456, ypos=390)
    show p612_be at Position(xanchor=0, yanchor=0, xpos=122, ypos=368)
    show p612_m at Position(xanchor=0, yanchor=0, xpos=193, ypos=270)
    show ship at Position(xanchor=0, yanchor=0, xpos=239, ypos=46)
    window show
    show c at left
    c "THEY'RE STARS!!!!!!!!!!!!!!!!!!!!!!!!!!"
    c "I LOVE THEM! WOW!"
    jump p612s




    # This ends the game.

    return