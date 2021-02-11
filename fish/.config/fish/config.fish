# Fish settings
set fish_greeting

# Package manager aliases
alias install "sudo pacman -S"
alias update "sudo pacman -Syu"
alias remove "sudo pacman -R"

alias aur "yay -S"

# System aliases
alias cpumax "sudo cpupower frequency-set --max"
alias cpumin "sudo cpupower frequency-set --min"
alias cpuinfo "cpupower frequency-info"

# Text editor aliases
alias v "nvim"
alias suv "sudo nvim"

# Change config files aliases
alias config_alacritty "nvim ~/.config/alacritty/alacritty.yml"
alias config_fish "nvim ~/.config/fish/config.fish"
alias config_polybar "nvim ~/.config/polybar/config"
alias config_awesome "nvim ~/.config/awesome/rc.lua"
alias config_qtile "nvim ~/.config/qtile/config.py"
alias config_nvim "nvim ~/.config/nvim/init.vim"
alias config_i3 "nvim ~/.config/i3/config"
alias config_ranger "cd ~/.config/ranger/"
alias configs "cd ~/.config"
alias config_picom "nvim ~/.config/picom/picom.conf"
alias update_dotfiles "cd ~/dotfiles && git add . && git commit -m"

# Short aliases for freqently uses commands
alias c "clear"
alias k "cd .."
alias j "cd"
alias r "ranger"


