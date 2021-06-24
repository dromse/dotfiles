#!/bin/bash

# =========================================================== #
# === This scripts set random wallpaper, change led color === #
# === Author: dromse(dromseproducer@gmail.com)            === #
# =========================================================== #


# set where it gets html
LINK_TO_WEBSITE='https://wallhaven.cc/search?categories=110&purity=100&atleast=3840x2160&ratios=16x9&sorting=random&order=desc&colors=0066cc'

# get html of random wallpapers page
RANDOM_WALLPAPERS_HTML=$(curl $LINK_TO_WEBSITE)

# get a link on page of first image
LINK_TO_FWALLPAPER=$(echo $RANDOM_WALLPAPERS_HTML | grep -oP '"https://wallhaven.cc/w/(.*?)"' | head -1 | tr '"' ' ')

# get html of first image page
FWALLPAPER=$(curl $LINK_TO_FWALLPAPER)

# get link on image
WALLPAPER=$(echo $FWALLPAPER | grep -oP 'src="https://w.wallhaven.cc/full/(.*?)"' | grep -oP '"(.*?)"' | tr '"' ' ')

# set wallpaper
feh --bg-fill $WALLPAPER

# get avarage color of wallpaper
AVARAGE_COLOR=$(magick convert $WALLPAPER -colors 1 -unique-colors txt: | grep -oP '\s#(.*?)\s' | tr '#' ' ')

# set led keyboard
sudo rogauracore single_static $AVARAGE_COLOR
