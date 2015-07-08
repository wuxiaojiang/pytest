import urllib2,re,os,xlrd,sys,subprocess
def get_name_list(name):
    path = os.getcwd()
    path = '%s//%s'%(path,name)
    list1 = os.listdir(path)
    return path,list1
def find(path,name,word):
    data = xlrd.open_workbook('%s//%s'%(path,name))
    table = data.sheet_by_index(0)
    nrows = table.nrows
    flag = 0
    for i in range(nrows):
        if word in table.row_values(i):
            #print '[*]Get result in row %d!'%(i+1)
            flag = 1
    return flag
def get_file_list():
    url = 'http://211.70.49.127/excel/'
    req = urllib2.Request(url)
    web = urllib2.urlopen(req)
    url = web.geturl()
    print '[*]Get data from %s'%url
    text = web.read()
    list1 = re.findall(r'<A HREF="(.*?)">',text)
    #for i in list1:
    #    print i
    print '[*]File list done!'
    return list1    
def search_file(list1,num_of_class):
    #'JC17012'
    list2=[]
    num = 0
    for i in list1:
        if num_of_class in i:
            list2.append(i)
            num +=1
    print '[*]Get %d result'%num
    return list2
def set_path(cla):
    path = os.getcwd()
    addr = '%s//%s'%(path,cla)
    return addr    
def save(url,name,addr):
    try:
        web = urllib2.urlopen(url)
        xls = web.read()
        fil = file('%s//%s'%(addr,name),'wb')
        fil.write(xls)
        fil.flush()
        fil.close()
    except(IOError):
        pass
