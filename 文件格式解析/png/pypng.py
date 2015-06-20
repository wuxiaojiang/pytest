import sys,binascii
class png_tool():
    def __init__(self):
        self.text = ''
    def load(self,path):
        try:
            fil = open(path,'rb+')
        except(IOError):
            pass
        text = fil.read()
        self.text = text
    def cheak_header(self):
        text = self.text
        h = text[0:8]
        h = binascii.hexlify(h)
        header = '%s%s'%('0x',h)
        print '[*]The header is %s'%header
        if header == '0x89504e470d0a1a0a':
            print '[*]This is png file'
        else:
            print '[*]This is not png file!'
            sys.exit(0)
    def IHDR_chunk(self):
        text = self.text
        print '[*]+-------------------+-----------+'
        print '[*]|          IHDR_chunk           |'
        print '[*]+-------------------+-----------+'
        length = hex(ord(text[8])*256*256*256+ord(text[9])*256*256+ord(text[10])*256+ord(text[11]))
        num = 10-len(length)
        space = ' '*num
        print '[*]|length_of_IHDR     | %s%s|'%(space,length)
        symbol = hex(ord(text[12])*256*256*256+ord(text[13])*256*256+ord(text[14])*256+ord(text[15]))
        num = 10-len(symbol)
        space = ' '*num
        print '[*]|symbol_of_IHDR     | %s%s|'%(space,symbol)
        width = hex(ord(text[16])*256*256*256+ord(text[17])*256*256+ord(text[18])*256+ord(text[19]))
        num = 10-len(width)
        space = ' '*num
        print '[*]|width              | %s%s|'%(space,width)
        height = hex(ord(text[20])*256*256*256+ord(text[21])*256*256+ord(text[22])*256+ord(text[23]))
        num = 10-len(height)
        space = ' '*num
        print '[*]|height             | %s%s|'%(space,height)
        bit_depth = hex(ord(text[24]))
        num = 10-len(bit_depth)
        space = ' '*num
        print '[*]|bit_depth          | %s%s|'%(space,bit_depth)
        color_type = hex(ord(text[25]))
        num = 10-len(color_type)
        space = ' '*num
        print '[*]|color_type         | %s%s|'%(space,color_type)
        c_p = hex(ord(text[26]))
        num = 10-len(c_p)
        space = ' '*num
        print '[*]|compression method | %s%s|'%(space,c_p)
        f_m = hex(ord(text[27]))
        num = 10-len(f_m)
        space = ' '*num
        print '[*]|filter method      | %s%s|'%(space,f_m)
        i_m = hex(ord(text[28]))
        num = 10-len(i_m)
        space = ' '*num
        print '[*]|interlace method   | %s%s|'%(space,i_m)
        crc = hex(ord(text[29])*256*256*256+ord(text[30])*256*256+ord(text[31])*256+ord(text[32]))
        num = 10-len(crc)
        space = ' '*num
        print '[*]|CRC                | %s%s|'%(space,crc)
        print '[*]+-------------------+-----------+'
        
