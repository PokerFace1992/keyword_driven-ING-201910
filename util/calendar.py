import time
import datetime
import locale

# 获取当前的日期
def get_current_date():
    time_tup = time.localtime()
    current_date = str(time_tup.tm_year) + "年" + \
        str(time_tup.tm_mon) + "月" + str(time_tup.tm_mday)+"日"
    return current_date

# 获取当前的时间
def get_current_time():
    time_str = datetime.datetime.now()
    locale.setlocale(locale.LC_CTYPE, 'chinese')
    now_time = time_str.strftime('%H点%M分%S秒')
    return now_time

# 获取当前的时间
def get_current_hour():
    time_str = datetime.datetime.now()
    now_hour = time_str.strftime('%H')
    return now_hour

def get_current_date_and_time():
    return get_current_date()+" "+get_current_time()

if __name__ == "__main__":
    print(get_current_date())
    print(get_current_time())
    print(get_current_hour())
    print(get_current_date_and_time())
