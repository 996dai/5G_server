from tkinter import *
import socket
import threading


class App:
    def __init__(self):
        self.app = Tk()
        self.app.title('HE客户端')
        self.frame1 = Frame(self.app)
        self.frame2 = Frame(self.app)
        self.frame3 = Frame(self.app)
        self.ent1_1 = None
        self.ent1_2 = None
        self.ent2_1 = None
        self.ent3_1 = None
        self.scrollbar_h = None
        self.udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def duo(self):
        try:
            self.udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            server_address = (self.ent1_1.get(), int(self.ent1_2.get()))  # 地址和端口
            self.udpSocket.sendto(self.ent2_1.get().encode(), server_address)  # 发送内容
            self.udpSocket.settimeout(10)
            receive_data, address = self.udpSocket.recvfrom(1024)  # 接收服务器内容
            self.ent3_1.insert('end', receive_data.decode('GBK') + '\n')  # 显示收到的数据内容
            self.udpSocket.close()
        except socket.timeout:
            self.ent3_1.insert('end', '数据接收超时' + '\n')
        except ConnectionResetError:
            self.ent3_1.insert('end', '服务器正在自动发qq，请稍等...' + '\n')

    # 超时时间设置：  https: // blog.csdn.net / zengleo / article / details / 83392691
    def date(self):
        thread_1 = threading.Thread(target=self.duo, name='t1')
        thread_1.start()

    def screen(self):
        sw = self.app.winfo_screenwidth()  # 得到屏幕宽度
        sh = self.app.winfo_screenheight()  # 得到屏幕高度

        ww, wh = 610, 400
        x, y = (sw - ww) / 2, (sh - wh) / 2
        self.app.geometry(f"%dx%d+%d+%d" % (ww - 180, wh, x + 100, y))

    def labels(self):
        Label(self.frame1, text="服务器IP:", font=('正楷', 18)).grid(column=0, row=0)
        Label(self.frame1, text="    端口:", font=('正楷', 18)).grid(column=0, row=1)
        Label(self.frame1, text='-' * 25, font=('正楷', 18)).grid(column=1, row=2)
        Label(self.frame2, text='-' * 25, font=('正楷', 18)).grid(column=0, row=1)
        Label(self.frame3, text='服务器返回来的数据', font=('正楷', 18)).grid(row=0)

    #  配置网址：https://blog.csdn.net/pythonitstream/article/details/128741032
    def entry(self):
        self.ent1_1 = Entry(self.frame1, bd=5, font=('楷体', 18), width=23)
        self.ent1_1.insert('end', '121.40.255.216')
        self.ent1_1.grid(column=1, row=0)

        self.ent1_2 = Entry(self.frame1, bd=5, font=('楷体', 18), width=23)
        self.ent1_2.insert('end', '8080')
        self.ent1_2.grid(column=1, row=1)

        self.ent2_1 = Entry(self.frame2, bd=5, font=('楷体', 18), width=25)
        self.ent2_1.insert('end', 'hk_A1,1')
        self.ent2_1.grid(column=0, row=0)

        self.ent3_1 = Text(self.frame3, bd=5, font=('楷体', 18), width=30, height=7)
        self.ent3_1.grid(row=1)

        self.scrollbar_h = Scrollbar(command=self.ent3_1.yview)
        self.scrollbar_h.pack(side=RIGHT, fill=Y)
        self.ent3_1.config(yscrollcommand=self.scrollbar_h.set)

    #  配置网址：https://blog.csdn.net/weixin_42272768/article/details/100589708
    def buttons(self):
        bt = Button(self.frame2, text='发送数据', font=('正楷', 15),
                    command=self.date,
                    activebackground='blue',
                    overrelief='sunken')
        bt.grid(column=1, row=0)

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
