import time


def log(content):
    this_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
    print('[' + str(this_time) + '] ' + content)
