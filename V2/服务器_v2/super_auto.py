# -*- coding: gbk -*-
import datetime as t
import win32con
import win32gui
import win32clipboard as w
from time import sleep

#['D ����','������', '����', '������']
# haike_a1,0,172.168.11.12 8000
class Aaa:
    def __init__(self, s):
        self.s = s
        self.d = {}
        self.lis = ['D ����', '������', '������', '������']
        if s == '1':
            self.dat = "����"
        else:
            self.dat = "����"

    def __repr__(self):
        if self.s == '1':
            return '����'

        else:
            return '����'

    def sendmsg(self, receiver):  # �Զ�����qq��Ϣ������ΪQQ��
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, self.dat)  # �����ı�����
        w.CloseClipboard()  # �ر�

        sleep(1)
        qq = win32gui.FindWindow(None, receiver)  # Ѱ��QQ����
        win32gui.SendMessage(qq, win32con.WM_PASTE, 0, 0)
        win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    def sends(self):
        print(self.lis)
        for i in self.lis:
            print(i)
            self.sendmsg(i)  # ������������ߵı�ע��
            sleep(2)
            print('success')


if __name__ == '__main__':
    a = Aaa('1')
    a.sends()
