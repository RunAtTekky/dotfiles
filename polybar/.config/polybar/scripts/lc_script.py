import requests

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
    # easy_solved = next(item['count'] for item in response_data['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'] if item['difficulty'] == 'Easy')
    # medium_solved = next(item['count'] for item in response_data['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'] if item['difficulty'] == 'Medium')
    # hard_solved = next(item['count'] for item in response_data['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'] if item['difficulty'] == 'Hard')

    # Format and print output
    print(total_solved)

    with open("lc_solved.txt", "w") as file:
        file.write(f'{total_solved}')

    # output = f"""
    # The User: {username}
    # solved {total_solved} problems. The category count is:
    # Easy: {easy_solved}
    # Medium: {medium_solved}
    # Hard: {hard_solved}
    # """
    #
    # print(output)

else:
    with open("lc_solved.txt", "r") as file:
        content = file.read()
        print(content)
    # print(f"Error {response.status_code}: {response.text}")
