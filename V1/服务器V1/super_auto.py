# -*- coding: gbk -*-
import datetime as t
import win32con
import win32gui
import win32clipboard as w
from time import sleep


class Aaa:
    def __init__(self, s):
        self.s = s
        self.d = {}
        self.lis = ['D ����', 'san', '������']
        with open('data.txt', 'r', encoding='utf-8') as f:
            f1 = f.readlines()
            for i in f1:
                s = i.split(':')
                self.d[s[0]] = s[1].strip()

    def sendmsg(self, receiver):  # �Զ�����qq��Ϣ������ΪQQ��
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, self.s)  # �����ı�����
        w.CloseClipboard()  # �ر�

        sleep(1)
        qq = win32gui.FindWindow(None, receiver)  # Ѱ��QQ����
        win32gui.SendMessage(qq, win32con.WM_PASTE, 0, 0)
        win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    def sends(self):
        for i in self.lis:
            self.sendmsg(i)  # ������������ߵı�ע��
            sleep(2)
            print('success')

    def __repr__(self):
        if self.s in self.d:
            times = str(t.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

            with open('logs.txt', 'r+', encoding='GBK') as f:
                s = f.read()
                f.seek(0)
                f.write(f'{self.s}     {times}\n' + s)

            return f'{str(self.d[self.s])}    {times.split(" ")[1]}'
        else:
            return 'û�ҵ�'


if __name__ == '__main__':
    print()

