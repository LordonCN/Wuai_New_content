import requests
import re
import time

class Spider(object):#类的首字母大写

    def start_request(self):
        response = requests.get("https://www.52pojie.cn/forum.php?mod=guide&view=newthread")# 目标页面
        res = response.text  # 将信息从前端代码拿出
        # 正则表达式部分
        question_list = re.findall('blank" class="xst" >(.*?)</a>', res)  #特征： 'blank" class="xst" >(.*?)</a>'
        question_url  = re.findall('a href="(.*?)" target="_blank" class="xst" >', res)#特征： a href = "thread-859123-1-1.html"target = "_blank"class ="xst" >
        print("                              吾爱破解论坛中最新发表内容如下所示：")
        for quelist, queurl in zip(question_list, question_url):  # 列表显示标题与部分地址
            print("*-----------------------------------------------------------------------------------------------*")
            print("                      "+quelist)#打印标题列表
        print("\n","[原创]吾爱破解 https://www.52pojie.cn/")
        print("      更多代码   -->Github : https://github.com/Tcloser")
        sign = input("获取问题链接，请输入所要查询的关键字:")
        number = 0 #作循环计数
        for i in question_list:
            if re.findall(sign, i) == [sign]:
                print(i,"---请点击-->","https://www.52pojie.cn/"+question_url[number])
            number = number + 1

spider = Spider()
spider.start_request()

print("此页面停留时间为1分钟")
time.sleep(60)
