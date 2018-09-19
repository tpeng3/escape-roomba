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

label click:
    $ roomstate = "bark"
    $ renpy.pause(hard=True)

label whodis:
    $ talking = True
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
    wc "Listen up."
    wc "I've only had Roomba-san for one day and and a half,"
    wc "But if anything happened to him I would kill everyone in this room and then myself."
menu:
    lc "(...)" #replace with typing anim later
    "> Yes.":
        lc "lol id lose in a knife fight against roombasan"
        jump seekawayout
    "> No.":
        lc "hey......... bnch"
        jump seekawayout


label end:
    # This ends the game.
    return

