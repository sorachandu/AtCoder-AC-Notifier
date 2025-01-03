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
            problems[i] = [diff, json_data[i]["is_experimental"]]
        else:
            problems[i] = [0,False]
    return problems

def write_all_problems(problems):
    path = get_path()
    with open(path,"w") as f:
        json.dump(problems, f, indent=2)


def read_all_problems():
    path = get_path()
    with open(path) as f:
        ans=f.read()
    return ans

#write_all_problems(get_problems())
