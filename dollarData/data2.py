import urllib.request
from bs4 import BeautifulSoup

#웹페이지의 소스를 가져온다.
url = "https://www.google.com/search?q=australian+5+dollar+note+clear+image&rlz=1C1ONGR_enAU1032AU1032&hl=ko&sxsrf=APwXEdcOGp7A5A0R5L9BxtKUON0rCg2Mog:1681112702781&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjl3-fr6J7-AhWJD94KHcz_BCkQ_AUoAXoECAEQAw&biw=1536&bih=714&dpr=1.25"
fp = urllib.request.urlopen(url)
source = fp.read()
fp.close()

#소스에서 img_area 클래스 하위의 소스를 가져온다.
soup = BeautifulSoup(source, 'html.parser')
soup = soup.find("p",class_ = "img_area")

#이미지 경로를 받아온다.
imgURL = soup.find("img")["src"]

print(imgURL)

