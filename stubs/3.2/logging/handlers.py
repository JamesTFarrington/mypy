# Stubs for logging.handlers (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Undefined, Any
import logging

threading = Undefined(Any)
DEFAULT_TCP_LOGGING_PORT = Undefined(Any)
DEFAULT_UDP_LOGGING_PORT = Undefined(Any)
DEFAULT_HTTP_LOGGING_PORT = Undefined(Any)
DEFAULT_SOAP_LOGGING_PORT = Undefined(Any)
SYSLOG_UDP_PORT = Undefined(Any)
SYSLOG_TCP_PORT = Undefined(Any)

class BaseRotatingHandler(logging.FileHandler):
    mode = Undefined(Any)
    encoding = Undefined(Any)
    namer = Undefined(Any)
    rotator = Undefined(Any)
    def __init__(self, filename, mode, encoding=None, delay=False): pass
    def emit(self, record): pass
    def rotation_filename(self, default_name): pass
    def rotate(self, source, dest): pass

class RotatingFileHandler(BaseRotatingHandler):
    maxBytes = Undefined(Any)
    backupCount = Undefined(Any)
    def __init__(self, filename, mode='', maxBytes=0, backupCount=0, encoding=None,
                 delay=False): pass
    stream = Undefined(Any)
    def doRollover(self): pass
    def shouldRollover(self, record): pass

class TimedRotatingFileHandler(BaseRotatingHandler):
    when = Undefined(Any)
    backupCount = Undefined(Any)
    utc = Undefined(Any)
    atTime = Undefined(Any)
    interval = Undefined(Any)
    suffix = Undefined(Any)
    extMatch = Undefined(Any)
    dayOfWeek = Undefined(Any)
    rolloverAt = Undefined(Any)
    def __init__(self, filename, when='', interval=1, backupCount=0, encoding=None, delay=False,
                 utc=False, atTime=None): pass
    def computeRollover(self, currentTime): pass
    def shouldRollover(self, record): pass
    def getFilesToDelete(self): pass
    stream = Undefined(Any)
    def doRollover(self): pass

class WatchedFileHandler(logging.FileHandler):
    def __init__(self, filename, mode='', encoding=None, delay=False): pass
    stream = Undefined(Any)
    def emit(self, record): pass

class SocketHandler(logging.Handler):
    host = Undefined(Any)
    port = Undefined(Any)
    address = Undefined(Any)
    sock = Undefined(Any)
    closeOnError = Undefined(Any)
    retryTime = Undefined(Any)
    retryStart = Undefined(Any)
    retryMax = Undefined(Any)
    retryFactor = Undefined(Any)
    def __init__(self, host, port): pass
    def makeSocket(self, timeout=1): pass
    retryPeriod = Undefined(Any)
    def createSocket(self): pass
    def send(self, s): pass
    def makePickle(self, record): pass
    def handleError(self, record): pass
    def emit(self, record): pass
    def close(self): pass

class DatagramHandler(SocketHandler):
    closeOnError = Undefined(Any)
    def __init__(self, host, port): pass
    def makeSocket(self, timeout=1): pass # TODO: Actually does not have the timeout argument.
    def send(self, s): pass

class SysLogHandler(logging.Handler):
    LOG_EMERG = Undefined(Any)
    LOG_ALERT = Undefined(Any)
    LOG_CRIT = Undefined(Any)
    LOG_ERR = Undefined(Any)
    LOG_WARNING = Undefined(Any)
    LOG_NOTICE = Undefined(Any)
    LOG_INFO = Undefined(Any)
    LOG_DEBUG = Undefined(Any)
    LOG_KERN = Undefined(Any)
    LOG_USER = Undefined(Any)
    LOG_MAIL = Undefined(Any)
    LOG_DAEMON = Undefined(Any)
    LOG_AUTH = Undefined(Any)
    LOG_SYSLOG = Undefined(Any)
    LOG_LPR = Undefined(Any)
    LOG_NEWS = Undefined(Any)
    LOG_UUCP = Undefined(Any)
    LOG_CRON = Undefined(Any)
    LOG_AUTHPRIV = Undefined(Any)
    LOG_FTP = Undefined(Any)
    LOG_LOCAL0 = Undefined(Any)
    LOG_LOCAL1 = Undefined(Any)
    LOG_LOCAL2 = Undefined(Any)
    LOG_LOCAL3 = Undefined(Any)
    LOG_LOCAL4 = Undefined(Any)
    LOG_LOCAL5 = Undefined(Any)
    LOG_LOCAL6 = Undefined(Any)
    LOG_LOCAL7 = Undefined(Any)
    priority_names = Undefined(Any)
    facility_names = Undefined(Any)
    priority_map = Undefined(Any)
    address = Undefined(Any)
    facility = Undefined(Any)
    socktype = Undefined(Any)
    unixsocket = Undefined(Any)
    socket = Undefined(Any)
    formatter = Undefined(Any)
    def __init__(self, address=Undefined, facility=Undefined, socktype=None): pass
    def encodePriority(self, facility, priority): pass
    def close(self): pass
    def mapPriority(self, levelName): pass
    ident = Undefined(Any)
    append_nul = Undefined(Any)
    def emit(self, record): pass

class SMTPHandler(logging.Handler):
    username = Undefined(Any)
    fromaddr = Undefined(Any)
    toaddrs = Undefined(Any)
    subject = Undefined(Any)
    secure = Undefined(Any)
    timeout = Undefined(Any)
    def __init__(self, mailhost, fromaddr, toaddrs, subject, credentials=None, secure=None,
                 timeout=0.0): pass
    def getSubject(self, record): pass
    def emit(self, record): pass

class NTEventLogHandler(logging.Handler):
    appname = Undefined(Any)
    dllname = Undefined(Any)
    logtype = Undefined(Any)
    deftype = Undefined(Any)
    typemap = Undefined(Any)
    def __init__(self, appname, dllname=None, logtype=''): pass
    def getMessageID(self, record): pass
    def getEventCategory(self, record): pass
    def getEventType(self, record): pass
    def emit(self, record): pass
    def close(self): pass

class HTTPHandler(logging.Handler):
    host = Undefined(Any)
    url = Undefined(Any)
    method = Undefined(Any)
    secure = Undefined(Any)
    credentials = Undefined(Any)
    def __init__(self, host, url, method='', secure=False, credentials=None): pass
    def mapLogRecord(self, record): pass
    def emit(self, record): pass

class BufferingHandler(logging.Handler):
    capacity = Undefined(Any)
    buffer = Undefined(Any)
    def __init__(self, capacity): pass
    def shouldFlush(self, record): pass
    def emit(self, record): pass
    def flush(self): pass
    def close(self): pass

class MemoryHandler(BufferingHandler):
    flushLevel = Undefined(Any)
    target = Undefined(Any)
    def __init__(self, capacity, flushLevel=Undefined, target=None): pass
    def shouldFlush(self, record): pass
    def setTarget(self, target): pass
    buffer = Undefined(Any)
    def flush(self): pass
    def close(self): pass

class QueueHandler(logging.Handler):
    queue = Undefined(Any)
    def __init__(self, queue): pass
    def enqueue(self, record): pass
    def prepare(self, record): pass
    def emit(self, record): pass

class QueueListener:
    queue = Undefined(Any)
    handlers = Undefined(Any)
    def __init__(self, queue, *handlers): pass
    def dequeue(self, block): pass
    def start(self): pass
    def prepare(self, record): pass
    def handle(self, record): pass
    def enqueue_sentinel(self): pass
    def stop(self): pass
