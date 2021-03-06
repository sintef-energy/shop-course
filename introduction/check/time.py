import pandas as pd

from check.check_button import *

def check1(shop):
    def check(shop):
        time_res = shop.get_time_resolution()
        if time_res['starttime'] + pd.Timedelta(days=2) == time_res['endtime']:
            return True, ''
        else:
            return False, 'Wrong end time'
    generate_button(shop, check)

def check2(shop):
    def check(shop):
        time_res = shop.get_time_resolution()
        if time_res['timeunit'] != 'minute':
            return False, 'Time unit should be minute'
        elif time_res['timeresolution'][time_res['starttime']] != 15:
            return False, 'Timeresolution has not been set correctly'
        else:
            return True, ''
    generate_button(shop, check)