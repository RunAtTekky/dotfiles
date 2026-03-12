[[ -o interactive ]] || return

autoload -Uz compinit
compinit -C

[[ -o login ]] && figlet -f slant -c -w $(tput cols) "RunAt" | lolcat

# oh-my-zsh
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
zstyle ':omz:update' mode disabled
source $ZSH/oh-my-zsh.sh

# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='nvim'
fi

# vi mode
bindkey -v

# Yank to clipboard
function vi-yank-xclip {
  zle vi-yank
  echo "$CUTBUFFER" | pbcopy
}
zle -N vi-yank-xclip
bindkey -M vicmd 'y' vi-yank-xclip

# ALIASES
alias v="nvim"
alias zs="zellij --layout ~/.config/zellij/my-dev-setup.kdl"
alias zc="zellij --layout compact"

# Accepting auto-suggestion using shift + tab
bindkey '^[[Z' autosuggest-accept

# FZF file opener
bindkey -s '^f' 'file=$(fzf) && [ -n "$file" ] && nvim "$file"\n'

# zoxide
eval "$(zoxide init zsh)"

# PATHS
export PATH="$PATH:$HOME/go/bin"
export PATH="$PATH:$HOME/bin"
export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"
export PATH="/opt/homebrew/opt/postgresql@18/bin:$PATH"

export LDFLAGS="-L/opt/homebrew/opt/postgresql@18/lib"
export CPPFLAGS="-I/opt/homebrew/opt/postgresql@18/include"

# NVM (Node Version Manager Lazy loaded)
export NVM_DIR="$HOME/.nvm"

load-nvm() {
  unset -f node yarn npm npx
  [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
  [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
}

node() { load-nvm; node "$@"; }
yarn() { load-nvm; yarn "$@"; }
npm() { load-nvm; npm "$@"; }
npx() { load-nvm; npx "$@"; }

# SDKMAN
export SDKMAN_DIR="$HOME/.sdkman"

sdk() {
  unset -f sdk
  source "$SDKMAN_DIR/bin/sdkman-init.sh"
  sdk "$@"
}
