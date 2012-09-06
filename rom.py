"""
ROM parser
"""

from cap import CAP
from fd import FD
from raw import RAW


class ROM(object):
    def __init__(self, data, start=0, prefix=''):
        self.start = start
        self.prefix = prefix
        self.data = data
        self.size = len(data)
        if CAP.check_sig(data):
            self.contents = CAP(data, start, prefix + '00_')
        else:
            self.contents = FD(data, start, prefix + '00_')
        self.trailing = None
        if self.size > self.contents.size:
            self.trailing = RAW(data[self.contents.size:], start + self.contents.size, prefix + '01_')

    def __str__(self):
        return '0x%08x+0x%08x: ROM' % (self.start, self.size)

    def showinfo(self, ts='  '):
        print ts + 'Size: 0x%x' % self.size
        if self.trailing:
            print ts + 'Trailing: 0x%x' % self.trailing.size
        print ts + str(self.contents)
        self.contents.showinfo(ts + '  ')
        if self.trailing:
            print ts + str(self.trailing)
            self.trailing.showinfo(ts + '  ')

    def dump(self):
        self.contents.dump()
        if self.trailing:
            self.trailing.dump()
