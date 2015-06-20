import sys,binascii
try:
    fil = open('1.png','rb+')
except(IOError):
    print 'no such file'
    sys.exit(0)
text = fil.read()

list1=[]
for i in range(8):
    c = '%s'%hex(ord(text[i]))
    c = c.split('0x')[1]
    if len(c)<2:
        c = '%s%s'%(0,c)
    list1.append(c)
header = ''.join(list1)
header = '%s%s'%('0x',header)
print header
h = text[0:8]
head = binascii.hexlify(h)
print head
print '------------------------------'
for i in range(25):
    print hex(ord(text[i+8]))
print '_____________________________'
