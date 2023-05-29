from tkinter import *
import socket
from super_auto import Aaa
from threading import Thread

class App:
    def __init__(self):
        self.app = Tk()
        self.app.title('HE服务端')
        self.frame1 = Frame(self.app)
        self.frame3 = Frame(self.app)
        self.ent1_1 = None
        self.ent1_2 = None
        self.ent3_1 = None
        self.scrollbar_h = None
        self.txt = None

    def duo(self):
        self.udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udpSocket.bind(('', 8080))
        recData, clientAddr = self.udpSocket.recvfrom(1024)  # 接收数据

        self.ent3_1.insert('end', recData.decode("utf-8") + '\n')  # 显示接收到的数据

        s = Aaa(str(recData.decode("utf-8")).split(',')[1])
        self.udpSocket.sendto(str(s).encode('GBK'), clientAddr)  # 发给客户端
        self.udpSocket.close()
        if str(s) != '没找到':
            print('自动发送')
            s.sends()

    def screen(self):
        sw = self.app.winfo_screenwidth()  # 得到屏幕宽度
        sh = self.app.winfo_screenheight()  # 得到屏幕高度
        ww, wh = 800, 400
        x, y = (sw - ww) / 2, (sh - wh) / 2
        self.app.geometry(f"%dx%d+%d+%d" % (ww - 180, wh, x + 100, y))

    def labels(self):
        Label(self.frame1, text="已报警的设备", font=('正楷', 18)).grid(column=0, row=0)
        Label(self.frame1, text="*"*10, font=('正楷', 18)).grid(column=0, row=1)
        Label(self.frame3, text='接收到的数据(编号,报警状态(0,1),ip)', font=('正楷', 18)).grid(column=0, row=0)

    #  配置网址：https://blog.csdn.net/pythonitstream/article/details/128741032
    def entry(self):
        self.ent1_1 = Entry(self.frame1, bd=5, font=('楷体', 18), width=23)
        self.ent1_1.grid(column=1, row=0)

        self.ent3_1 = Text(self.frame3, bd=5, font=('楷体', 18), width=50, height=10)
        self.ent3_1.grid(column=0, row=1)

        self.scrollbar_h = Scrollbar(command=self.ent3_1.yview)
        self.scrollbar_h.pack(side=RIGHT, fill=Y)
        self.ent3_1.config(yscrollcommand=self.scrollbar_h.set)

    def end(self):
        self.frame1.pack(anchor='w')
        self.frame3.pack()
        self.app.resizable(width=False, height=False)  # 可不可拉伸


    def start(self):
        t = Thread(target=self.duo, name='t')
        t.start()
        self.screen()
        self.labels()
        self.entry()
        self.end()
        self.app.mainloop()


if __name__ == '__main__':
    st = App()
    st.start()


# grid配置： https://www.cnblogs.com/ruo-li-suo-yi/p/7425307.html
