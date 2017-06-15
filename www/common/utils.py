import datetime
import time

def getDateStr():
    return datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")

#把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d-%H")


def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p

def text2html(text):
    lines = map(lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'), filter(lambda s: s.strip() != '', text.split('\n')))
    return ''.join(lines)