import sys,re
class dna():
    def __init__(self):
        self.msg = ''
        self.string = ''
    def open_fasta(self,path):
        try:
            fil = open(path)
            text = fil.read()
            f = text.split('genome')
            self.msg = f[0]
            self.string = f[1]
        except(IOError):
            print 'path is error'
            sys.exit(0)
    def find_string(self,string):
        list1=[]
        start = 0
        while True:
            index = self.string.find(string,start)
            if index == -1:
                break
            list1.append(index)
            start = index+1
        print list1
        l = len(list1)
        for i in range(l):
            print '----------------------------------------------------'
            if i!=l-1:
                print self.string[list1[i]:list1[i+1]-1]
            else:
                print self.string[list1[i]:]

