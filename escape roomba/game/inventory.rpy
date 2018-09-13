# Setting up the inventory (code referenced from  boneapp and leon's inventory screen)
init -1 python:
    import renpy.store as store
    import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    from operator import attrgetter # we need this for sorting items

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

    # Setting up tooltip style (flavor text when hovering over items)
    # Do we want this in the player text screen or on the menu...?
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

    inventory = Inventory()

    showitems = True #turn True to debug the inventory
    def display_items_overlay():
        if showitems:
            inventory_show = "Inventory: "
            for i in range(0, len(inventory.items)):
                item_name = inventory.items[i].name
                if i > 0:
                    inventory_show += ", "
                inventory_show += item_name

            ui.frame()
            ui.text(inventory_show, color="#000")
    config.overlay_functions.append(display_items_overlay)


screen inventory_button:
    imagebutton auto "show_inventory_%s.png" focus_mask True action [ Show("inventory_screen"), Hide("inventory_button")]

screen inventory_screen:
    add "inventory2.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown

    hbox align (.95,.04) spacing 20:
        imagebutton auto "hide_inventory_%s.png" focus_mask True action [ Hide("inventory_screen"), Show("inventory_button")]
    $ itemnum = 8 # how many items to display on one page
    $ x = 675 # coordinates of the top left item position
    $ y = 85
    $ i = 0
    $ sorted_items = sorted(inventory.items, reverse=True) # sort the items
    $ next_inv_page = inv_page + 1
    if next_inv_page > int(len(inventory.items)/itemnum):
        $ next_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*itemnum and i+1>inv_page*itemnum:
            $ x += 190
            if i%4==0:
                $ y += 170
                $ x = 675 # same as coordinates of top left item
            $ pic = item.image
            # tooltips tell flavor text (but we'll probably change this)
            $ my_tooltip = "tooltip_inventory_" + pic.replace("inv_", "").replace("inv/","").replace(".png", "")
            imagebutton idle pic hover pic xpos x ypos y action [Hide("gui_tooltip"), Show("inventory_button"), SetVariable("item", item), Hide("inventory_screen"), item_use] hovered [ Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) ] unhovered [Hide("gui_tooltip")] at inv_eff

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

    # TOOLTIPS - INVENTORY - FRIDGE

    image tooltip_inventory_cheese_packaged = LiveComposite((665, 173), (590,-112), Text("Packaged Sliced Cheese", style="tips_top"), (590,-80), Text("Nothing fancy. It's just packaged sliced American cheese.", style="tips_bottom"))
    image tooltip_inventory_cheese_opened = LiveComposite((665, 173), (590,-112), Text("Sliced Cheese", style="tips_top"), (590,-80), Text("Unwrapped sliced cheese. I better use it before it touches something weird...", style="tips_bottom"))
    image tooltip_inventory_cheese_shredded = LiveComposite((665, 173), (590,-112), Text("Shredded Cheese", style="tips_top"), (590,-80), Text("I shredded this cheese for a purpose, I think.", style="tips_bottom"))

    image tooltip_inventory_ham_packaged = LiveComposite((665, 173), (590,-112), Text("Packaged Sliced Ham", style="tips_top"), (590,-80), Text("Have a hammy day.", style="tips_bottom"))
    image tooltip_inventory_ham_opened = LiveComposite((665, 173), (590,-112), Text("Sliced Ham", style="tips_top"), (590,-80), Text("Unwrapped sliced ham. I better use it before it touches something weird...", style="tips_bottom"))
    image tooltip_inventory_ham_shredded = LiveComposite((665, 173), (590,-112), Text("Shredded Ham", style="tips_top"), (590,-80), Text("I shredded this ham for a purpose, I think.", style="tips_bottom"))
    image tooltip_inventory_ham_fried = LiveComposite((665, 173), (590,-112), Text("Fried Ham", style="tips_top"), (590,-80), Text("I'm using all of my willpower not to eat this delicious fried ham.", style="tips_bottom"))
    image tooltip_inventory_ham_burnt = LiveComposite((665, 173), (590,-112), Text("Burnt Ham", style="tips_top"), (590,-80), Text("I'm a terrible human being for allowing this travesty to happen to my ham.", style="tips_bottom"))

    image tooltip_inventory_lettuce_head = LiveComposite((665, 173), (590,-112), Text("Head of Lettuce", style="tips_top"), (590,-80), Text("It's a head of lettuce! Not to be confused with a head of cabbage...which is what I once did. That was a sad day.", style="tips_bottom"))
    image tooltip_inventory_lettuce_chopped = LiveComposite((665, 173), (590,-112), Text("Chopped Lettuce", style="tips_top"), (590,-80), Text("A bowl of chopped lettuce.", style="tips_bottom"))
    image tooltip_inventory_lettuce_leaf = LiveComposite((665, 173), (590,-112), Text("Lettuce Leaves", style="tips_top"), (590,-80), Text("Lettuce leaves, like any other vegetable, are supposed to be good for you. That could just be a conspiracy, though.", style="tips_bottom"))

    image tooltip_inventory_milk_carton = LiveComposite((665, 173), (590,-112), Text("Carton of Milk", style="tips_top"), (590,-80), Text("Fresh, 2% fat milk. Thankfully the expiration day is days away from now. Let's not think about the last time I had expired milk.", style="tips_bottom"))
    image tooltip_inventory_milk_glass = LiveComposite((665, 173), (590,-112), Text("Glass of Milk", style="tips_top"), (590,-80), Text("A poured glass of milk. I can use this for cereal...or just drink it, I guess.", style="tips_bottom"))

    image tooltip_inventory_tomato_whole = LiveComposite((665, 173), (590,-112), Text("Whole Tomato", style="tips_top"), (590,-80), Text("A plump, red tomato. It's so juicy!", style="tips_bottom"))
    image tooltip_inventory_tomato_sliced = LiveComposite((665, 173), (590,-112), Text("Tomato Slices", style="tips_top"), (590,-80), Text("Juicy-looking tomato slices. Perfect for a sandwich.", style="tips_bottom"))
    image tooltip_inventory_tomato_diced = LiveComposite((665, 173), (590,-112), Text("Diced Tomatoes", style="tips_top"), (590,-80), Text("Diced tomatoes. I could use these in an omelette.", style="tips_bottom"))