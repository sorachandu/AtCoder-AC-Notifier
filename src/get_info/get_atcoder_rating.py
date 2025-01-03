import requests
from bs4 import BeautifulSoup

def get_atcoder_rating(username):
    # AtCoderのユーザープロフィールページのURL
    url = f'https://atcoder.jp/users/{username}'

    # リクエストを送信してHTMLを取得
    response = requests.get(url)
    if response.status_code != 200:
        return "通信に失敗したか、存在しないユーザーです"

    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        rating = soup.find("th",class_ = "no-break", text = "Rating").find_parent("tr").find("td").find("span").text
        highest = soup.find("th",class_ = "no-break", text = "Highest Rating").find_parent("tr").find("td").find("span").text
        username = soup.find("a",class_="username").find("span").text
    except:
        return "atcoderのユーザーページの解析でエラーが発生しました"

    return rating,highest,username


# 使用例
username = 'noshinn'  # ここにAtCoderのユーザー名を入力
#rating = get_atcoder_rating(username)
#print(rating)
#if rating:
    #print(f"{username} の現在のレート: {rating}")

