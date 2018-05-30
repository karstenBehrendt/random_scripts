set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
"Plugin 'L9'
" Git plugin not hosted on GitHub
"Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
"Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
"Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
"Plugin 'ascenator/L9', {'name': 'newL9'}

Plugin 'davidhalter/jedi-vim'
Plugin 'Valloric/YouCompleteMe'
Plugin 'vim-syntastic/syntastic'
Plugin 'scrooloose/nerdtree'
Plugin 'rafi/awesome-vim-colorschemes'
Plugin 'kien/ctrlp.vim'
Plugin 'FelikZ/ctrlp-py-matcher'
Plugin 'ntpeters/vim-better-whitespace'
Plugin 'luochen1990/rainbow'
let g:rainbow_active=1
Plugin 'octol/vim-cpp-enhanced-highlight'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
let g:ycm_confirm_extra_conf = 0
let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'

"let g:syntastic_python_pylint_args='--ignore=E501,E111'
let g:syntastic_python_python_exec= 'python3'
let g:syntastic_python_flake8_args='--ignore=E501,E111,E114'
let g:syntastic_mode_map = { 'passive_filetypes': ['python'] }

" Jan's weird search thing
let g:ctrlp_match_func = { 'match': 'pymatcher#PyMatch' }

" For mouse click in NERDTree
:set mouse=a
let g:NERDTreeMouseMode=3

syntax on
filetype plugin indent on
set number
set ruler
set hlsearch

nnoremap <F3> :YcmCompleter GoToDefinition<CR>
nnoremap <F4> :YcmCompleter GetDoc<CR>
nnoremap <F5> :YcmCompleter GetType<CR>
nnoremap <F7> :tabprev<CR>
nnoremap <F8> :tabnext<CR>

nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

set tabstop=2
set expandtab
set softtabstop=2
set shiftwidth=2

" config parts
function! SetupPython()
  set tabstop=2
  set expandtab
  set softtabstop=2
  set shiftwidth=2
endfunction

filetype indent on
set ignorecase

:setlocal spell spelllang=en_us   " defines spell check params
set nospell                       " turns off, start with set spell

command! -bar SetupPython call SetupPython()

if v:version >= 704
  " The new Vim regex engine is currently slooooow as hell which makes syntax
  " highlighting slow, which introduces typing latency.
  " Consider removing this in the future when the new regex engine becomes
  " faster.
  set regexpengine=1
endif
set backspace=indent,eol,start " backspace over everything in insert mode

set nomodeline  " vi:, vim:, ex: does not bother anyone anymore
highlight ExtraWhitespace ctermbg=red
