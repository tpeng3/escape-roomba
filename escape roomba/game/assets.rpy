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

# Script style shortcuts
init python:

    def emph_tag(tag, argument, contents):
        color = "#FAA293"
        return [
                (renpy.TEXT_TAG, u"color="+color),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]

    config.custom_text_tags["emph"] = emph_tag


# Declare Leika
# if we want voice beeps haha
init python: 
    def l_beep(event, **kwargs):
            if event == "show":
                renpy.music.play("music/voice/leika.wav", channel="bleeps", loop=True)
            elif event == "slow_done" or event == "end":
                renpy.music.stop(channel="bleeps")

define l = Character("Leika", image="leika", vspace=2, who_color="#fff")

define lc = Character("Leika", kind=nvl, what_suffix="{fast}", what_color="#000", who_size=18, who_color="000", window_background="gui/frame2.png")
define wc = Character("Witch2", kind=nvl, what_suffix="{fast}", what_color="#000", who_size=18, who_color="000", window_background="gui/frame.png")

define lsame = Character("", kind=nvl, what_suffix="{fast}", what_color="#000", window_background="gui/frame2.png")
define wsame = Character("", kind=nvl, what_suffix="{fast}", what_color="#000", window_background="gui/frame.png")

#to add voice bleeps, just add `callback=l_beep`
#to add ctc, add in `ctc="ctc_arrow",`

# Leika face expressions go here
image side leika default = "images/sprite/side_leika_default.png"

#**Underscores_ in image declarations are optional but I just like them more haha...

# Declare background images
image bg_temp = "images/bg/bg_temp.png"

# Declare items
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


# Declare cgs
image cg_meeting = "images/cg/cg_meeting.png"

# Declare music
define audio.opening = "music/tam_music/tamco10.ogg"

# Declare sfx
define audio.alarm = "music/sounds/250629__kwahmah-02__alarm1.mp3"
