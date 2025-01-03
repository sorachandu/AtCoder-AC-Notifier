import requests
from bs4 import BeautifulSoup

def get_atcoder_rating(username):
    # AtCoderのユーザープロフィールページのURL
    url = f'https://atcoder.jp/users/{username}'

    # リクエストを送信してHTMLを取得
    response = requests.get(url)
    if response.status_code != 200:
        return None

    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        img_list = soup.find_all("img",class_="user-rating-stage-m")
        rating = img_list[0].find_parent("td").find("span").text
        highest = img_list[1].find_parent("td").find("span").text
        username = soup.find("a",class_="username").find("span").text
    except:
        return None

    return rating,highest,username


# 使用例
username = 'noshinn'  # ここにAtCoderのユーザー名を入力
#rating = get_atcoder_rating(username)
#print(rating)
#if rating:
    #print(f"{username} の現在のレート: {rating}")

