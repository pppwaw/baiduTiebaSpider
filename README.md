# baiduTiebaSpider  
百度贴吧爬虫,使用python3,调用模块requests,re,beautifulsoup4,lxml  
tiezi.py:  
  爬取帖子内所有发言，无法爬楼中楼，可选只看楼主,图片加文字一起爬，保存格式html，带换行  
  函数gettiezi():  
    第一个参数为url,为帖子地址，字符串型，必须加http://或https://  
    第二个参数为是否只看楼主，布尔型，默认为True  
tieba.py:  
  爬取贴吧内所有帖子，会自动调用tiezi.py,无参数  
