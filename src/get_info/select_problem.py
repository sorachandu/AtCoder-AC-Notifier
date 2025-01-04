from src.get_info.get_atcoder_rating import get_atcoder_username
from src.get_info.atcoder_problems import read_ac, renew
import json
import os
import random

def select_problem(min_diff, max_diff, username):
    username = get_atcoder_username(username)
    if username == None:
        return ("通信に失敗したか、存在しないユーザーです。")
    
    if min_diff < 0:
        min_diff = 0

    if min_diff > max_diff:
        return ("diffの指定が正しくないです。")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    all_problems_path = os.path.join(current_dir, "..", "..", "data", "all_problems.json")

    #all_problemsを読み込みたい
    with open (all_problems_path) as f:
        problems = json.load(f)

    ac = read_ac(username)
    if ac == None:
        return ("先にregisterコマンドを使用して登録してください")
    
    renew(username)
    ac = read_ac(username)
    can_select = dict()
    
    for i in problems:
        if "difficulty" not in problems[i]:
            continue

        if problems[i]["difficulty"] < min_diff or problems[i]["difficulty"] > max_diff:
            continue

        if i in ac:
            continue

        can_select[i] = problems[i]

    if len(can_select) == 0:
        return ("指定された条件に当てはまる問題がありません")

    chose_problem = random.choice(list(can_select.keys()))
    diff = can_select[chose_problem]["difficulty"]
    contest_id = can_select[chose_problem]["contest_id"]
    return (f"https://atcoder.jp/contests/{contest_id}/tasks/{chose_problem}")
    


#select_problem(0,10,"noshinn")
