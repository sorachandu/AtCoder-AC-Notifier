import requests
import json
import os
import math

filename = "all_problems.json"

def get_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "..", "data", filename)
    return file_path


def get_problems():
    api_path = "https://kenkoooo.com/atcoder/resources/problem-models.json"
    response = requests.get(api_path)
    if response.status_code != 200:
        return "通信エラーが発生しました"
    json_data = response.json()
    problems = {}
    for i in json_data:
        if "difficulty" in json_data[i]:
            diff = json_data[i]["difficulty"]
            if diff < 400:
                diff = round( 400 / math.exp((400-diff)/400) )
            experimental = json_data[i]["is_experimental"]
        else:
            diff = -1
            experimental = False
        
        if "title" in json_data[i]:
            title = json_data[i]["title"]
        else:
            title = ""
        problems[i] = dict()
        problems[i]["difficulty"] = diff
        problems[i]["is_experimental"] = experimental
        problems[i]["title"] = title
    
    write_all_problems(problems)
    add_problems_name()

def write_all_problems(problems):
    path = get_path()
    with open(path,"w") as f:
        json.dump(problems, f, indent=2)


def read_all_problems():
    path = get_path()
    with open(path) as f:
        ans = json.load(f)
    return ans

def add_problems_name():
    problems = read_all_problems()
    api_path = "https://kenkoooo.com/atcoder/resources/problems.json"
    response = requests.get(api_path)
    if response.status_code != 200:
        return "通信エラーが発生しました"
    json_data = response.json()
    for i in json_data:
        problem_id = i["id"]
        problem_name = i["name"]
        contest_id = i["contest_id"]
        if problem_id in problems:
            problems[problem_id]["title"] = problem_name
            problems[problem_id]["contest_id"] = contest_id
    write_all_problems(problems) 

