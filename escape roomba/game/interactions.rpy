################################################################################
## Initialization
################################################################################

init offset = -2


################################################################################ 
## Room Objects
################################################################################

init -2:
    $ unclickable = False
    $ talking = False
    $ alert = False

screen room:
    fixed:
        fit_first True
        xanchor 0
        yanchor 0
        xpos 23
        ypos 20
        xmaximum 795
        ymaximum 395

        # bg will change via CASE SWITCHING later aka check dynamic displayables
        add "images/bg/bg_temp.png"
        # this is gonna be some walltext code later HOO...
        if roomstate == "bark":
            imagebutton auto "images/bg/genericitem_%s.png" focus_mask True xanchor 0 yanchor 0 xpos 700 ypos 90 action If(not unclickable, Jump("whodis"))
            # imagebutton auto "images/side/show_recipe_%s.png" focus_mask True xanchor 0 yanchor 0 xpos 900 ypos 90 action Jump("message")
        
        add "images/bg/bg_borders.png"
    


################################################################################ 
## Side Phone Menu
################################################################################

# Set up phone screen
screen phone:
    fixed:
        fit_first True
        xanchor 0
        yanchor 0
        xpos 822
        ypos 21
        xmaximum 235
        ymaximum 395
        # background None

        add "images/side/menu_phone.png"

        # inventory app
        imagebutton auto "images/side/icon_inv_%s.png" focus_mask True action If(not talking, [Show("inventory_screen")]) xalign 0.25 yalign 0.2
        # messenger app
        imagebutton auto "images/side/icon_msg_%s.png" focus_mask True action If(not talking, [Jump("message")]) xalign 0.75 yalign 0.2
        # settings app
        imagebutton auto "images/side/icon_set_%s.png" focus_mask True action If(not talking, [ShowMenu("preferences")]) xalign 0.75 yalign 0.75



# screen inventory_button:
#     hbox align (.95,.04) spacing 20:
#         imagebutton auto "images/inventory/show_inventory_%s.png" focus_mask True action [ Show("inventory_screen"), Hide("inventory_button")]


#screen for side gui
#woggle is defined here so it can be used by the screen

#screen popup:
#    frame:
#        xalign 0.5
#        yalign 0.5
#        ypos 300
#        xpos 400
#        xmaximum 300
#        ymaximum 100
#        textbutton "{size=60}close{/size}" action Hide("popup")
#
#
#screen sidey:
#    zorder 10
#    frame:
#        xanchor 0
#        yanchor 0
#        xpos 793
#        ypos 0
#        xpadding 0
#        ypadding 0
#        background None
#        add "images/side/bg.jpg" xanchor 1.0 yanchor 0 xpos 359 ypos 0
#        add "woggle" xanchor 0 yanchor 0 xpos 0 ypos 0
#
#        if compad == "cool" and resolute == "heckya":
#            add "images/side/compad.png" xanchor 0 yanchor 0 xpos 0 ypos 0
#            add "images/side/resolute.jpg" xanchor 0 yanchor 0 xpos 165 ypos 105
#
#            imagebutton auto "images/side/log_%s.png" xanchor 0 yanchor 0 xpos 174 ypos 136 action Show("popup")
#
#            add spic xanchor 0 yanchor 0 xpos 76 ypos 176
#            viewport id "tex":
#                child_size (222, 315)
#                xanchor 0
#                yanchor 0
#                xpos 80
#                ypos 182
#                xmaximum 231
#                ymaximum 315
#                draggable True
#                mousewheel True
    #
#                vbox:
#                    xmaximum 222
#                    text "{font=pixelmix.ttf}{size=14}{color=#fff9e9}[stxt]{/color}{/size}{/font}"
    #
#            vbar value YScrollValue("tex") ymaximum 315 xanchor 0 yanchor 0 xpos 302 ypos 182 unscrollable "hide"
#
#        elif compad == "cool":
#            add "images/side/compad.png" xanchor 0 yanchor 0 xpos 0 ypos 0
#
#            imagebutton auto "images/side/log_%s.png" xanchor 0 yanchor 0 xpos 174 ypos 136 action Show("popup")
#
#            add spic xanchor 0 yanchor 0 xpos 76 ypos 176
#            viewport id "tex":
#                child_size (222, 315)
#                xanchor 0
#                yanchor 0
#                xpos 80
#                ypos 182
#                xmaximum 231
#                ymaximum 315
#                draggable True
#                mousewheel True
    #
#                vbox:
#                    xmaximum 222
#                    text "{font=pixelmix.ttf}{size=14}{color=#fff9e9}[stxt]{/color}{/size}{/font}"
    #
#            vbar value YScrollValue("tex") ymaximum 315 xanchor 0 yanchor 0 xpos 302 ypos 182 unscrollable "hide"
#
#
#        if braves == "3":
#            add "images/side/b3.png" xanchor 0 yanchor 0 xpos 36 ypos 0
#        elif braves == "2":
#            add "images/side/b2.png" xanchor 0 yanchor 0 xpos 36 ypos 0
#        else:
#            add "images/side/b1.png" xanchor 0 yanchor 0 xpos 36 ypos 0
#
#
#        if fuel == 5:
#            add "images/side/f5.jpg" xanchor 0 yanchor 0 xpos 193 ypos 551
#        elif fuel == 4:
#            add "images/side/f4.jpg" xanchor 0 yanchor 0 xpos 193 ypos 551
#        elif fuel == 3:
#            add "images/side/f3.jpg" xanchor 0 yanchor 0 xpos 193 ypos 551
#        elif fuel == 2:
#            add "images/side/f2.jpg" xanchor 0 yanchor 0 xpos 193 ypos 551
#        elif fuel == 1:
#            add "images/side/f1.jpg" xanchor 0 yanchor 0 xpos 193 ypos 551
#
#
#        if hasmubox:
#            if mubox == "on":
#                imagebutton auto "images/side/onbox_%s.png" xanchor 0 yanchor 0 xpos 275 ypos 0 action Show("popup")
#            else:
#                imagebutton auto "images/side/mubox_%s.png" xanchor 0 yanchor 0 xpos 275 ypos 0 action Show("popup")
#
#        if ia == "sure":
#            imagebutton auto "images/side/item_%s.png" xanchor 0 yanchor 0 xpos 80 ypos 579 action Show("popup")
#            imagebutton auto "images/side/act_%s.png" xanchor 1.0 yanchor 0 xpos 316 ypos 579 action Show("popup")
#        else:
#            add "images/side/lookaroundyou.png" xanchor 0 yanchor 0 xpos 61 ypos 583

#screen p612:
#    ## buttons that code for the bed
#    ## each area is a transparent square... i wonder if theres an easier way
#    button:
#        background None
#        area (151, 386, 162, 119)
#        hovered [ SetVariable("p612_beh", "p612_be h"), SetVariable("stxt", "A bed made of cotton and polyester. \n \nMade for sleeping.") ]
#        unhovered [ SetVariable("p612_beh", "p612_be"), SetVariable("stxt", "Planet 612. \n \nLargely uninhabited, save for a species of plant indigenous only to the planet, and one rabbit.") ]
#        action Jump("p612d_bed")
#    button:
#        background None
#        area (206, 428, 167, 115)
#        hovered [ SetVariable("p612_beh", "p612_be h"), SetVariable("stxt", "A bed made of cotton and polyester. \n \nMade for sleeping.") ]
#        unhovered [ SetVariable("p612_beh", "p612_be"), SetVariable("stxt", "Planet 612. \n \nLargely uninhabited, save for a species of plant indigenous only to the planet, and one rabbit.") ]
#        action Jump("p612d_bed")
#    button:
#        background None
#        area (281, 486, 177, 94)
#        hovered [ SetVariable("p612_beh", "p612_be h"), SetVariable("stxt", "A bed made of cotton and polyester. \n \nMade for sleeping.") ]
#        unhovered [ SetVariable("p612_beh", "p612_be"), SetVariable("stxt", "Planet 612. \n \nLargely uninhabited, save for a species of plant indigenous only to the planet, and one rabbit.") ]
#        action Jump("p612d_bed")
#
#    ## star buttons
#    button:
#        background None
#        area (76, 65, 46, 39)
#        hovered [ SetVariable("p612_sh", "p612_s h"), SetVariable("stxt", "STARSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS") ]
#        unhovered [ SetVariable("p612_sh", "p612_s"), SetVariable("stxt", "Planet 612. \n \nLargely uninhabited, save for a species of plant indigenous only to the planet, and one rabbit.") ]
#        action Jump("p612d_stars")
#
#
#### p612 hover screens
## what's added is actually variables that contain the image name, which is changed depending on if it's hovered over, like above
#screen p612_be:
#    add p612_beh xanchor 0 yanchor 0 xpos 122 ypos 368
#screen p612_s:
#    add p612_sh at uwu
#screen p612_f:    
#    add p612_fh at uwu
#screen p612_bo:
#    add p612_boh xanchor 0 yanchor 0 xpos 456 ypos 390
#screen p612_m:
#    add p612_mh xanchor 0 yanchor 0 xpos 193 ypos 270
#screen p612_ship:
#    add p612_shiph xanchor 0 yanchor 0 xpos 239 ypos 46
