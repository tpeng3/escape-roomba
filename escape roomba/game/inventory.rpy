# Setting up the inventory (code referenced from  boneapp and leon's inventory screen)
init -1 python:
    # import renpy.store as store
    # import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    # from operator import attrgetter # we need this for sorting items

    inv_page = 0 # initial page of the inventory screen
    item = None

    class Item(store.object):
        def __init__(self, name, player=None, image=""):
            self.name = name
            self.player = player # which character can use this item?
            self.image = image # image file to use for this item

    class Inventory(store.object):
        def __init__(self):
            self.items = []
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)

    def item_use():
        item.use()

    # set up inventory (and possible things to pick up)
    inventory = Inventory()

    ham_packaged = Item("Packaged Sliced Ham", image = "inv/inv_ham_packaged.png")
    tomato_whole = Item("Whole Tomato", image = "images/inventory/tomato_idle.png")


    # Setting up tooltip style (flavor text when hovering over items)
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    style.tips_top.size=24
    style.tips_top.color="#191970"
    style.tips_top.outlines=[(2, "#FFFFFF", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_bottom.size=24
    style.tips_bottom.color="#191970"
    style.tips_bottom.outlines=[(0, "#191970", 0,0)]
    #style.tips_bottom.outlines=[(0, "#155A57", 1, 1), (0, "#155A57", 2, 2)]
    style.tips_bottom.kerning = 2

    style.button.background=Frame("frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000"

    # showitems = True #debug text
    # def display_items_overlay():
    #     if showitems:
    #         inventory_show = "Inventory: "
    #         for i in range(0, len(inventory.items)):
    #             item_name = inventory.items[i].name
    #             if i > 0:
    #                 inventory_show += ", "
    #             inventory_show += item_name

    #         ui.frame()
    #         ui.text(inventory_show, color="#000")
    # config.overlay_functions.append(display_items_overlay)


screen inventory_button:
    hbox align (.95,.04) spacing 20:
        imagebutton auto "images/inventory/show_inventory_%s.png" focus_mask True action [ Show("inventory_screen"), Hide("inventory_button")]

screen inventory_screen:
    # add "inventory2.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown

    hbox align (.95,.04) spacing 20:
        imagebutton auto "images/inventory/hide_inventory_%s.png" focus_mask True action [ Hide("inventory_screen"), Show("inventory_button")]
    $ itemnum = 8 # how many items to display on one page
    $ x = 160 # coordinates of the top left item position
    $ y = 0
    $ i = 0
    $ sorted_items = sorted(inventory.items, reverse=True) # sort the items
    $ next_inv_page = inv_page + 1
    if next_inv_page > int(len(inventory.items)/itemnum):
        $ next_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*itemnum and i+1>inv_page*itemnum:
            $ x += 140
            if i%4==0:
                $ y += 120
                $ x = 160 # same as coordinates of top left item
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("inv_", "").replace("inv/","").replace(".png", "")
            imagebutton idle pic hover pic xpos x ypos y action [Hide("gui_tooltip"), Show("inventory_button"), SetVariable("item", item), Hide("inventory_screen"), item_use] hovered [ Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) ] unhovered [Hide("gui_tooltip")] #at inv_eff

        $ i += 1
        if len(inventory.items)>itemnum:
            imagebutton auto "next_page_%s.png" focus_mask True action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")]

screen gui_tooltip (my_picture="", my_tt_xpos=58, my_tt_ypos=687):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

init -1:
    # $ persistent.endings = 0
    # transform inv_eff: # use ATL to make hovered items super bright
    #     zoom 0.5 xanchor 0.5 yanchor 0.5
    #     on idle:
    #         linear 0.2 alpha 1.0
    #     on hover:
    #         linear 0.2 alpha 2.5
    $ xpos = 0
    $ ypos = 0
    $ tt_xpos = 0
    $ tt_ypos = 0
    $ tt_ypos_end = 0

    # TOOLTIPS
    image tooltip_inventory_ham_packaged = LiveComposite((xpos, ypos), (tt_xpos,tt_ypos), Text("Packaged Sliced Ham", style="tips_top"), (tt_xpos,tt_ypos_end), Text("Have a hammy day.", style="tips_bottom"))
    image tooltip_inventory_tomato_whole = LiveComposite((xpos, ypos), (tt_xpos,tt_ypos), Text("Whole Tomato", style="tips_top"), (tt_xpos,tt_ypos_end), Text("A plump, red tomato. It's so juicy!", style="tips_bottom"))
 