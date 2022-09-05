from datetime import date, datetime
import math
from urllib.parse import uses_relative
from winreg import REG_NOTIFY_CHANGE_SECURITY
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
tody = datetime.now().strftime('%Y-%m-%d')
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_ids = os.environ["USER_ID"].split("\n")
template_id = os.environ["TEMPLATE_ID"]


def get_weather():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  weather_tomo = res['data']['list'][1]
  return weather['weather'], math.floor(weather['temp']), math.floor(weather['high']), math.floor(weather['low']), weather_tomo['weather'],math.floor(weather_tomo['high']), math.floor(weather_tomo['low'])

def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)

def get_xinguan():
  tx_url = "https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?adCode=420100&limit=1"
  res = requests.get(tx_url).json()
  print(res)
  renshu = res['data'][0]
  print(renshu)
  return renshu['yes_wzz_add'], renshu['confirm_add']



client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature, highest, lowest ,wea_tomo ,highest_tomo , lowest_tomo  = get_weather()
wzz_add , confirm_add = get_xinguan()
data = {"confirm":{"value":confirm_add,"color":get_random_color()},"wzzadd":{"value":wzz_add,"color":get_random_color()},"weather":{"value":wea,"color":get_random_color()},"temperature":{"value":temperature,"color":get_random_color()},"love_days":{"value":get_count(),"color":get_random_color()},"birthday_left":{"value":get_birthday(),"color":get_random_color()},"words":{"value":get_words(),"color":get_random_color()},"highest": {"value":highest,"color":get_random_color()},"lowest":{"value":lowest, "color":get_random_color()},"wea_tomo":{"value":wea_tomo, "color":get_random_color()},"highest_tomo":{"value":highest_tomo, "color":get_random_color()},"lowest_tomo":{"value":lowest_tomo, "color":get_random_color()},"date":{"value":tody, "color":get_random_color()}}
count = 0
for user_id in user_ids:
  res = wm.send_template(user_id, template_id, data)
  count+=1

print("发送了" + str(count) + "条消息")
