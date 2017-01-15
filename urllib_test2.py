#-*-coding:utf-8-*-
import urllib

def callback(a,b,c):
    """
    @a:是目前为止传递的数据块数量
    @b:是每个数据块的大小，单位的byte
    @c:是远程文件的大小
    """
    download_progress = 100.0 * a * b / c

    if download_progress > 100:
        download_progress = 100
    print "%.2f%%" % download_progress
url = "http://www.163.com"
urlpath="/home/git/home163.html"
urllib.urlretrieve(url,urlpath,callback)
