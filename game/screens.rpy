# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

init -5 python:
    try: Day
    except NameError: Day = None
    if Day == None:
        Day = 1
        Money = 300
        Horny = 0
        MikeHorny = 0
    try: SonyaMet
    except NameError: SonyaMet = "None"
    try: SonFriend
    except NameError: SonFriend = "None"
    try: SonHorny
    except NameError: SonHorny = 0
    try: JesFriend
    except NameError: JesFriend = "None"
    try: JesHorny
    except NameError: JesHorny = 0
    #try: area
    #except NameError: area = None
    #if Day > 0:
        #renpy.show_screen(TheApartment)
    try: textboxcolorchoice
    
    except: textboxcolorchoice = "White"
    

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=True):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox xpos 240:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"
                    #xpos -240
                    #ypos 155

                    text who:
                        size 27
                        outlines [(3, "#666", 2, 2), (2, "#222266", 0, 0)]
                        xalign 0.5
                        italic True
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what":
                    outlines [(3, "#fff3", 1, 1), (0, "#222", 1, 1)]
                    size 23

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    imagebutton auto "gui/HideText_%s.png" focus_mask None action If(renpy.get_screen("say"), HideInterface(), None) xalign 1.0 yalign 1.0
    use quick_menu

##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.98

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
       
    imagemap:
        ground "Idle_MainMenu.png"
        idle "Idle_MainMenu.png"
        hover "Hover_MainMenu.png"
        
        alpha False
        
        hotspot (16, 5, 211, 87) action OpenURL("https://www.patreon.com/T4bbo")
        hotspot (1033, 0, 255, 65) action Start  
        hotspot (1028, 62, 255, 65) action ShowMenu("load")   
        hotspot (1029, 121, 255, 65) action ShowMenu("preferences")   
        hotspot (1032, 181, 255, 65) action OpenURL("https://www.patreon.com/posts/8672058")   
        hotspot (1035, 243, 255, 65) action Quit(confirm=False)
        hotspot (1142, 556, 137, 163) action OpenURL("https://www.patreon.com/cesargames")

    # The main menu buttons.
    # frame:
        # style_group "mm"
        # xalign .98
        # yalign .98

        # has vbox

        # textbutton _("Start Game") action Start()
        # textbutton _("Load Game") action ShowMenu("load")
        # textbutton _("Preferences") action ShowMenu("preferences")
        # textbutton _("Help") action Help()
        # textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the main menu.
    # window:
       # style "mm_root"
       
    imagemap:
        ground 'gui/main_menu.jpg' #Main_Menu.png'
        hover 'gui/main_menu.jpg'
    
        
    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
       #  textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

define gui.slot_button_width = 276
define gui.slot_button_height = 220
# define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = "#09f"

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 160
define config.thumbnail_height = 90
define config.autosave_slots = 12
define config.quicksave_slots = 12

screen file_picker():

    frame:
        style "file_picker_frame"
        xalign 0.5
        yalign 0.01

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            spacing 10
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 13):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()
                
    hbox yalign 0.2:

        $ columns = 3
        $ rows = 4

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            spacing 12
            xpos 8
            ypos 4
            #xfill True
            
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                #fixed:
                button:
                    xpos 10
                    xminimum 405
                    yminimum 105
                    action FileAction(i)

                    #xfill True
                    has hbox

                    # Add the screenshot.
                    imagebutton auto "gui/sv_delete_%s.png" action FileDelete(i) xpos 365 ypos -10
                    add FileScreenshot(i) xpos -35 ypos 5
                    key "save_delete" action FileDelete(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_time!t]\n[save_name!t]" #[file_name].
                    
    


               

init python:
    def name_func(newstring):
        store.save_name = newstring               
               

screen save():


    # This ensures that any other menu screen is replaced.
    tag menu
    use navigation
    use file_picker
    frame:
        #xysize (300,200)
        xpos 125
        ypos 520    
        vbox:

            text "{size=+5}Save name"
            button:
                id "input_1"
                xysize (250,40)
                action NullAction()
                #hover_sound ""
                add Input(hover_color="#3399ff",size=28, color="#000", default="", changed=name_func, length=20, button=renpy.get_widget("text_input_screen","input_1")) yalign 1.0

    text "Save Game":
        xalign 0.02
        yalign 0.99
        yoffset 15
        font "foo_regular.ttf"
        color "#f70"
        outlines [(2, "#222222", 0, 0)]
        size  120
    image "gui/JessMicroBikini1.png":
        xalign 0.777
        yalign 1.0
        yoffset 18

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker
    text "Load Game":
        xalign 0.02
        yalign 0.99
        yoffset 15
        font "foo_regular.ttf"
        color "#fff"
        outlines [(2, "#222222", 0, 0)]
        size  120
    image "gui/JessMicroBikini1.png":
        xalign 0.777
        yalign 1.0
        yoffset 18

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:        
            xpos -180
            ypos -20
            image "quickscreenpic.png"
        # The center column
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")
                
            frame:
                style_group "pref"
                has vbox
                label _("Rollback Side")
                textbutton _("Disable") action Preference("rollback side", "disable")
                textbutton _("Left") action Preference("rollback side", "left")
                textbutton _("Right") action Preference("rollback side", "right")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            #frame:
                #style_group "pref"
                #has vbox

                #textbutton _("Joystick...") action Preference("joystick")


        #vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")
                
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"
            frame:
                style_group "pref"
                has vbox
                label _("Text Box Color")
                text ""
                if textboxcolorchoice == "White":
                    text "{color=#fff}{size=36}White{/size}{/color}"
                else:
                    text "{color=#09f}{size=36}Blue{/size}{/color}"
               # vbox yoffset -25:
                #   textbutton _("Toggle Color") action [ToggleVariable("textboxcolorchoice", "White", "Blue"),gui.TogglePreference('background',Frame("gui/textbox2.png", 0, 0),Frame("gui/textbox3.png", 0, 0))]
                #hbox xalign 1.0:
                    #textbutton _("White") action SetScreenVariable("textboxcolorchoice", "White")
                    #textbutton _("Blue") action SetScreenVariable("textboxcolorchoice", "Blue")

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action
            
        image "quickscreenpic.png" xalign .5 yalign .5

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"
        
##############################################################################
# Yes/No Ending and End of Versions
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen Ending1(message=u'{b}{i}{/i}GAME OVER!{/b} \n\n Christine was not feeling comfortable enough to stay living with you. \n The next day she decided that it would be better to move out. \n\n HINT: Stop acting like a douchebag and try to improve your friendship with Christine.', newest=False):

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Quit") action Quit()

        image "Ending1.png" xalign .5 yalign .5
        
screen Ending2(message=u'{b}{i}{/i}GAME OVER!{/b} \n\n You went bankrupt and you could not afford to pay the rent for the flat. Christine had to leave too. \n HINT: You sould distract somehow Mr. Silver... maybe a girl would help.', newest=False):

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Quit") action Quit()

        image "Ending1.png" xalign .5 yalign .5

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"
        
screen Ending3(message=u'{b}{i}{/i}GAME OVER!{/b} \n\n The Mr. Silver got in trouble and you did not get paid, therefore you went bankrupt and you could not afford to pay the rent for the flat. Christine had to leave too. \n HINT: Watch out on every decision that might somehow gets in you in trouble.', newest=False):

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Quit") action Quit()

        image "Ending1.png" xalign .5 yalign .5

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"
        
screen Ending4(message=u'{b}{i}{/i}GAME OVER!{/b} \n\n Without Sonya there, your meeting with Mr. Silver went poorly, as he was not interested in you and your software. You soon went bankrupt and were evicted. \n Christine, with nowhere to say, went home. Christine had to leave too. \n HINT: Do NOT treat Sonya like a piece of meat.', newest=False):

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Quit") action Quit()

        image "Ending1.png" xalign .5 yalign .5

screen EndOfVersion1:

    imagemap:
        ground "EndOfVersion1.jpg"
        idle "EndOfVersion1.jpg"
        hover "EndOfVersion1_Hover.jpg"
        
        hotspot (890, 198, 322, 186) action OpenURL("https://www.patreon.com/T4bbo")
        hotspot (1059, 406, 151, 170) action OpenURL("https://www.patreon.com/cesargames")

screen PiratedVersion:

    imagemap:
        ground "PiratedVersion.jpg"
        idle "PiratedVersion.jpg"
        hover "PiratedVersion_Hover.jpg"
        
        hotspot (890, 198, 322, 186) action OpenURL("https://www.patreon.com/T4bbo")
        
##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.005
        yalign .99
        imagebutton auto "gui/backbutton_%s.png" focus_mask True action Rollback() xpos 1020 yalign 1.0 yoffset 8
        image "gui/skipbutton_idle.png" xpos 1055 yalign 1.0 yoffset 8
        imagebutton auto "gui/fastskipbutton_%s.png" focus_mask True action Skip() xpos 1090 yalign 1.0 yoffset 8

    image "gui/quickmenubg.png" xpos 0.0025 xalign 0.0 yalign 1.0
    hbox:
        style_group "quick"

        xalign 0.0025
        yalign .995
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        #textbutton _("Menu") action MainMenu()
        textbutton _("Prefs") action ShowMenu('preferences')
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Save") action ShowMenu('save')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 11
        bold True
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
        
init python:
    style.input.color = "#ffffff"


##############################################################################
# Own In game ImageMaps
#

screen Bathroom:
    tag navscreen
    
    imagemap:
        ground "backgrounds/Bathroom2.jpg"
        idle "backgrounds/Bathroom2.jpg"
        hover "backgrounds/Bathroom2Hover.jpg"
        
        hotspot (1106, 473, 141, 213) clicked Jump ("Toilet")   
        hotspot (152, 2, 132, 714) clicked Jump ("Shower")
        hotspot (31, 270, 130, 358) clicked Jump ("Towel")
        #hotspot (297, 1, 556, 35) clicked Jump ("TurnBathroom")
    imagebutton auto "backgrounds/RoomButtons/BackEntryHall_%s.png" focus_mask True action Jump ("HallEntry") xalign 0.48 yalign 0.01
        
screen Bedroom:
    
    imagemap:
        ground "backgrounds/Bedroom.jpg"
        idle "backgrounds/Bedroom.jpg"
        hover "backgrounds/BedroomHover.jpg"
        
        hotspot (1013, 18, 266, 642) clicked Jump ("BedroomOut")   
        hotspot (69, 378, 279, 168) clicked Jump ("Computer")
    imagebutton auto "backgrounds/RoomButtons/RightClosetBed_%s.png" focus_mask True action Jump ("BedroomIn") xalign 0.75 yalign 0.03
        
        
screen BedroomIn:
    tag navscreen
    
    add  "backgrounds/Bedroom_Closet1a.jpg" 
    imagemap:
        ground "backgrounds/Bedroom_Closet1a.jpg" 
        idle "backgrounds/Bedroom_Closet1a.jpg" 
        hover "backgrounds/Bedroom_Closet1b.jpg" 
        
        hotspot (732, 336, 547, 383) clicked Jump ("Bed")  
        hotspot (0, 9, 544, 608) clicked Jump ("Wardrobe")
        #hotspot (380, 0, 484, 37) clicked Jump ("TurnBedroomIn")
        #hotspot (1170, 0, 108, 188) clicked Jump ("BedroomInCorner")
    #imagebutton auto "backgrounds/RoomButtons/Bed_%s.png" focus_mask True action Jump ("Bed")
    #imagebutton auto "backgrounds/RoomButtons/Closet2_%s.png" focus_mask True action Jump ("Wardrobe")
    imagebutton auto "backgrounds/RoomButtons/LeftLivingRoom_%s.png" focus_mask True action Jump ("TurnBedroomIn") xalign 0.45 yalign 0.0
    imagebutton auto "backgrounds/RoomButtons/BedroomDesk_%s.png" focus_mask True action Jump ("BedroomInCorner") xalign 0.55 yalign 0.0
        
screen BedroomOut:
    
    imagemap:
        ground "backgrounds/BedroomOut2.jpg"
        idle "backgrounds/BedroomOut2.jpg"
        hover "backgrounds/BedroomOut2Hover.jpg"
        
        hotspot (959, 99, 193, 620) clicked Jump ("FreeRoom")   
        #hotspot (4, 59, 497, 539) clicked Jump ("Kitchen") #2y 539
        hotspot (578, 91, 270, 515) clicked Jump ("HallOut") 
        #hotspot (376, 0, 496, 37) clicked Jump ("TurnBedroomOut")
        #hotspot (4, 490, 332, 670) clicked Jump ("LivingRoom")
    imagebutton auto "backgrounds/RoomButtons/Bedroom_%s.png" focus_mask True action Jump ("TurnBedroomOut") xalign 0.48 yalign 0.01
    imagebutton auto "backgrounds/RoomButtons/LivingRoomCouch_%s.png" focus_mask True action Jump ("LivingRoom")
    imagebutton auto "backgrounds/RoomButtons/LivingRoomKitchen_%s.png" focus_mask True action Jump ("Kitchen")
    
    #imagebutton auto "Menu_%s.png" focus_mask True action ShowMenu("save")
        
screen FreeRoom: 
    
    imagemap:
        ground "backgrounds/FreeRoom2.jpg"
        idle "backgrounds/FreeRoom2.jpg"
        hover "backgrounds/FreeRoom2.jpg"
        
        #hotspot (413, 2, 463, 36) clicked Jump ("TurnFreeRoom")
    imagebutton auto "backgrounds/RoomButtons/BackLivingRoom_%s.png" focus_mask True action Jump ("LivingRoom") xalign 0.55 yalign 0.01

screen ChristineRoom:
    
    tag navscreen
    imagemap:
        ground "backgrounds/ChristineRoom2.jpg"
        idle "backgrounds/ChristineRoom2.jpg"
        hover "backgrounds/ChristineRoom2Hover.jpg"
        
        hotspot (0, 377, 110, 114) clicked Jump ("DogPicture")
        hotspot (75, 26, 140, 268) clicked Jump ("Poster1")
        hotspot (463, 67, 164, 238) clicked Jump ("Poster2")
        hotspot (163, 347, 296, 153) clicked Jump ("Pillows")
        hotspot (464, 421, 150, 211) clicked Jump ("BedsideTable")
        hotspot (664, 343, 145, 109) clicked Jump ("ComputerChristineRoom")
        hotspot (1058, 383, 79, 92) clicked Jump ("MedicBooks")
        hotspot (959, 477, 195, 218) clicked Jump ("TableDrawers")
        #hotspot (425, 0, 516, 38) clicked Jump ("TurnChristineRoom")
    imagebutton auto "backgrounds/RoomButtons/BackLivingRoom_%s.png" focus_mask True action Jump ("LivingRoom") xalign 0.55 yalign 0.01
        
screen HallEntry:

    tag navscreen
    
    imagemap:
        ground "backgrounds/HallEntry.jpg"
        idle "backgrounds/HallEntry.jpg"
        hover "backgrounds/HallEntryHover.jpg"
        
        hotspot (220, 0, 196, 518) clicked Jump ("LivingRoom")   
        hotspot (525, 41, 169, 564) clicked Jump ("Kitchen")
        hotspot (1056, 89, 204, 627) clicked Jump ("Bathroom")
    imagebutton auto "backgrounds/RoomButtons/EntryDoor_%s.png" focus_mask True action Jump ("HallOut") xalign 0.48 yalign 0.01
        
screen HallOut:
    
    tag navscreen
    imagemap:
        ground "backgrounds/HallOut2.jpg"
        idle "backgrounds/HallOut2.jpg"
        hover "backgrounds/HallOut2Hover.jpg"
        
        hotspot (1050, 158, 210, 435) clicked Jump ("Outside")
        hotspot (115, 64, 266, 654) clicked Jump ("Bathroom")
        #hotspot (421, 0, 441, 44) clicked Jump ("TurnHallOut")
    imagebutton auto "backgrounds/RoomButtons/RightLivingRoom_%s.png" focus_mask True action Jump ("LivingRoom") xalign 0.56 yalign 0.0
    imagebutton auto "backgrounds/RoomButtons/LeftKitchen_%s.png" focus_mask True action Jump ("Kitchen") xalign 0.425 yalign 0.0
        
screen Kitchen:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Kitchen2.jpg"
        idle "backgrounds/Kitchen2.jpg"
        hover "backgrounds/Kitchen2Hover.jpg"
        
        hotspot (0, 241, 92, 439) clicked Jump ("Fridge")
        hotspot (539, 57, 208, 491) clicked Jump ("Cook")
        #hotspot (419, 0, 432, 40) clicked Jump ("TurnKitchen")
    imagebutton auto "backgrounds/RoomButtons/LeftLivingRoom_%s.png" focus_mask True action Jump ("LivingRoom") xalign 0.45 yalign 0.0
    imagebutton auto "backgrounds/RoomButtons/RightEntryHall_%s.png" focus_mask True action Jump ("HallOut") xalign 0.55 yalign 0.0
        
screen LivingRoom:

    tag navscreen
    
    imagemap:
        ground "backgrounds/LivingRoom2.jpg"
        idle "backgrounds/LivingRoom2.jpg"
        hover "backgrounds/LivingRoom2Hover.jpg"
        
        hotspot (264, 218, 316, 232) clicked Jump ("Television")
        hotspot (688, 2, 589, 658) clicked Jump ("Balcony")
        hotspot (0, 169, 228, 407) clicked Jump ("BedroomIn")
        #hotspot (442, 0, 245, 70) clicked Jump ("TurnLivingRoom")
    imagebutton auto "backgrounds/RoomButtons/LeftGuestRoom_%s.png" focus_mask True action Jump ("FreeRoom") xalign 0.385 yalign 0.0
    imagebutton auto "backgrounds/RoomButtons/LeftEntryHall_%s.png" focus_mask True action Jump ("HallOut") xalign 0.275 yalign 0.0
    imagebutton auto "backgrounds/RoomButtons/RightKitchen_%s.png" focus_mask True action Jump ("Kitchen") xalign 0.51 yalign 0.0
        
screen Balcony:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Balcony2.jpg"
        idle "backgrounds/Balcony2.jpg"
        hover "backgrounds/Balcony2Hover.jpg"
        
        hotspot (0, 212, 751, 505) clicked Jump ("HotTub")
        #hotspot (538, 1, 315, 42) clicked Jump ("TurnHallOut")
    imagebutton auto "backgrounds/RoomButtons/InLivingRoom_%s.png" focus_mask True action Jump ("LivingRoom") xalign 0.55 yalign 0.01

screen JessSite:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Bedroom_Computer_JessicaBlog.jpg"
        idle "backgrounds/Bedroom_Computer_JessicaBlog.jpg"
        hover "backgrounds/Bedroom_Computer_JessicaBlog_Hover.jpg"
        
        hotspot (239, 488, 123, 70) clicked Jump ("JessPhotos")
        hotspot (238, 560, 127, 75) clicked Jump ("JessVideos")
        hotspot (452, 410, 87, 66) action OpenURL("https://www.patreon.com/T4bbo/posts?tag=Jess%27s%20site") 
        hotspot (239, 84, 57, 56) clicked Jump ("JessQuit")
        hotspot (805, 413, 251, 59) clicked Jump ("ProcessingPatreonship")
        hotspot (350, 409, 95, 68) clicked Jump ("JessBlog")

screen MassageDecision:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Day13_ChrJesMassage_01a.jpg"
        idle "backgrounds/Day13_ChrJesMassage_01a.jpg"
        hover "backgrounds/Day13_ChrJesMassage_01a_Hover.jpg"
        
        hotspot (283, 1, 775, 182) clicked Jump ("ChrMassageChoice")
        hotspot (8, 361, 1267, 358) clicked Jump ("JesMassageChoice")
        hotspot (1079, 0, 163, 207) clicked Jump ("OilGet") 
        
screen MassageDecision2:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Day13_ChrJesMassage_01b.jpg"
        idle "backgrounds/Day13_ChrJesMassage_01b.jpg"
        hover "backgrounds/Day13_ChrJesMassage_01b_Hover.jpg"
        
        hotspot (283, 1, 775, 182) clicked Jump ("ChrMassageChoice")
        hotspot (8, 361, 1267, 358) clicked Jump ("JesMassageChoice")


screen JessMassage:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Day13_ChrJesMassage_23.jpg"
        idle "backgrounds/Day13_ChrJesMassage_23.jpg"
        hover "backgrounds/Day13_ChrJesMassage_23_Hover.jpg"
        
        hotspot (136, 191, 163, 261) clicked Jump ("JesShoulder")
        hotspot (313, 214, 205, 158) clicked Jump ("JesBack")
        hotspot (331, 373, 98, 51) clicked Jump ("JesBreasts")
        hotspot (530, 195, 150, 246) clicked Jump ("JesAss")
        hotspot (689, 216, 188, 220) clicked Jump ("JesThighs")
        hotspot (877, 244, 243, 193) clicked Jump ("JesLowerLegs")
        hotspot (1136, 259, 130, 177) clicked Jump ("JesFoot")
        
screen JessMassageOil:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Day13_ChrJesMassage_24.jpg"
        idle "backgrounds/Day13_ChrJesMassage_24.jpg"
        hover "backgrounds/Day13_ChrJesMassage_24_Hover.jpg"
        
        hotspot (136, 191, 163, 261) clicked Jump ("JesShoulder")
        hotspot (313, 214, 205, 158) clicked Jump ("JesBack")
        hotspot (331, 373, 98, 51) clicked Jump ("JesBreasts")
        hotspot (530, 195, 150, 246) clicked Jump ("JesAss")
        hotspot (689, 216, 188, 220) clicked Jump ("JesThighs")
        hotspot (877, 244, 243, 193) clicked Jump ("JesLowerLegs")
        hotspot (1136, 259, 130, 177) clicked Jump ("JesFoot")


screen ChrMassage:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Day13_ChrJesMassage_44a.jpg"
        idle "backgrounds/Day13_ChrJesMassage_44a.jpg"
        hover "backgrounds/Day13_ChrJesMassage_44a_Hover.jpg"
        
        hotspot (198, 234, 162, 225) clicked Jump ("ChrShoulder")
        hotspot (367, 251, 172, 147) clicked Jump ("ChrBack")
        hotspot (374, 390, 85, 49) clicked Jump ("ChrBreasts")
        hotspot (559, 226, 160, 220) clicked Jump ("ChrAss")
        hotspot (721, 256, 162, 191) clicked Jump ("ChrThighs")
        hotspot (896, 277, 226, 147) clicked Jump ("ChrLowerLegs")
        hotspot (1134, 272, 132, 150) clicked Jump ("ChrFoot")
        
screen ChrMassageOil:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Day13_ChrJesMassage_44b.jpg"
        idle "backgrounds/Day13_ChrJesMassage_44b.jpg"
        hover "backgrounds/Day13_ChrJesMassage_44b_Hover.jpg"
        
        hotspot (198, 234, 162, 225) clicked Jump ("ChrShoulder")
        hotspot (367, 251, 172, 147) clicked Jump ("ChrBack")
        hotspot (374, 390, 85, 49) clicked Jump ("ChrBreasts")
        hotspot (559, 226, 160, 220) clicked Jump ("ChrAss")
        hotspot (721, 256, 162, 191) clicked Jump ("ChrThighs")
        hotspot (896, 277, 226, 147) clicked Jump ("ChrLowerLegs")
        hotspot (1134, 272, 132, 150) clicked Jump ("ChrFoot")

screen ChrFuck:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Day13_Bedroom_15c.jpg"
        idle "backgrounds/Day13_Bedroom_15c.jpg"
        hover "backgrounds/Day13_Bedroom_15c_Hover.jpg"
        
        hotspot (515, 87, 155, 100) clicked Jump ("Day13Kiss")
        hotspot (523, 193, 157, 68) clicked Jump ("Day13Neck")
        hotspot (493, 277, 232, 140) clicked Jump ("Day13Tits")
        hotspot (488, 421, 235, 120) clicked Jump ("Day13Stomach")
        hotspot (656, 607, 221, 105) clicked Jump ("Day13Legs")
        hotspot (438, 594, 99, 102) clicked Jump ("Day13BigToe")
        hotspot (544, 580, 151, 133) clicked Jump ("Day13Panties")
        
screen ChrFuckHorny:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Day13_Bedroom_16c.jpg"
        idle "backgrounds/Day13_Bedroom_16c.jpg"
        hover "backgrounds/Day13_Bedroom_16c_Hover.jpg"
        
        hotspot (515, 87, 155, 100) clicked Jump ("Day13Kiss")
        hotspot (523, 193, 157, 68) clicked Jump ("Day13Neck")
        hotspot (493, 277, 232, 140) clicked Jump ("Day13Tits")
        hotspot (488, 421, 235, 120) clicked Jump ("Day13Stomach")
        hotspot (656, 607, 221, 105) clicked Jump ("Day13Legs")
        hotspot (292, 580, 161, 127) clicked Jump ("Day13BigToe")
        hotspot (544, 580, 151, 133) clicked Jump ("Day13Panties")


screen JessFuckFrontNotHorny:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Day14_Jess_13a.jpg"
        idle "backgrounds/Day14_Jess_13a.jpg"
        hover "backgrounds/Day14_Jess_13c.jpg"
        
        hotspot (495, 122, 171, 83) clicked Jump ("JessYachtKissScene")
        hotspot (479, 249, 237, 94) clicked Jump ("JessYachtTitsScene")
        hotspot (526, 427, 161, 134) clicked Jump ("JessYachtPussyFaceUp")
        hotspot (727, 549, 167, 130) clicked Jump ("JessYachtFootScene")
        hotspot (248, 526, 144, 145) clicked Jump ("JessicaSexMenuFaceDown")

screen JessFuckFrontHorny:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Day14_Jess_14a.jpg"
        idle "backgrounds/Day14_Jess_14a.jpg"
        hover "backgrounds/Day14_Jess_14c.jpg"
        
        hotspot (495, 122, 171, 83) clicked Jump ("JessYachtKissScene")
        hotspot (479, 249, 237, 94) clicked Jump ("JessYachtTitsScene")
        hotspot (526, 427, 161, 134) clicked Jump ("JessYachtPussyFaceUp")
        hotspot (727, 549, 167, 130) clicked Jump ("JessYachtFootScene")
        hotspot (248, 526, 144, 145) clicked Jump ("JessicaSexMenuFaceDown")


screen JessFuckBackNotHorny:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Day14_Jess_15a.jpg"
        idle "backgrounds/Day14_Jess_15a.jpg"
        hover "backgrounds/Day14_Jess_15c.jpg"
        
        hotspot (610, 376, 163, 118) clicked Jump ("JessYachtSpankScene")
        hotspot (453, 609, 249, 101) clicked Jump ("JessicaYachtPussyFaceDown")
        hotspot (369, 373, 152, 145) clicked Jump ("JessicaYachtAssPlay")
        hotspot (508, 176, 129, 113) clicked Jump ("JessicaSexMenuFaceUp")


screen JessFuckBackHorny:

    tag navscreen
    
    imagemap:
        ground "backgrounds/Day14_Jess_16a.jpg"
        idle "backgrounds/Day14_Jess_16a.jpg"
        hover "backgrounds/Day14_Jess_16c.jpg"
        
        hotspot (610, 376, 163, 118) clicked Jump ("JessYachtSpankScene")
        hotspot (453, 609, 249, 101) clicked Jump ("JessicaYachtPussyFaceDown")
        hotspot (369, 373, 152, 145) clicked Jump ("JessicaYachtAssPlay")
        hotspot (508, 176, 129, 113) clicked Jump ("JessicaSexMenuFaceUp")

#init python:
#    def stat_box(**kwargs):
#        curried_toggle = renpy.curry(toggle_stats)
#        if show_stats:
#            ui.frame()
#            ui.vbox()
#            ui.image("Ksicht.png")
            #ui.text("Friend: %d" % Friend)
#            ui.image("Smile.png"), ui.text(": %d" % Friend)
            #ui.text("Horny: %d" % Horny)
#            ui.image("Heart.png"), ui.text(": %d" % Horny)
#            ui.textbutton("Hide Stats", clicked=curried_toggle(False))
#            ui.close()
#        else:
#            ui.frame()
#            ui.textbutton("Christine", clicked=curried_toggle(True))
#    renpy.define_screen("stat_box", stat_box)

#    def toggle_stats(x):
#        global show_stats 
#        show_stats = x
#        renpy.restart_interaction()
        

screen control():
        imagebutton auto "gui/gamestats_%s.png" xpos 0 ypos 0 action If(renpy.get_screen("stat_box"), Hide("stat_box"), Show("stat_box"))
        
screen cheats():
    if JesFriend == "None":
        $ JesFriend = 0
    if SonFriend == "None":
        $ SonFriend = 0
    imagemap:
        ground "gui/cheats.png"
        hotspot(338, 316, 23, 25) action SetVariable("Friend", Friend-1)
        hotspot(366, 316, 26, 28) action SetVariable("Friend", Friend+1)
        hotspot(396, 316, 28, 25) action SetVariable("Horny", Horny-1)
        hotspot(428, 313, 25, 28) action SetVariable("Horny", Horny+1)
        hotspot(556, 316, 28, 25) action SetVariable("JesFriend", JesFriend-1)
        hotspot(588, 320, 25, 17) action SetVariable("JesFriend", JesFriend+1)
        hotspot(624, 314, 20, 26) action SetVariable("JesHorny", JesHorny-1)
        hotspot(648, 314, 32, 26) action SetVariable("JesHorny", JesHorny+1)
        hotspot(780, 314, 24, 26) action SetVariable("SonFriend", SonFriend-1)
        hotspot(810, 316, 23, 22) action SetVariable("SonFriend", SonFriend+1)
        hotspot(837, 316, 28, 24) action SetVariable("SonHorny", SonHorny-1)
        hotspot(868, 316, 29, 26) action SetVariable("SonHorny", SonHorny+1)
        hotspot(590, 492, 30, 33) action SetVariable("MikeHorny", MikeHorny-1)
        hotspot(622, 500, 24, 24) action SetVariable("MikeHorny", MikeHorny+1)
    text "[player_name]'s horny points" xpos 620 ypos 400 font "foo_regular.ttf" color "#fff" outlines [(3, "#222222", 0, 0)] xalign 0.55
    text "[MikeHorny]"xpos 618 ypos 450 font "foo_regular.ttf" color "#fff" outlines [(3, "#222222", 0, 0)] xalign 0.55
    
    text "[JesHorny]" xpos 646 ypos 273 font "foo_regular.ttf" color "#fff" outlines [(3, "#222222", 0, 0)] xalign 0.55
    text "[JesFriend]" xpos 588 ypos 273 font "foo_regular.ttf" color "#fff" outlines [(3, "#222222", 0, 0)] xalign 0.55
    
    text "[SonHorny]" xpos 867 ypos 276 font "foo_regular.ttf" color "#fff" outlines [(3, "#222222", 0, 0)] xalign 0.55
    text "[SonFriend]" xpos 808 ypos 276 font "foo_regular.ttf" color "#fff" outlines [(3, "#222222", 0, 0)] xalign 0.55

    text "[Horny]" xpos 424 ypos 273 font "foo_regular.ttf" color "#fff" outlines [(3, "#222222", 0, 0)] xalign 0.55
    text "[Friend]" xpos 368 ypos 273 font "foo_regular.ttf" color "#fff" outlines [(3, "#222222", 0, 0)] xalign 0.55
     
screen stat_box():
    imagebutton:
        idle "gui/calendarbg.png"
        hover "gui/calendarbg_hover.png"
        focus_mask True
        xalign 1.0 yalign 0.0
        action If(renpy.get_screen("cheats"), Hide("cheats"), Show("cheats"))
        
    vbox xpos 0.955 ypos 0.043:
        text "[Day]":
            xalign 0.55
            size 40
            outlines [(3, "#222222", 0, 0)]
            font "foo_regular.ttf"
            color "#fff"
            
    vbox xalign 0.925 yalign 0.014:
        text _("{color=#54a992}$ {/color}" + str(Money)):
            xalign 1.0
            size 40
            outlines [(3, "#222222", 0, 0)]
            font "foo_regular.ttf"
            color "#fff"
            
    vbox xpos 0.885 ypos 0.067:
        image "Heart.png"
        text "[MikeHorny]":
            yoffset -45
            xalign 0.55
            font "foo_regular.ttf"
            color "#fff"
            outlines [(2, "#222222", 0, 0)]
            size  25

#This is your stat_box Screen
#screen stat_box():
    if not renpy.get_screen("cheats"):
        fixed:
            xpos 0
            ypos 0.045
            image "gui/Christine2.png"
        hbox xpos 0.009 ypos 0.213:
            text "[Friend]":
                xalign 0.45
                font "foo_regular.ttf"  
                color "#fff"
                outlines [(2, "#222222", 0, 0)]
                size  25
        hbox xpos 0.054 ypos 0.213:
            text "[Horny]":
                xalign 0.45
                font "foo_regular.ttf"
                color "#fff"
                outlines [(2, "#222222", 0, 0)]
                size  25
        if SonFriend != "None":
            fixed:
                xpos 0
                ypos 0.542
                image "gui/Sonya2.png"
            
            hbox xpos 0.009 ypos 0.709:
                text "[SonFriend]":
                    xalign 0.5
                    font "foo_regular.ttf"
                    color "#fff"
                    outlines [(2, "#222222", 0, 0)]
                    size  25

            hbox xpos 0.055 ypos 0.709:
                #image "Heart.png"   
                text "[SonHorny]":
                    xalign 0.5
                    font "foo_regular.ttf"
                    color "#fff"
                    outlines [(2, "#222222", 0, 0)]
                    size  25
        if JesFriend != "None":
            fixed:
                xpos 0
                ypos 0.294
                image "gui/Jessica2.png"
            
            hbox xpos 0.009 ypos 0.458:
                text "[JesFriend]":
                    xalign 0.5
                    font "foo_regular.ttf"
                    color "#fff"
                    outlines [(2, "#222222", 0, 0)]
                    size  25
            hbox xpos 0.055 ypos 0.458:
                text "[JesHorny]":
                    xalign 0.5
                    font "foo_regular.ttf"
                    color "#fff"
                    outlines [(2, "#222222", 0, 0)]
                    size  25
                
### end of line ###