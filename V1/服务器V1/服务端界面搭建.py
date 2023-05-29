from tkinter import *
import socket
from super_auto import Aaa
from threading import Thread


class App:
    def __init__(self):
        self.app = Tk()
        self.app.title('HE服务器端')
        self.frame1 = Frame(self.app)
        self.frame2 = Frame(self.app)

        self.frame3 = Frame(self.app)
        self.ent1_1 = None
        self.ent1_2 = None
        self.ent2_1 = None
        self.ent3_1 = None
        self.ent3_2 = None
        self.scrollbar_h = None
        self.key = 1
        self.txt = None
        self.str_obj = StringVar(self.frame2)

    def duo(self):
        try:
            while self.key:
                self.udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.udpSocket.bind(('', 8080))
                self.udpSocket.settimeout(100)
                recData, clientAddr = self.udpSocket.recvfrom(1024)  # 接收数据
                self.ent1_1.select_clear()
                self.ent1_1.insert('end', clientAddr)  # 显示客户端ip
                self.ent3_1.insert('end', recData.decode("utf-8") + '\n')  # 接收到的数据

                s = Aaa(str(recData.decode("utf-8")))
                self.ent3_2.insert('end', str(s) + '\n')  # 要发送的数据

                self.udpSocket.sendto(str(s).encode('GBK'), clientAddr)  # 发给客户端
                self.udpSocket.close()
                if str(s) != '没找到':
                    s.sends()
        except socket.timeout:
            self.ent3_1.insert('end', '数据接收超时' + '\n')

    def date(self):
        if self.key:
            cv = Canvas(self.frame2, width=70, height=65)
            cv.grid(column=2, row=0)
            cv.create_rectangle(20, 20, 50, 50, fill="red", outline='red')
            self.str_obj.set("未开启")
            self.key = 0
        else:
            cv = Canvas(self.frame2, width=70, height=65)
            cv.grid(column=2, row=0)
            cv.create_rectangle(20, 20, 50, 50, fill="green", outline='green')
            self.str_obj.set("已开启")
            self.key = 1

            t = Thread(target=self.duo, name='t')
            t.start()

    def screen(self):
        sw = self.app.winfo_screenwidth()  # 得到屏幕宽度
        sh = self.app.winfo_screenheight()  # 得到屏幕高度

        ww, wh = 610, 400
        x, y = (sw - ww) / 2, (sh - wh) / 2
        self.app.geometry(f"%dx%d+%d+%d" % (ww - 180, wh, x + 100, y))

    def labels(self):
        Label(self.frame1, text="客户端IP:", font=('正楷', 18)).grid(column=0, row=0)
        Label(self.frame1, text="    端口:", font=('正楷', 18)).grid(column=0, row=1)
        Label(self.frame1, text='-' * 25, font=('正楷', 18)).grid(column=1, row=2)
        Label(self.frame2, text='服务器状态:', font=('正楷', 18)).grid(column=0, row=0)
        Label(self.frame3, text='接收到的数据', font=('正楷', 18)).grid(column=0, row=0)
        Label(self.frame3, text='返给客户端的数据', font=('正楷', 18)).grid(column=1, row=0)

        self.str_obj.set("未开启")
        self.txt = Label(self.frame2, textvariable=self.str_obj, font=('正楷', 18))

        cv = Canvas(self.frame2, width=70, height=65)
        cv.grid(column=2, row=0)
        cv.create_rectangle(20, 20, 50, 50, fill="red", outline='red')

    #  配置网址：https://blog.csdn.net/pythonitstream/article/details/128741032
    def entry(self):
        self.ent1_1 = Entry(self.frame1, bd=5, font=('楷体', 18), width=23)
        self.ent1_1.grid(column=1, row=0)

        self.ent1_2 = Entry(self.frame1, bd=5, font=('楷体', 18), width=23)
        self.ent1_2.insert('end', '8080')
        self.ent1_2.grid(column=1, row=1)

        self.ent3_1 = Text(self.frame3, bd=5, font=('楷体', 13), width=21, height=10)
        self.ent3_1.grid(column=0, row=1)

        self.ent3_2 = Text(self.frame3, bd=5, font=('楷体', 13), width=21, height=10)
        self.ent3_2.grid(column=1, row=1)

        self.scrollbar_h = Scrollbar(command=self.ent3_1.yview)
        self.scrollbar_h.pack(side=RIGHT, fill=Y)
        self.ent3_1.config(yscrollcommand=self.scrollbar_h.set)

    #  配置网址：https://blog.csdn.net/weixin_42272768/article/details/100589708
    def buttons(self):
        bt = Button(self.frame2, text='开关按钮', font=('正楷', 15), command=self.date, activebackground='blue',
                    overrelief='sunken')
        bt.grid(column=3, row=0)

    def end(self):
        self.frame1.pack(anchor='w')
        self.frame2.pack(anchor='w')
        self.frame3.pack()
        self.app.resizable(width=False, height=False)  # 可不可拉伸

    def start(self):
        self.screen()
        self.labels()
        self.entry()
        self.buttons()
        self.end()
        self.app.mainloop()


if __name__ == '__main__':
    st = App()
    st.start()

# grid配置： https://www.cnblogs.com/ruo-li-suo-yi/p/7425307.html
