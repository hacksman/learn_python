#!/usr/bin/env python 
# coding:utf-8
# @Time :10/24/18 10:55

"""
    📋 --->>> 控制台输出
    🤔 --->>> 解析
    📢 --->>> 说明
    🌰 --->>> 例子

    materials:
        # python logging模块使用教程
        1. https://www.jianshu.com/p/feb86c06c4f4

        # Python之日志处理（logging模块）
        2. https://www.cnblogs.com/yyds/p/6901864.html

        # [python小记] logging模块SMTPhandler实现日志邮件报警
        3. https://blog.csdn.net/a469357594/article/details/79025234

        # logging-cookbook
        4. https://docs.python.org/3/howto/logging-cookbook.html#context-info
"""

import logging
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 1. 日志级别
# 日志级别等级：debug < info < warning < error < critical（毁灭级，软件已经不能正常工作）

# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.warn("warn message")
# logging.error("error message")
# logging.critical("critical message")

# 📋：
# >>> WARNING:root:warning message
# >>> WARNING:root:warn message
# >>> ERROR:root:error message
# >>> CRITICAL:root:critical message

# 🤔：
#   默认情况下，logging会将warning(python3已将warn弃用)级别以上的日志输出到控制台(stout)，输出格式如下
#   >>> 日志级别  :   Logger实例名称  :   消息内容
#   >>> ERROR    :      root       :   error message


# -------------------------------------------- 分割线 --------------------------------------------


# 2. 简单配置(运行此部分，需注释上部分代码)
# logging.basicConfig(filename="python_log.log", level=logging.DEBUG)
#
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")

# 📢：
#   此时当前路径下会有一个python_log.log的文件，里面如下的日志
#     INFO:root:info message
#     WARNING:root:warning message
#     ERROR:root:error message
#     CRITICAL:root:critical message
#   level设置了logging的级别为INFO，高于INFO级别的日志都会被打印出来


# -------------------------------------------- 分割线 --------------------------------------------


# 3. 核心四大组件 ———— Logger、Handler、Filter、Formatter

# 3.1 Logger

# 作用：提供了可一直使用的接口
# 两类方法: ① 配置方法 ② 消息方法
# 3.1.1 配置方法
# Logger.setLevel()         >>> 设置日志处理的最低级别
# Logger.addHandler()       >>> 为logger对象添加handler对象
# Logger.removeHandler()    >>> 为logger对象删除handler对象
# Logger.addFilter()        >>> 为logger对象添加filter对象
# Logger.removeFilter()     >>> 为logger对象删除filter对象


# 3.1.2 消息方法
# 日志方法创建之后，可通过消息方法创建日记记录

# 📢：
# Logger.info("info message")、Logger.warning()等
# 其中有两个方法较为特殊：Logger.log() 和 Logger.exception()
# Logger.log() 可以需要多传入一个level参数，自定义level时可以用到
# Logger.exception() 会输出堆栈跟踪信息，一般在错误日志后用它来打印详细错误信息

# 🌰：

# log = logging.getLogger("play")
# log.setLevel(level=logging.INFO)
#
# log.info("aaa")
# # 此时控制台不输出aaa
# log.warning("bbb")
# # 控制台输出bbb
#
# # 控制台输出
# # 若不添加StreamHandler控制台输出，则只有级别在warning以上的日志才会被输出
# stream_hander = logging.StreamHandler()
# log.addHandler(stream_hander)
# log.info("ccc")


# 3.2 Handler
# 作用：将日志发送到指定的位置
# 📢：
#   可通过addHandler()方法创建多个handler对象，比如一个程序需要实现多个日志输出
#       1. 所有日志输出至一个文件
#       2. 重大级别日志输出至控制台
#       3. 严重级别的日志发送至email
#
#   开发者需要关心的几个配置方法
#   Handler.setLevel()          >>> 设置日志处理的最低级别
#   Handler.setFormatter()      >>> 为handler设置一个格式器对象
#   Handler.addFilter()         >>> 为handler添加一个过滤器对象
#   Handler.removeFilter()      >>> 为handler删除一个过滤器对象
# Handler是一个基类，只定义了必要的接口，应该用它的子类，常见的子类有：
# logging.StreamHandler                         >>> 将日志输出至控制台
# logging.FileHandler                           >>> 将日志消息输出至文件，默认文件大小会无限增长
# logging.handlers.RotatingFileHandler          >>> 将日志消息输出至文件，并支持文件按大小分割
# logging.handlers.TimedRotatingFileHandler     >>> 将日志消息输出至文件，并支持文件按时间分割
# logging.handlers.HTTPHandler                  >>> 将日志消息以GET或POST方法发送给某HTTP服务器
# logging.handlers.SMTPHandler                  >>> 将日志消息发送给指定email
# logging.NullHandler                           >>> 该Handler实例会忽略error messages，通常被想使用logging的library
#                                                   开发者使用来避免'No handlers could be found for logger XXX'信息的出现

# 🌰：
# from logging.handlers import SMTPHandler
# log = logging.getLogger("play")
# stmp_handler = SMTPHandler(mailhost=("smtp.163.com", 25),
#                            fromaddr="your_email@163.com",
#                            toaddrs=["send_to_email@163.com"],
#                            subject="test for log",
#                            credentials=("your_email@163.com", "passwd"))
# log.addHandler(stmp_handler)
# log.setLevel(logging.DEBUG)
# log.info("info>>> massage")


# # 3.3 Filter
# # 作用：提供更细力度的过滤，决定哪些日志可以被输出
#
# # 🌰：
#
# logger = logging.getLogger('a')
#
#
# class NoParsingFilter(logging.Filter):
#     def filter(self, record):
#         return not record.getMessage().startswith('parsing')
#
#
# logger.addFilter(NoParsingFilter())
#
# logger.warning("word--parsing is not start")
# logger.warning("parsing start")
#
# # 📋：
# # >>> word--parsing is not start


# 3.4 Formatter
# 作用：决定日志最终的输出格式

# 🌰：
# log = logging.getLogger("play")
#
# log_format = logging.Formatter(fmt="🤣🤣🤣 %(asctime)s - %(filename)s - %(lineno)s - %(message)s")
#
# log_stream_handler = logging.StreamHandler()
#
# log_stream_handler.setFormatter(log_format)
#
# log.addHandler(log_stream_handler)
#
# log.setLevel(logging.DEBUG)
#
# log.info("design something")


# -------------------------------------------- 分割线 --------------------------------------------


# 实例
class AddWarnEmoji(logging.Filter):

    def filter(self, record):
        if record.levelname == "WARNING":
            record.emoji = "🙄🙄🙄"
            return True
        elif record.levelname == "ERROR":
            record.emoji = "💀💀💀"
            return True
        else:
            record.emoji = "→→→→→"
            return True


log_stream_handler = logging.StreamHandler()
log_file_handler = logging.FileHandler("python.log", encoding="utf-8")
log_stream_handler.addFilter(AddWarnEmoji())
LOG_FORMAT = "%(asctime)s - %(emoji)-3s %(levelname)-7s - %(filename)s - %(lineno)-4s - %(message)s"
log_format = logging.Formatter(fmt=LOG_FORMAT)
log_stream_handler.setFormatter(log_format)
log_file_handler.setFormatter(log_format)

logger = logging.getLogger("play")
logger.setLevel(logging.INFO)

logger.addHandler(log_stream_handler)
logger.addHandler(log_file_handler)

logger.info("你好啊")
logger.warning("真香警告...")
logger.error("真香警告...")

