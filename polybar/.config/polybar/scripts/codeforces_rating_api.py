#!/sbin/python3
import sys
import json
import requests
import os  # Add this import

URL = "https://codeforces.com/api/user.status?handle=RunAt"
RATINGS = [
    800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700,
    1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700,
    2800, 2900, 3000,
]

def fetch_count(count):
    "Function to fetch problems solve for each rating"
    try:
        res = requests.get(URL)
        if not res.ok:
            return
        res_json = res.json()
        for x in RATINGS:
            count[x] = 0
        s = set()
        for x in res_json["result"]:
            problemID = str(x['problem']['contestId']) + str(x['problem']['index'])
            if(problemID not in s): 
                s.add(problemID)
                rating = x["problem"].get("rating", None)
                verdict = "OK" == x.get("verdict", "")
                if rating and verdict:
                    count[rating] += 1
    except Exception as e:
        return

def range_count(count, left, right):
    """
    Function to calculate solved questions within the rating
    range: [left, right]
    """
    solved = 0
    for x in count.keys():
        if left <= x <= right:
            solved += count[x]
    return solved

def main():
    "Main module"
    count = {}
    
    # Get the directory where the script is running
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create a new directory in the same location
    new_dir_name = "cf_data"
    new_dir_path = os.path.join(script_dir, new_dir_name)
    
    # Create the directory if it doesn't exist
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)
    
    try:
        fetch_count(count)
        # Save the file in the new directory
        file_path = os.path.join(new_dir_path, "cf_solved.json")
        with open(file_path, "w") as file:
            json.dump(count, file)
    except:
        # Read from the new directory
        file_path = os.path.join(new_dir_path, "cf_solved.json")
        with open(file_path, "r") as file:
            count = json.load(file)
            
    solved = range_count(count, int(sys.argv[1]), int(sys.argv[2]))
    print(solved)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(-1)
        sys.exit()
    main()
