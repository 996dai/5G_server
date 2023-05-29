# -*- coding: gbk -*-
import datetime as t
import win32con
import win32gui
import win32clipboard as w
from time import sleep

#['D 七娃','鲍蒙蒙', '何亮', '代畅成']
# haike_a1,0,172.168.11.12 8000
class Aaa:
    def __init__(self, s):
        self.s = s
        self.d = {}
        self.lis = ['D 七娃', '鲍蒙蒙', '杨天涛', '代畅成']
        if s == '1':
            self.dat = "警报"
        else:
            self.dat = "正常"

    def __repr__(self):
        if self.s == '1':
            return '警报'

        else:
            return '正常'

    def sendmsg(self, receiver):  # 自动发送qq消息，参数为QQ名
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, self.dat)  # 复制文本内容
        w.CloseClipboard()  # 关闭

        sleep(1)
        qq = win32gui.FindWindow(None, receiver)  # 寻找QQ窗口
        win32gui.SendMessage(qq, win32con.WM_PASTE, 0, 0)
        win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    def sends(self):
        print(self.lis)
        for i in self.lis:
            print(i)
            self.sendmsg(i)  # 这里填入接收者的备注名
            sleep(2)
            print('success')


if __name__ == '__main__':
    a = Aaa('1')
    a.sends()
