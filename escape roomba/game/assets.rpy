# This file is for declaring assets and variables.
# Right now the stuff I'm declaring here are just random variables from onm, you can delete them later but it's just a good reference as a template

# Declare gui shortcuts
transform mid:
    xalign 0.5
    yalign 0.35

transform bg_corner:
    xalign 0.1
    yalign 0.1

transform uwu: #for you reddo
    xanchor 0
    yanchor 0
    xpos 0
    ypos 0

image ctc_arrow:
    "gui/continue.png" #continue.png does not exist rn, make one later?
    0.75
    "gui/continue2.png"
    0.75
    repeat

image im = "gui/overlay/item_menu.png"

# Declare Leika
# if we want voice beeps haha
init python: 
    def l_beep(event, **kwargs):
            if event == "show":
                renpy.music.play("music/voice/leika.wav", channel="bleeps", loop=True)
            elif event == "slow_done" or event == "end":
                renpy.music.stop(channel="bleeps")

define l = Character("Leika", image="leika", vspace=2, who_color="#fff")
#to add voice bleeps, just add `callback=l_beep`
#to add ctc, add in `ctc="ctc_arrow",`

# Leika face expressions go here
image side leika default = "images/sprite/side_leika_default.png"

#**Underscores_ in image declarations are optional but I just like them more haha...

# Declare background images
image bg_temp = "images/bg/bg_temp.png"

# Declare items

# Declare cgs
image cg_meeting = "images/cg/cg_meeting.png"

# Declare music
define audio.opening = "music/tam_music/tamco10.ogg"

# Declare sfx
define audio.alarm = "music/sounds/250629__kwahmah-02__alarm1.mp3"
