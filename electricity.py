import re
import requests

# 华理电费查询url
ELEC_QUERY_URL = 'https://yktyd.ecust.edu.cn/epay/wxpage/wanxiao/eleresult'
# 宿舍号
ROOM_ID = 327
# 校区 徐汇：3 奉贤：2
AREA_ID = 3
# 楼宇ID 徐汇：3-24舍对应5-26，
#           2舍：47，25舍：48，晨园：53，励志公寓：54
#     奉贤：1-4舍对应1-4，5-24舍对应27-46，25-28舍对应49-52，职工宿舍55
BUILD_ID = 7


# 推送函数
def notify(msg):
    pass


def getElec():
    "电费查询"
    headers = {"Host": "yktyd.ecust.edu.cn", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.23(0x1800172e) NetType/4G Language/zh_CN",
               "Accept-Language": "zh-CN,zh-Hans;q=0.9",
               "Cache-Control": "max-age=0"}
    params = {
        "sysid": 1,
        "roomid": ROOM_ID,
        "areaid": AREA_ID,
        "buildid": BUILD_ID
    }
    result = requests.get(ELEC_QUERY_URL, headers=headers, params=params)
    elec = re.findall('([0-9.]*)度', result.text)[0]
    if float(elec) < 20:
        notify(f'当前电费：{elec:.5}, 请充值！')


getElec()
