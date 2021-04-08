import requests
import json
import time
import sys
from datetime import datetime, timedelta, timezone

def getTimeStr():
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    return bj_dt.strftime("%Y-%m-%d %H:%M:%S")


def log(content):
    print(getTimeStr() + ' ' + str(content))
    sys.stdout.flush()

#本期大学习打卡
def newXuexi(id):
    url = "http://dxx.hngqt.org.cn/study/studyAdd"
    payload={'projectId': str(id)}
    headers = {
    'Cookie': 'UM_distinctid=178aba03bc71-093fe673e653fc-43066a60-1fa400-178aba03bc81e0; JSESSIONID=AEE6DBBC4CB1AF273C8EBB8E1FC934BF; sessionid=2EEE8714E58035262EFDAB0ABAE2BDE8; CNZZDATA1260977729=47853971-1617786938-%7C1617786938'
    }
    response = requests.post(url, headers=headers, data=payload)
    j = json.loads(response.content)
    if j['success'] == True:
        log('{0}打卡成功'.format(id))
    else:
        log('{0}打卡失败'.format(id))

#往期大学习打卡
def xuexi(id):
    url = "http://dxx.hngqt.org.cn/historystudy/studyHistoryAdd"
    payload={'projectId': str(id)}
    headers = {
    'Cookie': 'UM_distinctid=178aba03bc71-093fe673e653fc-43066a60-1fa400-178aba03bc81e0; JSESSIONID=AEE6DBBC4CB1AF273C8EBB8E1FC934BF; sessionid=2EEE8714E58035262EFDAB0ABAE2BDE8; CNZZDATA1260977729=47853971-1617786938-%7C1617786938'
    }
    response = requests.post(url, headers=headers, data=payload)
    j = json.loads(response.content)
    if j['success'] == True:
        print('{0}打卡成功'.format(id))
    else:
        print('{0}打卡失败'.format(id))

if __name__ == '__main__':
    for i in range(50,74):
        #print(i)
        xuexi(i)
        time.sleep(1)
        