import binascii
fil = open('hhh.exe')

c = fil.read()
for i in range(108):
    print str(i) + '   '+hex(ord(c[2*i])*256+ord(c[2*i+1]))+'.....'+c[2*i]+c[2*i+1]
pe = ord(c[60])
print hex(ord(c[pe+1]))
