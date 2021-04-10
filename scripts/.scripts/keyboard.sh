#!/bin/bash

# Speed moving through text
xset r rate 500 50 &

# Swap esc and caps
# setxkbmap -option caps:swapescape &

# Change layouts
setxkbmap -layout us,ru,ua -option grp:alt_shift_toggle -option caps:swapescape &
