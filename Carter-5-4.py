# @Time    : 2018/4/22 16:22
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import urllib.request
file = urllib.request.urlopen('http://manning.com/sande2/data/message.txt')
message = file.read()
print(message)

# import html2text
# message = html2text.html2text(message)
# print(message)