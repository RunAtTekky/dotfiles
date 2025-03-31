import requests
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, "lc_solved.txt")

# Define the endpoint and headers
url = "https://leetcode.com/graphql"
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"  # This is just an example, use your own user agent or any generic one
}

# Define the query and variables
username = "RunAtMe"
data = {
    "query": """
    query userProblemsSolved($username: String!) {
        allQuestionsCount {
            difficulty
            count
        }
        matchedUser(username: $username) {
            problemsSolvedBeatsStats {
                difficulty
                percentage
            }
            submitStatsGlobal {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
        }
    }
    """,
    "variables": {
        "username": username
    }
}

# Make the POST request
response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    response_data = response.json()
    # Extract necessary details
    total_solved = next(item['count'] for item in response_data['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'] if item['difficulty'] == 'All')
    
    # Print and save to file in the script's directory
    print(total_solved)
    with open(output_file, "w") as file:
        file.write(f'{total_solved}')
else:
    # Read from the file in the script's directory
    try:
        with open(output_file, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: Could not fetch data and backup file not found")
