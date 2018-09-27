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
    define config.mouse = {
        "default" : [("gui/cursor_default.png", 0, 0)],
        "hover" : [("gui/cursor_hover.png", 0, 0)]
        }

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
        add "images/bg/bg_noborder.png"
        # this is gonna be some walltext code later HOO...
        if roomstate == "bark":
            imagebutton auto "images/bg/genericitem_%s.png" focus_mask True xanchor 0 yanchor 0 xpos 700 ypos 90 mouse "hover" action If(not unclickable, Jump("whodis"))
            imagebutton idle "images/inventory/ham_idle.png" focus_mask True xanchor 0 yanchor 0 xpos 200 ypos 90 mouse "hover" action If(not unclickable, Jump("hammy"))
            imagebutton idle "images/inventory/egg_idle.png" focus_mask True xanchor 0 yanchor 0 xpos 400 ypos 100 mouse "hover" action If(not unclickable, Jump("eggy"))
            imagebutton idle "images/inventory/cheese_idle.png" focus_mask True xanchor 0 yanchor 0 xpos 400 ypos 200 mouse "hover" action If(not unclickable, Jump("cheesy"))
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
        # if selitem is not None:
        #     imagebutton auto "images/side/icon_inv_%s.png"  mouse "hover" action If(not talking, [Show("inventory_screen"), Show("gui_select")]) xalign 0.25 yalign 0.2
        # else:
        imagebutton auto "images/side/icon_inv_%s.png"  mouse "hover" action If(not talking, [Show("inventory_screen"), SetVariable("unclickable", True)]) xalign 0.25 yalign 0.2
        # messenger app
        imagebutton auto "images/side/icon_msg_%s.png" mouse "hover" action If(not talking, [Jump("message")]) xalign 0.75 yalign 0.2
        # settings app
        imagebutton auto "images/side/icon_set_%s.png"  mouse "hover" action If(not talking, [ShowMenu("preferences")]) xalign 0.75 yalign 0.75