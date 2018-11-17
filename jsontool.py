import json
import socket
from urllib.parse import urlparse
from urllib.request import urlretrieve
import os


def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False

def allprint(d):
    for k, v in d.items():
        if isinstance(v, dict):
            allprint(v)
        else:
            print("{0} : {1}".format(k, v))
            print(v)

def print_url(d):
    for k,v in d.items():
        if isinstance(v, dict):
            print_url(v)
        else:
            if (isinstance(v,str)):
                #print(v)
                #print(type(v))
                if(uri_validator(v)):
                    print(v)
 
def save_img(img_url,file_name,file_path='images'):
    #保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 images 文件夹
    try:
        if not os.path.exists(file_path):
            print('文件夹',file_path,'不存在，重新建立')
            #os.mkdir(file_path)
            os.makedirs(file_path)
        #获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        #拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
       #下载图片，并保存到文件夹中
        urlretrieve(img_url,filename=filename)
    except IOError as e:
        print('文件操作失败',e)
    except Exception as e:
        print ('错误 ：',e)

with open('776875059.json',encoding='utf-8') as f:

    data = json.load(f)
    #allprint(data)
    print_url(data)
    test_img ="https://img1.doubanio.com/view/subject/l/public/s29845508.jpg"
    save_img(test_img,"test_img")