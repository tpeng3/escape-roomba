# The script of the game goes in this file.

# The game starts here.
label start:
    $ roomstate = "blank"
    $ talking = True
    scene black
    show screen room
    show screen phone

    l default "Let's see..."
    l "If there are two guys on the moon, and one killed the other with a rock, would that be fcked up or what?"
menu:
    l "what do I think?"
    "> yea":
        l "not if it's dio"
        $ alert = True
        jump seekawayout
    "> nah we good":
        l "Is that so?"
        jump seekawayout

# default searching label
label seekawayout:
    $ unclickable = False
    $ talking = False
    if alert:
        show alert onlayer screens
    window hide

label click:
    $ roomstate = "bark"
    $ renpy.pause(hard=True)

label whodis:
    $ talking = True
    if selitem == "Whole Tomato":
        l "i fed the doggo a tomato... is that safe...?"
    else:
        $ inventory.add(tomato_whole)
        l "what is that."
        l "that's not {emph}roombasan{/emph}"
    jump seekawayout

# would probably move the chat messages into its own file later
label message:
    $ talking = True
    $ unclickable = True
    $ alert = False
    hide alert onlayer screens
    wc "So here's the plan."
    wc "We gather all the bedsheets and pillows,"
    wc "and build a blanket fort where we can cry about getting trapped in a hotel room."
menu:
    lc "(...)" #replace with typing anim later
    "> Yes.":
        lc "bro........... I'll send roomba-san the goods."
        jump seekawayout
    "> No.":
        lc "tina: yes i got tired of reading the same debugging flavor text jaflkewj"
        jump seekawayout

label hammy:
    l "have a hammy day"
    $ inventory.add(ham_packaged)
    jump seekawayout

label eggy:
    l "why do we egg"
    $ inventory.add(eggs)
    jump seekawayout

label cheesy:
    l "im tired"
    $ inventory.add(cheese)
    jump seekawayout

label te:
    show poop onlayer screens at mid
    l "am i alive?"
    hide poop onlayer screens

label inventory:
    $ renpy.pause(hard=True)

label end:
    # This ends the game.
    return

