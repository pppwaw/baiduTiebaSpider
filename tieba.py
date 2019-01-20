import requests,tiezi
from bs4 import BeautifulSoup as bs
from urllib import parse
url="https://tieba.baidu.com/f?kw="+input("请输入贴吧名字")+"&ie=utf-8"
r=requests.get(url)
rsoup=bs(r.text,"lxml")
lasturlcanshu=parse.urlparse(rsoup.find(class_="last pagination-item").get("href")).query#获取参数
pn=int(parse.parse_qs(lasturlcanshu)["pn"][0])#获取总pn
for i in range(0,pn+1,50):
    print("下一页")
    r = requests.get(url+"&pn="+str(i))
    rsoup = bs(r.text, "lxml")
    rtext=rsoup.find_all("a",class_="j_th_tit")
    rauthor=rsoup.find_all(class_="frs-author-name j_user_card")
    alist=0#authorlist
    for j in rtext:
        tmp=input("是否获取标题为\""+j.get("title")+"\",作者为\""+rauthor[alist].text+"\"的帖子?[Y,n]")
        alist+=1
        if tmp == "Y" or tmp == "y" or tmp == "":
            lz = input("是否只看楼主?[Y,n]")
            if lz == "Y" or lz == "y" or lz == "":
                tiezi.gettiezi("https://tieba.baidu.com"+j.get("href"),True)
            else:
                tiezi.gettiezi("https://tieba.baidu.com" + j.get("href"), False)