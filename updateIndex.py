#!/bin/sh python
# -*- coding: UTF-8 -*-
import os
import time


def fmtTime(ts):
    timestruct = time.localtime(ts)
    return time.strftime('%Y-%m-%d', timestruct)


if __name__ == '__main__':
    files = os.listdir('./')
    files.sort()
    fs = open('index.md', 'w')
    fs.write('''---
layout: default
---

###List:
''')
    for file in files:
        if os.path.isfile(file) \
                and file.endswith('.md') \
                and file != 'index.md' \
                and file != 'sample.md':
            print(file)

            fs.write('- [%s](%s) %s ~ %s\n' % (file,
                     file, fmtTime(os.path.getctime(file)), fmtTime(os.path.getmtime(file))))

    fs.close()
