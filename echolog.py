# 日志输出系统
import os
import time

class echo_log_info:
    def __init__(self,log):
        print("["+ time.asctime() +"]"+"[INFO]" + log)

class echo_log_error:
    def __init__(self,log):
        print("["+ time.asctime() +"]"+"[ERROR]" + log)