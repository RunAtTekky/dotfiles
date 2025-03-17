import os
import subprocess

def get_data():
    result = subprocess.run(['nom', 'list'], text=True, capture_output=True)
    processed_text = result.stdout

    processed_text = processed_text.splitlines()
    return processed_text
    
def convert_to_list(processed_text):
    name_link = []
    for i in range(0, len(processed_text)-1, 2):
        title = processed_text[i]
        link = processed_text[i+1][4:]

        name_link.append([title,link])
    return name_link

def get_userchoice(name_link):
    title_string = ""

    for [title,_] in name_link:
        title_string += title
        title_string += "\n"

    # Take input with ROFI
    user_choice_title = subprocess.run(['rofi', '-dmenu', '-i'], input=title_string, text=True, capture_output=True)
    user_choice_title = user_choice_title.stdout

    for idx, [title, link] in enumerate(name_link):
        if title == user_choice_title[0:-1]:
            return idx

    return -1

def copy_and_output(user_choice):
    if user_choice == -1:
        return

    title_chosen = name_link[user_choice][0]
    link_chosen = name_link[user_choice][1]

    # Copy to clipboard
    os.system(f'echo -n {link_chosen} | xclip -selection clipboard')

    print(title_chosen)
    print(link_chosen)

# Get data
processed_text = get_data()

# Convert data to list
name_link = convert_to_list(processed_text)

# UI
user_choice = get_userchoice(name_link)

# Copy and output
copy_and_output(user_choice)
