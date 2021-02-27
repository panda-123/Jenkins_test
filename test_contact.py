# coding=UTF-8
# 作者:herui
# 时间:2021/1/28 20:50
# 功能: 接口测试


import requests
def test_req():
    # 获取access_token的值
    ID = 'ww9db5398ae0670287'
    SECRET = 'rjGnaO2DrF-dUVycJOd7QzoikdKKXzBVG8vUi8lSNSk'
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}')
    access_token = res.json()['access_token']
    print(res.json(),'\n', access_token)
    print(1111111111111111111111111111111111111111)