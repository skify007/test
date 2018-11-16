## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    ## These control the width and height of the screen.

    config.screen_width = 1280
    config.screen_height = 720

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Babysitter"

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "Babysitter"
    config.version = "0.1.6.b"
    #try: textboxcolorchoice
    #except NameError: textboxcolorchoice = "Blue"

    #########################################
    # Themes

    ## We then want to call a theme function. theme.roundrect is
    ## a theme that features the use of rounded rectangles.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.
    #if textboxcolorchoice == "White":
        #theme.tv(
        ## Theme: TV
        ## Color scheme: Dramatic Flesh

            ## The color of an idle widget face.
            #widget = "#BF7C51",

            ## The color of a focused widget face.
            #widget_hover = "#dda570",

            ## The color of the text in a widget.
            #widget_text = "#E5DFDF",
            ## The color of a disabled widget face.
            #disabled = "#ab6038",
            ## The color of disabled widget text.
            #disabled_text = "#BF7C51",
            ## The color of a frame containing widgets.
            #frame = "#49271b",
            #gm_root = "#2a201f",
            ## The color of the text in a selected widget. (For
            ## example, the current value of a preference.)
            #widget_selected = "#ffffff",


            ## The color of informational labels.
            #label = "#ffffff",

            ## The background of the main menu. This can be a color
            ## beginning with '#', or an image filename. The latter
            ## should take up the full height and width of the screen.
            #mm_root = "gui/main_menu.jpg",

            ## The background of the game menu. This can be a color
            ## beginning with '#', or an image filename. The latter
            ## should take up the full height and width of the screen.

            ## If this is True, the in-game window is rounded. If False,
            ## the in-game window is square.
        #rounded_window = True,

            ## And we're done with the theme. The theme will customize
            ## various styles, so if we want to change them, we should
            ## do so below.
            #)
    #else:
    theme.tv(
        widget = "#5548fc",
        widget_hover = "#35affe",
        widget_text = "#9acbfd",
        disabled = "#293852",
        disabled_text = "#9192aa",
        frame = "#2c0128", #49271b
        gm_root = "#7a7b99",
        widget_selected = "#ffffff",
        label = "#ffffff",
        mm_root = "gui/main_menu.jpg",
        rounded_window = True,
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    style.window.background = Frame("gui/textbox2.png", 0, 0)
    style.say_who_window.background = Frame("gui/namebox2.png", 0, 0)
    #style.window.background = gui.preference('background',Frame("gui/textbox2.png", 0, 0))
    #style.say_who_window.background =  gui.preference('who',Frame("gui/namebox2.png", 0, 0))
        ## Margin is space surrounding the window, where the background
    ## is not drawn.

    #style.window.left_margin =75 #175
    #style.window.right_margin = 225
    style.window.top_margin = 20
    style.window.bottom_margin = 8

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 35 #280
    style.window.right_padding = 35
    style.window.top_padding = 15
    style.window.bottom_padding = 12
    style.window.xmaximum = 1035

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 105 #155
    
    #style.say_who_window.xalign = 0.0
    #style.say_who_window.yalign = 1.0
    style.say_who_window.xpos = -240 #For precise placement
    style.say_who_window.ypos = 172 #For precise placement
    #style.say_who_window.yoffset = 155 #For precise placement
    style.say_who_window.left_padding = 10
    style.say_who_window.top_padding = 9
    style.say_who_window.right_padding = 10
    style.say_who_window.bottom_padding = 10
    style.say_who_window.xminimum = 244
    style.say_who_window.yminimum = 38
    style.say_who_window.xfill = False

    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    #style.mm_menu_frame.xpos = 0.5
    #style.mm_menu_frame.xanchor = 0.5
    #style.mm_menu_frame.ypos = 0.75
    #style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    # style.default.font = "DejaVuSans.ttf"

    ## The default size of text.

    # style.default.size = 22

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.
    style.default.color = "#000"
    style.default.size = 22
    #style.default.outlines = [(2, "#aaa", 2, 2), (2, "#fff", 0, 0)]
    #style.default.hover_color = "#000"
   # style.default.hover_outlines = [(3, "#fff", 1, 1)]
    style.default.antialias  = True


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to True if the game has voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    style.button.activate_sound = "click.wav"
    style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    config.enter_sound = "click.wav"
    config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    # config.main_menu_music = "main_menu_theme.ogg"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.
    config.help = "README.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = None

    ## Used when exiting the game menu to the game.
    config.exit_transition = None

    ## Used between screens of the game menu.
    config.intra_transition = None

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = None

    ## Used when returning to the main menu from the game.
    config.game_main_transition = None

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = None

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = None

    ## Used when a game is loaded.
    config.after_load_transition = None

    ## Used when the window is shown.
    config.window_show_transition = None

    ## Used when the window is hidden.
    config.window_hide_transition = None

    ## Used when showing NVL-mode text directly after ADV-mode text.
    config.adv_nvl_transition = dissolve

    ## Used when showing ADV-mode text directly after NVL-mode text.
    config.nvl_adv_transition = dissolve

    ## Used when yesno is shown.
    config.enter_yesno_transition = None

    ## Used when the yesno is hidden.
    config.exit_yesno_transition = None

    ## Used when entering a replay
    config.enter_replay_transition = None

    ## Used when exiting a replay
    config.exit_replay_transition = None

    ## Used when the image is changed by a say statement with image attributes.
    config.say_attribute_transition = None

    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persistent information can be found by the init code.)
python early:
    config.save_directory = "Babysitter-1481583430"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 0

    ## The default auto-forward time setting.

    config.default_afm_time = 10

    #########################################
    ## More customizations can go here.
    #Code for customizing the in-game menu choices
    
    ##Code for customization of choice BG
    style.menu_choice_button.background = Frame("ButtonIdle_small.png",28,9)
    style.menu_choice_button.hover_background = Frame("ButtonHover_small.png",28,9)
    style.menu = Style(style.hbox)
    style.menu_window.xfill = False
    style.menu_choice_button.xminimum = 60
    style.menu_choice_button.yminimum = 60
    style.menu_choice_button.xpadding = 50
    style.menu_choice_button.ypadding = 25

    
    ##Code for customization of text in the choice button
    style.menu_choice.color = "#fff"
    style.menu_choice.size = 18
    style.menu_choice.outlines = [(2, "#3f603e", 0, 0)]
    style.menu_choice.hover_color = "#fff"
    style.menu_choice.hover_outlines = [(2, "#000", 0, 0)]


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "Babysitter-0.1.6.b"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "Babysitter"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    
    config.main_menu_music = ("MainMenu.mp3")
    config.window_icon = ("images/Icon.png")
    config.windows_icon = ("images/Icon.png")
    
    # Declare two archives.
    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("sounds", "all")

    # Put script files into the scripts archive.
    build.classify("game/**.rpy", "scripts")
    build.classify("game/**.rpyc", "scripts")

    # Put images into the images archive.
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    
    # Put sounds into the images archive.
    build.classify("game/**.mp3", "images")
    build.classify("game/**.avi", "images")
    build.classify("game/**.wav", "images")