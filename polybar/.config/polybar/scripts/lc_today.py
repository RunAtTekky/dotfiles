from urllib.request import urlopen
import json

def print_data():
    url = "https://leetcode-stats-api.herokuapp.com/runatme"
    # url = f"https://alfa-leetcode-api.onrender.com/{username}/solved"
    
    # store the response of URL 
    response = urlopen(url) 
    
    # storing the JSON response from url in data 
    json_data = json.loads(response.read()) 
    
    solved_problems = json_data["totalSolved"]

    # submission_today = json_data["submissionCalendar"][0]

    # first_key = next(iter(json_data["submissionCalendar"]))
    # first_value = json_data["submissionCalendar"][first_key]
    # print(first_value)

    last_key = list(json_response["submissionCalendar"].keys())[-1]
    last_value = json_response["submissionCalendar"][last_key]
    print(last_value)


try:
    print_data()
except:
    print("API DOWN")
