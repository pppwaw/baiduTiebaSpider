import requests,re
from bs4 import BeautifulSoup as bs




def gettiezi(url,zhikanlouzhu=True):
    apattrn = re.compile('">' + '(.*?)' + '</a>', re.S)
    rstr = r"[\/\\\:\*\?\"\<\>\|]"#不允许的文件名内字符
    if zhikanlouzhu:#只看楼主
        r=requests.get(url+"?see_lz=1")
        rsoup=bs(r.text,"lxml")
        file = open(re.sub(rstr, "_", rsoup.title.get_text() + ".html"), "w",encoding="utf-8")
        page=int(rsoup.find_all("span", class_="red")[1].get_text())#获取椰树
        for i in range(1, page+1):#页数循环
            r = requests.get(url+"?see_lz=1&pn="+str(i))
            rsoup = bs(r.text, "lxml")
            rtext = rsoup.find_all(class_="d_post_content j_d_post_content")

            for j in range(len(rtext)):
                for k in rtext[j].contents:
                    if "</a>" in str(k):
                        #print(apattrn.findall(str(k)))
                        if k.get("href") == apattrn.findall(str(k))[0]:
                            file.write(str(k))
                        else:
                            file.write(apattrn.findall(str(k))[0])

                    else:
                        #print(str(k))
                        file.write(str(k))
                file.writelines("</br>")
    else:
        r = requests.get(url)
        rsoup = bs(r.text, "lxml")
        file = open(rsoup.title.get_text() + ".html", "w")
        for i in range(1, int(rsoup.find_all("span", class_="red")[1].get_text())+1):

            r = requests.get(url+"?pn="+str(i))
            rsoup = bs(r.text, "lxml")
            rtext = rsoup.find_all(class_="d_post_content j_d_post_content")

            for j in range(len(rtext)):
                for k in rtext[j].contents:
                    #if "br" not in k:
                    file.write(str(k))
                file.writelines("</br>")
    return(True)
if __name__ == "__main__":
    url = input("百度贴吧地址:")
    tmp = input("是否加只看楼主[Y,n]:")

    print(gettiezi(url,tmp == "Y" or tmp == "y" or tmp == ""))