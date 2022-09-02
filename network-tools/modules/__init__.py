import logging
import os
import time
from logging.handlers import RotatingFileHandler

from flask import Flask


def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)


def getLogHandler():
    # 日志地址
    log_dir_name = "mpt-app-logs"
    log_file_name = 'logger-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    log_file_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + os.sep + log_dir_name
    make_dir(log_file_folder)
    log_file_str = log_file_folder + os.sep + log_file_name

    logging.basicConfig(level=logging.INFO)
    file_log_handler = RotatingFileHandler(log_file_str, maxBytes=1024 * 1024, backupCount=10, encoding='UTF-8')
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
    )
    file_log_handler.setFormatter(formatter)
    file_log_handler.setLevel(logging.INFO)

    logging.getLogger('apscheduler.executors.default').setLevel(logging.WARNING)

    return file_log_handler


app = Flask(__name__)
app.url_map.strict_slashes = False
app.logger.addHandler(getLogHandler())

exception_dict = {
    "AssertionError": "断言语句（assert）失败",
    "AttributeError": "尝试访问未知的对象属性",
    "EOFError": "用户输入文件末尾标志EOF（Ctrl+d）",
    "FloatingPointError": "浮点计算错误",
    "GeneratorExit": "generator.close()方法被调用的时候",
    "ImportError": "导入模块失败的时候",
    "IndexError": "索引超出序列的范围",
    "KeyError": "字典中查找一个不存在的关键字",
    "KeyboardInterrupt": "用户输入中断键（Ctrl+c",
    "MemoryError": "内存溢出（可通过删除对象释放内存）",
    "NameError": "尝试访问一个不存在的变量",
    "NotImplementedError": "尚未实现的方法",
    "OSError": "操作系统产生的异常（例如打开一个不存在的文件）",
    "OverflowError": "数值运算超出最大限制",
    "ReferenceError": "弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象",
    "RuntimeError": "一般的运行时错误",
    "StopIteration": "迭代器没有更多的值",
    "SyntaxError": "Python的语法错误",
    "IndentationError": "缩进错误",
    "TabError": "Tab和空格混合使用",
    "SystemError": "Python编译器系统错误",
    "SystemExit": "Python编译器进程被关闭",
    "TypeError": "不同类型间的无效操作",
    "UnboundLocalError": "访问一个未初始化的本地变量（NameError的子类）",
    "UnicodeError": "Unicode相关的错误（ValueError的子类）",
    "UnicodeEncodeError": "Unicode编码时的错误（UnicodeError的子类）",
    "UnicodeDecodeError": "Unicode解码时的错误（UnicodeError的子类）",
    "UnicodeTranslateError": "Unicode转换时的错误（UnicodeError的子类）",
    "ValueError": "传入无效的参数",
    "ZeroDivisionError": "除数为零",
}