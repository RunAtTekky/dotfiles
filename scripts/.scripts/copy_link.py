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
    for idx, [title,link] in enumerate(name_link):
        print(idx, title)

    print('\nChoose your video index: ')

    chosen = False
    while not chosen:
        user_choice = int(input())

        if user_choice < 0 or user_choice >= len(name_link):
            print("Not available. Try again.")
        else:
            chosen = True
    
    return user_choice

# Get data
processed_text = get_data()

# Convert data to list
name_link = convert_to_list(processed_text)

# UI
user_choice = get_userchoice(name_link)

title_chosen = name_link[user_choice][0]
link_chosen = name_link[user_choice][1]

# Copy to clipboard
os.system(f'echo -n {link_chosen} | xclip -selection clipboard')

print(f'\nCopied URL for \n{title_chosen}')