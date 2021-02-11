" generic settings
set relativenumber
set number
set expandtab
set tabstop=4
set shiftwidth=4

" plug-vim 
call plug#begin('~/.vim/plugged')

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'ryanoasis/vim-devicons'
Plug 'jackguo380/vim-lsp-cxx-highlight'
Plug 'townk/vim-autoclose'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'tyrannicaltoucan/vim-deep-space'
Plug 'ap/vim-css-color'

call plug#end()


" colorscheme
set termguicolors 
set termguicolors
colorscheme deep-space
set background=dark

set encoding=UTF-8


" mapping
map <C-n> :NERDTreeToggle<CR>
