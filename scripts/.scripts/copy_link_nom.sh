#!/bin/sh

data=$(nom list)

# Extract titles and URLs
titles=$(echo "$data" | grep -v '^  - ')  # Extract only the titles
urls=$(echo "$data" | grep '^  - ' | sed 's/  - //')  # Extract only the URLs

# Use dmenu to let user select a title
# selected_title=$(echo "$titles" | dmenu -i -l 10 -p "Select a Video:")
selected_title=$(echo "$titles" | rofi -dmenu -i)

[ -z "$selected_title" ] && exit

# Find the index of the selected title
index=$(echo "$titles" | grep -n "$selected_title" | cut -d: -f1)

# Get the corresponding URL
selected_url=$(echo "$urls" | sed -n "${index}p")

# Copy the URL to clipboard (Supports X11 and Wayland)
if command -v xclip >/dev/null 2>&1; then
    echo -n "$selected_url" | xclip -selection clipboard
elif command -v wl-copy >/dev/null 2>&1; then
    echo -n "$selected_url" | wl-copy
else
    echo "Clipboard tool not found. Install xclip or wl-clipboard."
    exit 1
fi

echo "Copied: $selected_url"

