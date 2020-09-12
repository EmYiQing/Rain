import os
import sys

try:
    base_path = os.path.abspath('.')
    sys.path.append(base_path)
    sys.path.append(base_path + os.sep + 'report')
    sys.path.append(base_path + os.sep + 'common')
    sys.path.append(base_path + os.sep + 'plugin')
except Exception as e:
    print(e)

from common.log import log
from common.input import processing_input

if __name__ == '__main__':
    print("----------------小迪群内部专用漏洞扫描平台----------------")
    log("欢迎来到漏洞扫描系统")
    while True:
        try:
            print("xushao > ", end="")
            command = input()
            processing_input(command)
        except Exception as e:
            print(e)
            log("系统异常!")
            continue
