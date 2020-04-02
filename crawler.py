import urllib.request as req
from bs4 import BeautifulSoup

# NSWITCH_BOARD = 
url_nswitch = "https://www.ptt.cc/bbs/NSwitch/index.html"
url_gossiping = "https://www.ptt.cc/bbs/Gossiping/index.html"

def get_titles(url):
    # fetch website
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    
    # use bs4 to parse specific data
    root = BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a:
            print(title.a.string)

    # return url of next page
    next_page_btn = root.find("a", string="‹ 上頁")
    return next_page_btn["href"]

def get_multipages(board, url, page_count=None):
    print("Articles in {}:".format(board))
    next_page = url

    if page_count:
        count = 0    
        while count < page_count:
            next_page = "http://www.ptt.cc" + get_titles(next_page)
            count += 1
    else:
        get_titles(next_page)

def run():
    get_multipages("NSwitch", url_nswitch)
    get_multipages("Gossiping", url_gossiping, 3)

if __name__ == '__main__':
    run()