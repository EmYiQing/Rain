from common.log import log
from plugin.activemq import get_plugin_info
import os

def processing_input(command):
    if command == "help":
        print("帮助信息：")
        print("扫描目标" + " " * 20 + "scan [ip]:[port] [CVE完整编号]")
        print("漏洞详情" + " " * 20 + "detail [CVE完整编号]")
        print("漏洞库" + " " * 22 + "show cve")
        print("扫描列表和扫描ID" + " " * 12 + "list")
        print("导出扫描报告：" + " " * 14 + "export [扫描ID]")
        print("退出系统" + " " * 20 + "exit")
        print("\n示例：")
        print("scan 10.14.4.240:8080 CVE-2015-5254\n")
    elif command.startswith("scan"):
        ip = command.split(" ")[1].split(":")[0].strip()
        port = command.split(" ")[1].split(":")[1].split("CVE")[0].strip()
        cve = command.split(" ")[-1].strip()
        log("搜索CVE中......")
    elif command == "show cve":
        s = open("cve")
        for a in s.readlines():
            print(a, end="")
    elif command == "scanlist":
        log("scanlist")
    elif command.startswith("detail"):
        cve = str(command).split(" ")[1]
        if cve=="CVE-2015-1830":
            data = get_plugin_info()
            print(data["name"])
            print(data["info"])
            print(data["level"])
            print(data["type"])
    elif command.startswith("export"):
        log("export")
    elif command == "exit":
        log("退出系统")
        exit(0)
    elif command == "":
        return
    else:
        print(os.popen(command).read())
