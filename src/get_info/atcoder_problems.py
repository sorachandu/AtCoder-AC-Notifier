import requests
import json
import os
import time
from get_atcoder_rating import get_atcoder_rating

def get_path(username,filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "..", "data", username, filename)
    return file_path

def get_submissions(user_id, unix_second):
    api_path = "https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user=" + user_id + "&from_second=" + str(unix_second)
    response = requests.get(api_path)
    json_data = response.json()
    if len(json_data) == 0:
        return dict(), unix_second
    last_submission_time = json_data[-1]["epoch_second"]
    ans = select_ac_only(json_data)
    return ans, last_submission_time


def select_ac_only(submissions: dict):
    ans = {}
    for submission in submissions:
        if type(submission) != dict:
            continue
        if submission["result"] != "AC":
            continue
        ans[submission["problem_id"]] = "AC"
    return ans 

#sub,time = get_submissions("noshinn", 0)
#print(sub)

def write_ac(username, submissions, acs):
    path = get_path(username, username+"_ac.json")
    for submission in submissions:
        if submission not in acs:
            acs[submission] = "AC"
    with open(path,"w") as f:
        json.dump(acs, f, indent=2)

def read_ac(username):
    path = get_path(username, username+"_ac.json")
    with open(path) as f:
        ans = json.load(f)
    return ans


def write_info(username, unix_second):
    path = get_path(username, username+"_info.json")
    ans = {}
    ans["unix_second"] = unix_second
    ans["rating"] = get_atcoder_rating(username)[0]
    ans["highest"] = get_atcoder_rating(username)[1]
    with open(path, "w") as f:
        json.dump(ans, f, indent=2)

def read_info(username):
    path = get_path(username, username+"_info.json")
    with open(path) as f:
        ans = json.load(f)
    return ans
    

def renew(username):
    userinfo = read_info(username)
    unix_second = int(userinfo["unix_second"])
    #unix 取得して2日分は取る
    unix_now = int(time.time())
    unix_second = min(unix_now-24*60*60*2,unix_second)
    submissions, unix_second = get_submissions(username, unix_second)
    acs = read_ac(username)
    write_ac(username, submissions, acs)
    write_info(username,unix_second)
    
#renew("amesyu")

