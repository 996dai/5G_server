# -*- coding: gbk -*-
import datetime as t
import win32con
import win32gui
import win32clipboard as w
from time import sleep

#['D ����','������', '����', '������']
# haike_a1,0,172.168.11.12 8000
class Aaa:
    def __init__(self, s, name):
        self.s = s
        self.name = name
        self.d = {}
        self.lis = ['D ����', '������', '������', '������', '��˶', '��ƽ�', '����']
        self.dat = None

    def __repr__(self):
        if self.s == '1':
            self.dat = '�豸' + self.name + '���𱨾�'
            return '���յ��豸����'
        elif self.s == '0':
            return '�豸����'
        else:
            return '��������ȷ��״̬��'

    def sendmsg(self, receiver):  # �Զ�����qq��Ϣ������ΪQQ��
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, self.dat)  # �����ı�����
        w.CloseClipboard()  # �ر�

        sleep(0.5)
        qq = win32gui.FindWindow(None, receiver)  # Ѱ��QQ����
        win32gui.SendMessage(qq, win32con.WM_PASTE, 0, 0)
        win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    def sends(self):
        for i in self.lis:
            print(i)
            self.sendmsg(i)  # ������������ߵı�ע��
            sleep(0.5)

    # def logs(self):

if __name__ == '__main__':
    a = Aaa('1')
    a.sends()
