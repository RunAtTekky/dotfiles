#!/sbin/python3

from urllib.request import urlopen
import json

def print_data():
    url = "https://leetcode.com/api/problems/algorithms/"
    # url = f"https://alfa-leetcode-api.onrender.com/{username}/solved"
    
    # store the response of URL 
    response = urlopen(url) 
    print(response)
    
    # storing the JSON response from url in data 
    json_data = json.loads(response.read()) 

    print(json_data)
    
    solved_problems = json_data["num_solved"]

    print(solved_problems)

try:
    url = "https://leetcode.com/api/problems/algorithms/"
    # url = f"https://alfa-leetcode-api.onrender.com/{username}/solved"
    
    # store the response of URL 
    response = urlopen(url) 
    print(response)
    
    # storing the JSON response from url in data 
    json_data = json.loads(response.read()) 

    print(json_data)
    
    solved_problems = json_data["num_solved"]

    print(solved_problems)
except:
    print("API DOWN")

