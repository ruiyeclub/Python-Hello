# 微博的cookie登录 通过cookie绕过登录

import urllib.request

url = 'https://weibo.com/manage/dataservice'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': 'SINAGLOBAL=7433510253858.066.1626400475254; Hm_lvt_53d4fa5bbf46e49e62d85aef95382029=1637997183; UOR=,,www.baidu.com; XSRF-TOKEN=OHJpaJiZlES6EiIvBrjXBCKs; SCF=AkcGP-eHy2XC3cPXqiQW8ncUYfzerljsGvmxVD1bfkU--ZUyu0YxugLCOIhDvAfLBHFzra7iO1OPhBlwcSiYAVo.; login_sid_t=8459edd3b7546d17d9dc3f417c3a73e3; cross_origin_proto=SSL; _s_tentry=weibo.com; Apache=3982063068339.9473.1645606984052; ULV=1645606984056:7:1:1:3982063068339.9473.1645606984052:1641803798355; wb_view_log=1920*10801; appkey=; WBtopGlobal_register_version=2022022317; SUB=_2A25PEYi8DeRhGeBN7lcZ8ibEwzyIHXVsZv10rDV8PUNbmtB-LUn9kW9NREnY51XIY7B0D2vyGZl1rhCmfl8Nx9pp; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFNS1PFq8qin4NbojMbb5x75JpX5KzhUgL.Foq0SK-ReonR1h52dJLoIpRLxK.L1K.L1hnLxK-L1K5L12eLxK-LB-BLBK9CqP.t; ALF=1677143147; SSOLoginState=1645607148; WBPSESS=Dt2hbAUaXfkVprjyrAZT_OhEIOnkaRC33aQpmzSeK8ihrtDV3-OQ2lX09TrBFomCBk2UG6YW88I-8B6L0pHZ86lkWNmMnWzSG7ZNdSgJqRcyQRezV5euycuh5En5j4dziJU2NZ-HGuJOGFoDRJeDQsM6WIcx7kA9JXK-8ntYQ85-ihK-WlmU0h79VksgxZDoqbf-Murc_cAy_vieG8U_Dw==',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
