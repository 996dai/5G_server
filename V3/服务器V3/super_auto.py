# -*- coding: gbk -*-
import datetime as t
import win32con
import win32gui
import win32clipboard as w
from time import sleep

#['D 七娃','鲍蒙蒙', '何亮', '代畅成']
# haike_a1,0,172.168.11.12 8000
class Aaa:
    def __init__(self, s, name):
        self.s = s
        self.name = name
        self.d = {}
        self.lis = ['D 七娃', '鲍蒙蒙', '杨天涛', '代畅成', '冯硕', '洪科杰', '何亮']
        self.dat = None

    def __repr__(self):
        if self.s == '1':
            self.dat = '设备' + self.name + '发起报警'
            return '已收到设备警报'
        elif self.s == '0':
            return '设备正常'
        else:
            return '请输入正确的状态码'

    def sendmsg(self, receiver):  # 自动发送qq消息，参数为QQ名
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, self.dat)  # 复制文本内容
        w.CloseClipboard()  # 关闭

        sleep(0.5)
        qq = win32gui.FindWindow(None, receiver)  # 寻找QQ窗口
        win32gui.SendMessage(qq, win32con.WM_PASTE, 0, 0)
        win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    def sends(self):
        for i in self.lis:
            print(i)
            self.sendmsg(i)  # 这里填入接收者的备注名
            sleep(0.5)

    # def logs(self):

if __name__ == '__main__':
    a = Aaa('1')
    a.sends()
