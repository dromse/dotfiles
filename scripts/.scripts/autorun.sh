#!/bin/bash

killall polybar
polybar example &
pgrep -x picom     > /dev/null || picom &
#pgrep -x udiskie   > /dev/null || udiskie --no-automount --no-notify --tray &
pgrep -x xbindkeys > /dev/null || xbindkeys -p &
# pgrep -x paperview > /dev/null || paperview /usr/share/wallpaper/night 5 &
pgrep -x feh       > /dev/null || feh --bg-scale ~/.scripts/wall.jpg &

# speed of cursor moving
xset r rate 500 50 &

# switch layout and swap caps and esc
setxkbmap -layout us,ru,ua -option grp:alt_shift_toggle -option caps:swapescape &
