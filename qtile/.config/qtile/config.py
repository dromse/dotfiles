from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess


mod = "mod4"
terminal = guess_terminal()


keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(), desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(), desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(), desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(), desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(), 
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(), desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    # Start rofi run
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Spawn a rofi run"),

    # Volume control
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%"),),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%"),),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),),

    # Screenshot
    Key([], "Print", lazy.spawn("spectacle"),),
]


group_names = [("WWW", {'layout': 'bsp'}),                
               ("DEV", {'layout': 'bsp'}),     
               ("SYS", {'layout': 'bsp'}),    
               ("DOC", {'layout': 'bsp'}),       
               ("VBOX", {'layout': 'bsp'}),         
               ("CHAT", {'layout': 'bsp'}),         
               ("MUS", {'layout': 'bsp'}),       
               ("VID", {'layout': 'bsp'}),       
               ("GFX", {'layout': 'bsp'})] 


groups = [Group(name, **kwargs) for name, kwargs in group_names] 


for i, (name, kwargs) in enumerate(group_names, 1):     
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group     
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group 


layout_theme = {
    "border_width": 2,
    "margin": 10,
    "single_margin": 10,
    "border_focus": "#81a1c1",
    "border_normal": "3b4252",
}


layouts = [
    layout.Bsp( **layout_theme ),
    layout.Max( **layout_theme ),
    ]


# Nord Color Theme
colors = [["#2e3440", "#2e3440"], #nord0
          ["#3b4252", "#3b4252"], #nord1
          ["#434c5e", "#434c5e"], #nord2
          ["#4c566a", "#4c566a"], #nord3
          ["#d8dee9", "#d8dee9"], #nord4
          ["#e5e9f0", "#e5e9f0"], #nord5
          ["#eceff4", "#eceff4"], #nord6
          ["#8fbcbb", "#8fbcbb"], #nord7
          ["#88c0d0", "#88c0d0"], #nord8
          ["#81a1c1", "#81a1c1"], #nord9
          ["#5e81ac", "#5e81ac"], #nord10
          ["#bf616a", "#bf616a"], #nord11
          ["#d08770", "#d08770"], #nord12
          ["#ebcb8b", "#ebcb8b"], #nord13
          ["#a3be8c", "#a3be8c"], #nord14
          ["#b48ead", "#b48ead"]] #nord15


widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize=12,
    padding=3,
    background=colors[0],
)


extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        bottom=bar.Bar(
            [
                # Workspaces widget
                widget.GroupBox(
                    # fontsize = 9, 
                    margin_y = 3, 
                    margin_x = 0,  
                    padding_y = 5,   
                    padding_x = 3, 
                    borderwidth = 3,     
                    active = colors[6],  
                    inactive = colors[6],  
                    rounded = False, 
                    highlight_color = colors[3],  
                    highlight_method = "line",   
                    this_current_screen_border = colors[3], 
                    this_screen_border = colors [0],  
                    other_current_screen_border = colors[0],  
                    other_screen_border = colors[0],        
                    foreground = colors[6], 
                    background = colors[0]
                ),
                
                # Just spacer
                widget.Spacer(
                ),

                # Volume widget
                widget.TextBox(
                    text='\uE0B2',
                    background = colors[0],
                    foreground = colors[7],
                    padding=0,
                    fontsize=37
                ),
                
                widget.Volume(
                    background=colors[7],  
                    foreground=colors[0],
                ),

                # CPU widget
                widget.TextBox(
                    text='\uE0B2',
                    background = colors[7],
                    foreground = colors[10],
                    padding=0,
                    fontsize=37
                ),

                widget.CPU(
                    format='CPU: {freq_current}GHz {load_percent}%  ',
                    background=colors[10],
                    foreground=colors[0],
                ),
                
                # RAM widget
                widget.TextBox(
                    text='\uE0B2',
                    background = colors[10],
                    foreground = colors[8],
                    padding=0,
                    fontsize=37
                ),

                widget.Memory(
                    background=colors[8],  
                    foreground=colors[0],
                ),
                
                # Internet widget
                widget.TextBox(
                    text='\uE0B2',
                    background = colors[8],
                    foreground = colors[9],
                    padding=0,
                    fontsize=37
                ),

                widget.Net(
                    interface="wlo1",
                    background=colors[9],
                    foreground=colors[0],
                    format='{down} ↓↑{up} ',
                ), 
                
                # Clock widget
                widget.TextBox(
                    text='\uE0B2',
                    background = colors[9],
                    foreground = colors[7],
                    padding=0,
                    fontsize=37
                ),

                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p ',
                    background=colors[7],
                    foreground=colors[0],
                ),
               
                # Systray widget
                widget.TextBox(
                    text='\uE0B2',
                    background = colors[7],
                    foreground = colors[0],
                    padding=0,
                    fontsize=37
                ),

                widget.Systray(
                    background=colors[0],
                    foreground=colors[0],
                ),

                widget.TextBox(
                    text=' \uE0B2',
                    background = colors[0],
                    foreground = colors[10],
                    padding=0,
                    fontsize=37
                ),
            ], 25 # Bar size
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False


floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])


auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "qtile"


# autostart [picom, feh and etc.]
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.call([home])


