#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re


def readheaders(file):
    headerDict = {}
    f = open(file,'r')
    headersText = f.read()
    headers = re.split('\n', headersText)
    for header in headers:
        result = re.split(':', header, maxsplit=1)
        headerDict[result[0]] = result[1].strip()
    f.close()
    return headerDict


if __name__ == '__main__':
    import pprint

    pprint.pprint(readheaders('http_header.txt'))