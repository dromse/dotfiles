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
    Key([mod, "control"], "k", lazy.layout.shuffle_down(), 
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(), 
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(), 
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(), 
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), 
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    # rofi start
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Spawn a rofi run"),
]

group_names = [("WWW", {'layout': 'max'}),                
               ("DEV", {'layout': 'max'}),     
               ("SYS", {'layout': 'max'}),    
               ("DOC", {'layout': 'max'}),       
               ("VBOX", {'layout': 'max'}),         
               ("CHAT", {'layout': 'max'}),         
               ("MUS", {'layout': 'max'}),       
               ("VID", {'layout': 'max'}),       
               ("GFX", {'layout': 'max'})] 


groups = [Group(name, **kwargs) for name, kwargs in group_names] 


for i, (name, kwargs) in enumerate(group_names, 1):     
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group     
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group 


layout_theme = {
    "border_width": 2,
    "margin": 7,
    "border_focus": "#81a1c1",
    "border_normal": "3b4252",
}


layouts = [
    layout.Bsp( **layout_theme ),
    layout.Max( **layout_theme ),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)


extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(),
                #widget.Prompt(),
                widget.Spacer(),
                widget.WindowName(
                        width=bar.CALCULATED,
                    ),
                widget.Spacer(),
                #widget.Chord(
                #    chords_colors={
                #        'launch': ("#242831", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.Systray(),
                # widget.QuickExit(),
            ],
            24,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), 
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), 
        start=lazy.window.get_size()),
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


# autostart
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.call([home])


