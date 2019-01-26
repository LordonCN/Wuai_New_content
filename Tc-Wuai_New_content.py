import requests
import re
import time
#目前只支持8页
web_site   = 'https://www.52pojie.cn/forum.php?mod=guide&view=newthread&page=' #网址 可用循环多次
title_sign = 'blank" class="xst" >(.*?)</a>'                             #标题特征
url_sign   = 'a href="(.*?)" target="_blank" class="xst" >'              #链接特征
class Spider(object):

    def start_request (self,websit1) :
        response = requests.get(websit1)
        res = response.text  # 将信息从前端代码拿出
        # 正则表达式
        question_list = re.findall(title_sign, res) #标题特征
        question_url  = re.findall(url_sign, res)   #链接特征
        print("                              吾爱破解论坛中最新发表内容如下所示：")
        for quelist, queurl in zip(question_list, question_url):  #列表显示标题与部分地址
            print(" *-----------------------------------------------------------------------------------------------*")
            print("                      "+quelist)#打印出来
        return question_list,question_url  #将问题名称与地址输出至list，url保存
    def seach_keyword(self,question_list,question_url):
        number = 0
        sum_number = 0
        sign = input("获取问题链接，请输入所要查询的关键字:")
        print(" *-----------------------------------------------------------------------------------------------*")
        for i in question_list:
            if re.findall(sign, i) == [sign]:#匹配相同字段，对应链接顺序
                print(i,"---请点击-->","https://www.52pojie.cn/"+question_url[number])
                sum_number +=1
            number = number + 1
        if sum_number == 0:
            print("                      目前最新发布中没有搜索到相关内容。")
print("\n", "[原创]吾爱破解 https://www.52pojie.cn/")
print("      更多代码   -->Github : https://github.com/Tcloser")
page_now = 1#先输出第一页内容
spider = Spider()
(list,url) = spider.start_request(web_site+str(page_now))#调用Spider类中的请求函数
spider.seach_keyword(list,url)
while 1: #进行翻页处理
    next_page = input('    是否继续向下翻页查看？确定按回车退出的话直接关了吧:')
    if next_page == '':
        page_now = page_now+1#翻页
        (list, url) = spider.start_request(web_site+str(page_now))
        spider.seach_keyword(list, url)
    else :
        break
print("此页面停留时间为1分钟")
time.sleep(60)
