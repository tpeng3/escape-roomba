# Setting up the inventory (code referenced from  boneapp and leon's inventory screen)
init -1 python:
    import copy

    inv_page = 0 # initial page of the inventory screen
    selitem = None
    sel_xpos = None
    sel_ypos = None

    class Item(store.object):
        def __init__(self, name, player=None, image="", recipeItem=None):
            self.name = name
            # self.player = player # which character can use this item?
            self.image = image # image file to use for this item
            self.selected = False
            self.recipeItem = recipeItem

        def use(self):
            if self in inventory.selected_items:
                inventory.selected_items.remove(self)
            else:
                inventory.selected_items.append(self)

    class Inventory(store.object):
        def __init__(self):
            self.items = []
            self.selected_items = []
            self.event_text = None
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            if item.recipeItem is not None:
                self.event_text = item.recipeItem
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)
        
    class Recipe(store.object):
        def __init__(self, items=[], item_created=None):
            self.items = items
            self.item_created = item_created
        def combine_check(self):
            correct_recipe_items = copy.copy(self.items)
            for item in inventory.selected_items:
                if item in correct_recipe_items:
                    correct_recipe_items.remove(item)
                if not (item in self.items):
                    too_many = True
            if len(correct_recipe_items) == 0:
                inventory.add(self.item_created)
                for drop_item in self.items:
                    inventory.drop(drop_item)
            inventory.selected_items = []

    # set up inventory (and possible things to pick up)
    inventory = Inventory()

    ham_packaged = Item("Packaged Sliced Ham", image = "images/inventory/ham")
    cheese = Item("Cheese Packet", image = "images/inventory/cheese")
    tomato_whole = Item("Whole Tomato", image = "images/inventory/tomato")
    eggs = Item("Dozen of Eggs", image = "images/inventory/egg")
    eggs_and_tomato = Item("Eggs and Tomato", image = "images/inventory/te", recipeItem = "te")

    recipes = [Recipe([eggs, tomato_whole], eggs_and_tomato)]

init python:
    def combine_items():
        if len(inventory.selected_items) == 2:
            for recipe in recipes:
                recipe.combine_check()
        return

    def check_success():
        flag = "te"
        if inventory.event_text is not None:
            flag = inventory.event_text
            inventory.event_text = None
        return flag

    # def display_items_overlay():
    #     inventory_show = "Selected: "
    #     if selitem is not None:
    #         inventory_show += selitem
    #     ui.frame()
    #     ui.text(inventory_show, color="#000")
    # config.overlay_functions.append(display_items_overlay)

    # def display_combine_overlay():
    #     inventory_show = "Selected Combo: "
    #     for item in inventory.selected_items:
    #         inventory_show += item.name
    #         inventory_show += ", "
    #     ui.frame()
    #     ui.text(inventory_show, color="#000")
    # config.overlay_functions.append(display_combine_overlay)


screen inventory_screen:
    modal True #prevent clicking on other stuff when inventory is shown

    add "gui/nvl.png" xanchor 0 yanchor 0 xpos 23 ypos 20

    hbox xanchor 0 yanchor 0 xpos 822 ypos 21:
        imagebutton auto "images/side/menu_inv_%s.png" focus_mask True action [Hide("inventory_screen"), Hide("gui_select")]

    hbox xanchor 0 yanchor 0 xpos 22 ypos 21:
        imagebutton idle "images/inventory/button_deselect.png" focus_mask True action [SetVariable("selitem", None)]

    hbox xanchor 0 yanchor 0 xpos 22 ypos 100:
        imagebutton idle "images/inventory/button_combine.png" focus_mask True action [Hide("inventory_screen"), Show("combining_screen")]

    add "images/side/menu_dim.png" xanchor 0 yanchor 0 xpos 822 ypos 21    
    
    $ itemnum = 8 # how many items to display on one page
    $ x = 160 # coordinates of the top left item position
    $ y = 0
    $ i = 0
    $ next_inv_page = inv_page + 1
    if next_inv_page > int(len(inventory.items)/itemnum):
        $ next_inv_page = 0
    for item in inventory.items:
        if i+1 <= (inv_page+1)*itemnum and i+1>inv_page*itemnum:
            $ x += 140
            if i%4==0:
                $ y += 120
                $ x = 160 # same as coordinates of top left item
            $ idlepic = item.image + "_idle.png"
            $ hoverpic = item.image + "_hover.png"
            # $ selpic = item.image + "_selected.png"
            $ my_tooltip = "tooltip_" + item.image.replace("images/inventory/", "")

            imagebutton idle idlepic hover hoverpic xpos x ypos y action [SetVariable("selitem", inventory.items[i].name), SetVariable("sel_xpos", x), SetVariable("sel_ypos", y)] hovered [ Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=0) ] unhovered [Hide("gui_tooltip")]

        $ i += 1
        if len(inventory.items)>itemnum:
            imagebutton auto "next_page_%s.png" focus_mask True action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")]

    if selitem is not None:
        add "images/inventory/selected.png" xpos sel_xpos ypos sel_ypos


screen combining_screen:
    modal True #prevent clicking on other stuff when inventory is shown

    add "gui/nvl.png" xanchor 0 yanchor 0 xpos 23 ypos 20

    hbox xanchor 0 yanchor 0 xpos 822 ypos 21:
        imagebutton auto "images/side/menu_inv_%s.png" focus_mask True action [Hide("combining_screen")]

    hbox xanchor 0 yanchor 0 xpos 22 ypos 100:
        imagebutton idle "images/inventory/button_view.png" focus_mask True action [Hide("combining_screen"), Show("inventory_screen")]

    add "images/side/menu_dim.png" xanchor 0 yanchor 0 xpos 822 ypos 21    
    
    $ itemnum = 8 # how many items to display on one page
    $ x = 160 # coordinates of the top left item position
    $ y = 0
    $ i = 0
    $ next_inv_page = inv_page + 1
    if next_inv_page > int(len(inventory.items)/itemnum):
        $ next_inv_page = 0
    for item in inventory.items:
        if i+1 <= (inv_page+1)*itemnum and i+1>inv_page*itemnum:
            $ x += 140
            if i%4==0:
                $ y += 120
                $ x = 160 # same as coordinates of top left item
            $ pic = item.image + "_idle.png"
            # $ hoverpic = item.image + "_hover.png"
            $ selpic = item.image + "_selected.png"
            $ my_tooltip = "tooltip_" + item.image.replace("inv_", "").replace("images/inventory/","").replace(".png", "")

            imagebutton idle pic xpos x ypos y action [SetVariable("item", item), item.use, combine_items()]

            if item in inventory.selected_items:
                add "images/inventory/combined.png" xpos x ypos y

        $ i += 1
        if len(inventory.items)>itemnum:
            imagebutton auto "next_page_%s.png" focus_mask True action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")]

screen gui_tooltip (my_picture="", my_tt_xpos=gui.dialogue_xpos, my_tt_ypos=200):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

init -1:
    # $ persistent.endings = 0
    # transform inv_eff: # use ATL to make hovered items super bright
    #     zoom 0.5 xanchor 0.5 yanchor 0.5
    #     on idle:
    #         linear 0.2 alpha 1.0
    #     on hover:
    #         linear 0.2 alpha 2.5
    $ width = gui.dialogue_width
    $ height = gui.textbox_height
    $ ypos = 465

    # TOOLTIPS
    image tooltip_ham = LiveComposite((width, height), (0,ypos), Text("It ham."))
    image tooltip_tomato = LiveComposite((width, height), (0,ypos), Text("(It's a {emph}Whole Tomato.{/emph} I bet you $5 I can eat this whole.)"))
    image tooltip_cheese = LiveComposite((width, height), (0,ypos), Text("A packet of sliced cheese."))
    image tooltip_egg = LiveComposite((width, height), (0,ypos), Text("Opening the carton, gives me {emph}6 eggs{/emph}."))
    image tooltip_te = LiveComposite((width, height), (0,ypos), Text("My dinner."))


 