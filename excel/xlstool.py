from __future__ import division
from xls_def import *
import urllib2,re,os,xlrd,sys,subprocess
class search():
    def __init__(self):
        pass
    def download(self,d_name):
        list1 = get_file_list()
        list2 = search_file(list1,d_name)
        addr = set_path(d_name)
        subprocess.Popen('mkdir %s'%d_name,shell = True)
        t = len(list2)
        for i in range(t):
            url = 'http://211.70.49.127%s'%list2[i]
            name = list2[i].split('/excel/')[1]
            save(url,name,addr)
            x = i+1
            x = x/t*100
            p = int(x/5)
            point = p*'='
            space = (20-p)*' '
            sys.stdout.write ("\r[*]Download:%s%% [%s>%s]"%(int(x),point,space))
            sys.stdout.flush()
        print '\n[*]Download accomplish!'
    def local(self,d_name,s_name):
        path,n_list = get_name_list(d_name)
        print '[*]Search objest:%s'%d_name
        print '[*]Key word : %s'%s_name
        t = len(n_list)
        r_list = []
        for i in range(t):
            n = n_list[i]
            tx = find(path,n,s_name)
            if tx == 1:
                r_list.append(n)
            x = i+1
            x = x/t*100
            p = int(x/5)
            point = p*'='
            space = (20-p)*' '
            sys.stdout.write("\r[*]Search persent:%d%% [%s>%s]"%(int(x),point,space))
            sys.stdout.flush()
        print '\n[*]Local search accomplish!'
        if len(r_list) == 0:
            print '[*]No result!'
        else:
            for i in r_list:
                print '[*]Result : %s'%i
            
            
