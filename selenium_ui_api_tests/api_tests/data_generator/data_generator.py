import datetime
import time


def random_name():
    date = datetime.datetime.now()
    _time = time.strftime('%H:%M:%S', time.localtime())
    print(date)
    print(_time)
    return str(f'test_user_{date.year}.{date.month}.{date.day}_{_time}')
