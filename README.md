# Managing my dotfiles
My repo for my Arch linux setup.
I had my own setup on Linux Mint which you can check out [here](https://github.com/RunAtTekky/dotfiles/tree/mint) 

Now I'm using [Omarchy](http://omarchy.org/) for ricing and I'm focusing on actual productivity rather than mindless ricing.

Check out the [WIKI](https://github.com/RunAtTekky/dotfiles/wiki)

# Screenshots
Fastfetch output
![LinuxSetup](https://i.postimg.cc/MWV9p0Bq/fastfetch.png)

Yazi
![Yazi](https://i.postimg.cc/ZTWvgT6C/screenshot-2025-08-26-00-59-56.png)

NVIM
![NVIM](https://i.postimg.cc/T26ypgFD/screenshot-2025-08-26-01-00-07.png)

Lazygit
![Lazygit](https://i.postimg.cc/w9G7DSnH/screenshot-2025-08-26-01-00-20.png)


# Programs I Use
Setup Script: [Omarchy](http://omarchy.org/)

WM/Compositor: [Hyprland](https://hypr.land/)

OS: [Arch Linux](https://archlinux.org/)

Shell: [ZSH](https://wiki.archlinux.org/title/Zsh)

Bar: [Waybar](https://github.com/Alexays/Waybar)

File Manager: [YAZI](https://github.com/sxyazi/yazi)

Application Launcher: [Walker](https://github.com/abenz1267/walker)

PDF Viewer: [Zathura](https://pwmt.org/projects/zathura/)

Image Viewer: [Swayimg](https://github.com/artemsen/swayimg)

Video Player: [MPV](https://mpv.io/)

Browser: [Zen](https://zen-browser.app/) | [Brave](https://brave.com/) | [Chromium](https://www.chromium.org/chromium-projects/)

Editor: [NVIM](https://github.com/neovim/neovim)

## Pre-requisites
```
git
stow
```

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

