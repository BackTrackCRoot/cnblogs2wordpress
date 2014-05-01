#!/usr/env python
# -*- coding: GBK –*-


## Script Name: cnblogs2wordpress
## Date: 2014-04-29
## Author: CRoot,Caesar@11111010

from xml.etree import ElementTree
import xmlrpclib,datetime

def load():
    #print "请输入您要转换的.xml文件路径："
    XMLFilename = raw_input("请输入您要转换的.xml文件路径:")
    fo = open(XMLFilename).read()
    #fo = 'blog.xml'
    read_xml(fo)

def read_xml(text):
    wp_username = raw_input("WordPres 账号：")
    wp_password = raw_input("WordPress 密码：")
    wp_url = raw_input("您的博客xmlrpc路径：")
    root = ElementTree.fromstring(text)
    lst_title = root.getiterator("title")
    lst_date = root.getiterator("pubDate")
    lst_article = root.getiterator("description")
    for i in range(0, len(lst_title)):
        #print "=============================================="
        #print lst_title[i].text.encode('gb2312')
        #print lst_date[i].text.encode('gb2312')
        #print lst_article[i].text.encode('gb2312')
		# print lst_date[i].text
		# print month2num(lst_date[i].text)
        #rs = updatetowp(wp_url,wp_username,wp_password,lst_title[i].text,month2num(lst_date[i].text),lst_article[i].text,'','')
        rs = updatetowp(wp_url,wp_username,wp_password,lst_title[i].text,month2num(lst_date[i].text),addMore(lst_article[i].text),'','')
        print rs
    
    
def updatetowp(wp_url,wp_username,wp_password,title,sdate,content,tags,categories):
    wp_blogid=''
    status_published = 0
    server = xmlrpclib.ServerProxy(wp_url)
    # #中文的gbk转换成utf8格式, 不转换是会出错
    # categories= [categories.decode('gbk','ignore').encode('utf8','ignore')]
    # #中文的gbk转换成utf8格式
    # title=title.decode('gbk','ignore').encode('utf8','ignore')
    # #中文的gbk转换成utf8格式
    # content=content.decode('gbk','ignore').encode('utf8','ignore')
	#中文的gbk转换成utf8格式, 不转换是会出错
    categories= [categories.encode("UTF-8")]
    #中文的gbk转换成utf8格式
    title=title.encode("UTF-8")
    #中文的gbk转换成utf8格式
    content=content.encode("UTF-8")
    date_created=xmlrpclib.DateTime(datetime.datetime.strptime(sdate, "%Y-%m-%d %H:%M"))
    data = {'title': title, 'description': content, 'dateCreated': date_created , 'categories':categories, 'mt_keywords': tags,'post_status':'publish'}
    post_id = server.metaWeblog.newPost(wp_blogid, wp_username,wp_password, data, status_published)
    return post_id
    
def month2num(otime):
    month2num = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    result = ''
    weekday = otime[0:3]
    day = otime[5:7]
    month = str(month2num.index(otime[8:11]) + 1)
    year = otime[12:16]
    hour = otime[17:19]
    minute = otime[20:22]
    second = otime[23:25]
    
    result = year + '-' + month + '-' + day + ' ' + hour + ':' + minute
    return result

# def addMore(ostr):
    # ipos = 300
    # if(len(ostr) > ipos):
        # while(ostr[ipos:ipos+1] == '<' or ostr[ipos:ipos+1] == '>'):
            # ipos -= 1
        # ostr = ostr[0:ipos] + '<!--more-->' + ostr[ipos+1:len(ostr)]
        # print ostr
    # return ostr
def addMore(ostr):
    ipos = 320
    if(len(ostr) > ipos):
        ostr = ostr[0:ipos] + '<!--more-->' + ostr[ipos+1:len(ostr)]
        # ostr = ostr[0:ipos] + '<!- --><!--more-->' + ostr[ipos+1:len(ostr)]
    return ostr

if __name__ == '__main__':
    load()
    #updatetowp("http://www.unixcroot.tk/xmlrpc.php","","","test112","content2222",'','')