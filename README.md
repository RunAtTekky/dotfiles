# Managing my dotfiles
Use this repo to get back to the configuration of various programs you use on a new computer.

Check out the [WIKI](https://github.com/RunAtTekky/dotfiles/wiki)

> Click this to watch YT video

[YT Video](https://youtu.be/fVjRIJNxGK8)

# Screenshots
![Typing Speed](https://i.imgur.com/6kQDOYL.png)

![Footy 4 Windows](https://i.imgur.com/sTbnrdq.png)

![Footy 3 Windows](https://i.imgur.com/4mIljue.png)


# Programs I Use
WM: [i3WM](https://github.com/i3/i3)

OS: [Linux Mint](https://linuxmint.com/)

Shell: [ZSH](https://wiki.archlinux.org/title/Zsh)

Compositor: [Picom](https://github.com/ibhagwan/picom)

Bar: [Polybar](https://github.com/polybar/polybar)

File Manager: [LF File Manager](https://github.com/gokcehan/lf)

Application Launcher: [Rofi](https://github.com/davatorium/rofi)

PDF Viewer: [Zathura](https://pwmt.org/projects/zathura/)

Image Viewer: [SXIV](https://github.com/xyb3rt/sxiv)

Video Player: [MPV](https://mpv.io/)

Browser: [Zen](https://zen-browser.app/)

Editor: [VSCode](https://github.com/microsoft/vscode) | [NVIM](https://github.com/neovim/neovim)

## Pre-requisites
```
git
stow
```
<!-- - `git` -->
<!-- - `stow` -->

## Getting the dotfiles
Clone this repo to your home directory
> Home directory is `~` just use `cd ~` or `cd` to go to home directory

```bash
git clone git@github.com:RunAtTekky/dotfiles.git
```


This will create a directory `~/dotfiles/`

```bash
cd dotfiles/
```

Now we use stow to get whatever config we want

> Keep in mind that you need to install the program first and then use the following command

```bash
stow nvim
```

This will set the config for your NeoVim

# Creating new dotfiles

> Install the program and create your config as you would normally

> Create a folder structure inside dotfiles folder same as the actual dotfile

> Let's say we have Picom config in `~/.config/picom/` directory

> We want to create similar structure in dotfiles

> Create the following directories `~/dotfiles/picom/.config/picom/` and copy the contents of actual config here

## Copying config files
This command will copy actual config files to our `dotfiles` 

```bash
cp -r ~/.config/picom/ ~/dotfiles/picom/.config/picom/
```

## Creating symlink
Use this command to create symlink between actual config files and the config files we have in `dotfiles`

```bash
stow --adopt picom
```

> Now actual config and files in our dotfiles are linked

> If you change one other will also change

