import datetime,json
from datetime import date

from apis import Page


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, Page):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, obj)