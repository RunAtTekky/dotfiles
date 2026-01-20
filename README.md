# My dotfiles for MacOS
On my [main](https://github.com/RunAtTekky/dotfiles) setup I use [Omarchy](https://omarchy.org/)

Earlier I used [Linux Mint](https://github.com/RunAtTekky/dotfiles/tree/mint)

[Here](https://github.com/RunAtTekky/dotfiles/tree/macos) on my MacOS setup I want similar keyboard driven workflow.

# Programs I Use and which are currently managed in this branch
|Tool|Program Name|
|---|---|
|Shell | [ZSH](https://wiki.archlinux.org/title/Zsh)|
|Terminal Emulator | [Kitty](https://github.com/kovidgoyal/kitty)|
|Terminal Multiplexer | [Zellij](https://zellij.dev/)|
|Window Manager | [AeroSpace](https://github.com/nikitabobko/AeroSpace)|
|Video Player | [MPV](https://mpv.io/)|
|Browser | [Brave](https://brave.com/)|
|Editor | [NVIM](https://github.com/neovim/neovim)|

> [!NOTE]
> The config for neovim is [here](https://github.com/RunAtTekky/kickstart-modular.nvim/tree/macos)

## How to use these dotfiles?
> [!NOTE]
> I have created this [script](https://github.com/RunAtTekky/initial-setup-script/tree/macos) to install everything with just one single `bash` script

Currently, you'd have to `clone` the repo and run the `./install-all.sh` by yourself.

TODO: I will be creating a `init.sh` script which would be on my domain `runat.xyz/mac/init.sh`

So we can use something like this:
```bash
# For MacOS
bash <(curl -fsSL https://runat.xyz/mac/init.sh) # TODO
# For Arch
bash <(curl -fsSL https://runat.xyz/init.sh) # Works on Arch
```

This is what I currently use on my [Arch setup](https://github.com/RunAtTekky/dotfiles)
to install all the programs and configurations I use on my computer.
