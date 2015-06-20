import sys
class pe_tool():
    def __init__(self):
        self.pe=''
        self.text = ''
    def open_exe(self,path):
        fil = open(path)
        text = fil.read()
        self.text = text
        mz = '%s%s'%(text[0],text[1])
        if mz == 'MZ':
            pass
        else:
            print '[*]MZ error,It is not PE file!'
            sys.exit(0)
        pe = ord(text[60])
        self.pe = pe-1
        print '[*]PE addr is %s'%str(hex(pe))
    def get_more(self):
        text = self.text
        pe = self.pe
        if text[pe]+text[pe+1] == 'PE':
            pass
        else:
            print '[*]Error PE addr!'
            sys.exit(0)
        machine = hex(ord(text[pe+5])*256+ord(text[pe+4]))
        print '[*]machine : %s'%machine
        number_of_section = hex(ord(text[pe+7])*256+ord(text[pe+6]))
        print '[*]number_of_section : %s'%number_of_section
        size_of_optional_header = ord(text[pe+20])
        print '[*]size_of_optional_section : %s'%str(size_of_optional_header)
        version = '%d.%d'%(ord(text[pe+26]),ord(text[pe+27]))
        print '[*]version : %s'%version
        size_of_code = hex(ord(text[pe+31])*65536*256+ord(text[pe+30])*65536+ord(text[pe+29])*256+ord(text[pe+28]))
        print '[*]size_of_code : %s'%size_of_code
        RVA = hex(ord(text[pe+43])*65536*256+ord(text[pe+42])*65536+ord(text[pe+41])*256+ord(text[pe+40]))
        print '[*]address_of_entry_point : %s'%RVA
        base_of_code = hex(ord(text[pe+47])*65536*256+ord(text[pe+46])*65536+ord(text[pe+45])*256+ord(text[pe+44]))
        print '[*]base_of_code : %s'%base_of_code
        base_of_data = hex(ord(text[pe+51])*65536*256+ord(text[pe+50])*65536+ord(text[pe+49])*256+ord(text[pe+48]))
        print '[*]base_of_data : %s'%base_of_data
        image_base = hex(ord(text[pe+55])*65536*256+ord(text[pe+54])*65536+ord(text[pe+53])*256+ord(text[pe+52]))
        print '[*]image_base : %s'%image_base
        

