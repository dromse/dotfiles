#!/bin/sh

# faster moving on text
xset r rate 440 50
# add new keyboard layout
setxkbmap -layout us,ru,ua
# add hotkey for above command
setxkbmap -option 'grp:alt_shift_toggle'
# change caps and esc button
setxkbmap -option caps:swapescape

picom --experimental-backends &
feh --bg-scale ~/images/wallpaper.jpg &
