# Managing my dotfiles
Started with Linux Mint, check it [here](https://github.com/RunAtTekky/dotfiles/tree/mint)

This branch is for my Arch linux setup.

Now I'm using [Omarchy](http://omarchy.org/) so I can focus on actual productivity rather than mindless ricing.

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

# HOW to use
> [!NOTE]
> I use a [script](https://github.com/RunAtTekky/initial-setup-script) to copy config files of desired programs

```bash
git clone https://github.com/RunAtTekky/dotfiles.git "$HOME/dotfiles"
```


This will create a directory `~/dotfiles/`

```bash
cd "$HOME/dotfiles/"
# Install program if not installed
# Remove the config files for the program
rm -rf "$HOME/.config/kitty" 
# Use the config files from out dotfiles
stow kitty
```

This will set the configuration for your Kitty Terminal Emulator

## Structure

If you want to store the dotfiles for `kitty` you need to have the same structure.

The config files for `kitty` are in `~/.config/kitty/kitty.conf`
So you will create a folder inside `dotfiles` and structure it exactly like the actual path

```
├── kitty
│   └── .config
│       └── kitty
│           └── kitty.conf

```

## Creating symlink
Now you have copied your desired configuration to `$HOME/dotfiles/kitty/`

Now we will create symlink

```bash
# Remove the actual config files
rm -rf "$HOME/.config/kitty"
# Symlink files in ~/dotfiles/kitty
stow kitty
```

> The changes you make in dotfiles will appear in the actual config location

