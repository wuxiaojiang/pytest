#-*-coding:cp936-*-
#----------------------------------------------
#程序名：根据CPU占用率对风扇进行调速
#作 者：吴晓疆
#日 期：2015/6/6
#----------------------------------------------
import serial,time,socket,psutil,os,sys
from ctypes import *
#----------------------------------------------
def message_box(title,text):
    user32 = windll.LoadLibrary("user32.dll")
    user32.MessageBoxA(0,text,title,0)
def usart_init(baudrate,port):
    ser = serial.Serial()
    ser.baudrate = baudrate
    ser.port = port
    try:
        ser.open()
        message_box('状态','串口初始化完毕')
    except(IOError):
        message_box('串口错误','串口初始化错误，请检查串口连接情况！')
        sys.exit(0)
    return ser
#--------------------------------------------------------------------
def set_log():
    date = time.strftime('%Y-%m-%d',time.localtime())
    name = '%s.txt'%date
    path = os.getcwd()
    full_name = '%s//log//%s'%(path,name)
    d = os.listdir('%s//log'%path)
    if name in d:
        fil = open(full_name,'a+')
    else:
        fil = file(full_name,'a+')
    return fil
def insert_data(fil,data):
    fil.write(data)
    fil.close()
def load_data(data):
    fil = set_log()
    insert_data(fil,data)
#----------------------------------------------------------------------
def get_temp():
    temp = psutil.cpu_percent(1)
    return temp
def send_level(ser,old_level,temp):
    level = int(temp/10)+1
    ser.write(chr(level))
    if old_level != level:
        return level
#----------------------------------------------------------------------
class cpu_tool():
    def __init__(self):
        self.level = 1
    def no_log_model(self):
        ser = usart_init(9600,4)
        while True:
            temp = get_temp()
            t = send_level(self.level,temp)
            if t != None:
                self.level = t
    def log_model(self):
        ser = usart_init(9600,4)
        while True:
            temp = get_temp()
            t = send_level(ser,self.level,temp)
            if t != None:
                self.level = t
                ti = time.strftime("%H:%M:%S", time.localtime()) 
                data = '在%s时改变转速为%d\n'%(ti,t)
                load_data(data)
        
        
