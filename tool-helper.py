import time
import os
import smtplib as root
import requests
import mechanize
import gmail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import subprocess
from colorama import Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import urllib
import random
subprocess.call("cls",shell=True)
name = ""
menu = 1
io = 1
see = 1
i = 1

print("version - 1.0(Created Terror696)\n"+Fore.GREEN+"GitHub: https://github.com/Terror696\n[!] Я вам помогу выполнить ваши задачи быстрея\n"+Fore.MAGENTA+"[!] Мой киви (номер не мой!)'+380636010596'\n"+Fore.WHITE)

while menu == 1:
    print(Fore.GREEN + "[-] Меню управления!\n"+Fore.YELLOW+"[1]: Вход на сайт через прокси!\n[2]: Генератор почты!\n[3]: Отправить письмо на почту!\n[4]: Найти по NickNames!\n[5]: Узнать все ссылки на странице!\n[6]: Узнать id и стоимость инвентаря Steam!\n[0]: Выход"+Fore.WHITE)
    menu = 0
    write = input(Fore.MAGENTA + "Введите номер раздела: " + Fore.WHITE)
    if write == "1":
        subprocess.call("cls",shell=True)
        print(Fore.GREEN + "[?] Введите ссылку на сайт пример'http://example.com'" + Fore.WHITE)
        link = input(Fore.MAGENTA + "Link: " + Fore.WHITE)
        print(Fore.GREEN + "[?] Введите теперь прокси пример '105.27.238.161:80'" + Fore.WHITE)
        proxy = input(Fore.MAGENTA + "Proxy: " + Fore.WHITE)
        print(Fore.GREEN + "[!] Ожидайте запуска браузера!" + Fore.WHITE)
        prox = Proxy()
        prox.proxy_type = ProxyType.MANUAL
        prox.http_proxy = proxy
        prox.ssl_proxy = proxy
        capabilities = webdriver.DesiredCapabilities.CHROME
        prox.add_to_capabilities(capabilities)
        driver = webdriver.Chrome(desired_capabilities=capabilities)
        driver.get(link)
        input()
        menu = 1
    elif write == "2":
        subprocess.call("cls",shell=True)
        print(Fore.GREEN+"Генератор почты начел работу!\n\n\n"+Fore.WHITE)
        link = "http://www.yopmail.com"

        str3 = ''.join([random.choice(list('qwertyuiopasdfghjklzxcvbnm')) for x in range(6)])
        str4 = ''.join([random.choice(list('QWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(1)])
        name_generator = str4 + str3
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent','Enge')]
        br.open(link)
        br.select_form(nr=0)
        br.form["login"] = name_generator       #Имя
        sub = br.submit()
        f = br.geturl()
        print(Fore.YELLOW+"Cайт почты:" + Fore.GREEN+"http://www.yopmail.com\n"+Fore.WHITE)
        print(Fore.YELLOW+"Почта: "+ Fore.GREEN + name_generator + "@yopmail.com\n"+Fore.WHITE)
        input()
        menu = 1
    elif write == "3":
        subprocess.call("cls",shell=True)
        def send_mail():
            login = input(Fore.MAGENTA + "[?] Введите вашу почту: " + Fore.WHITE)
            password = input(Fore.MAGENTA + "[?] Введите пароль от почты: " + Fore.WHITE)
            url = input(Fore.MAGENTA + "[?] Введите smtp вашей почты: " + Fore.WHITE)
            toaddr = input(Fore.MAGENTA + "[?] Введите почту на которою хотите отправить письмо: " + Fore.WHITE)
            topic = input(Fore.MAGENTA + "[?] Введите заголовок письма: " + Fore.WHITE)
            message = input(Fore.MAGENTA + "[?] Введите сообщения письма: " + Fore.WHITE)
            num = int(input(Fore.MAGENTA + "[?] Ввелите количество потоков: " + Fore.WHITE))
            spam = topic
            for value in range(num):
                str1 = ''.join([random.choice(list('123467890')) for x in range(10)])
                topic = spam +"%" +str1+"%"
                msg = MIMEMultipart()

                msg[ 'Subject' ] = topic
                msg[ 'From' ] = login
                body = message
                msg.attach(MIMEText(body,'plain'))

                server = root.SMTP_SSL( url, 465)
                server.login(login, password)
                server.sendmail(login,toaddr,msg.as_string())

        def main():
            send_mail()

        if __name__ == '__main__':
            main()
        print(Fore.GREEN+"[!] Все сообщения были отправлены!\nСпасибо что выбрали мой код;)"+Fore.WHITE)
        menu = 1
    elif write == "4":
        subprocess.call("cls",shell=True)
        print(Fore.GREEN+"[?] Извените за малое количество сайтов когда будет обновления скрипта будет больше сайтов!"+Fore.WHITE)
        check = input(Fore.MAGENTA + "Введите username: "+Fore.WHITE)
        HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56'
        }
        URL = 'https://www.instagram.com/' + check
        responce = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(responce.content, 'html.parser')
        ins = responce.status_code
        if ins == 200:
            print("Instagram: " + URL + "\n")
        else:
            print("Instagram: No user\n")
        URL = 'https://github.com/' + check
        responce = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(responce.content, 'html.parser')
        ins = responce.status_code
        if ins == 200:
            print("GitHub: " + URL + "\n")
        else:
            print("GitHub: No user\n")
        URL = 'https://api.twitch.tv/api/channels/'+check+'/access_token?oauth_token=fa0dch8f9hejkkx47om8i1jmvh25qp&need_https=true&platform=_&player_backend=mediaplayer'
        responce = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(responce.content, 'html.parser')
        ins = responce.status_code
        if ins == 200:
            print("Twitch: " + "https://www.twitch.tv/" + check + "\n")
        else:
            print("Twitch: No user\n")
        URL = 'https://nl.pinterest.com/' + check
        responce = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(responce.content, 'html.parser')
        ins = responce.status_code
        if ins == 200:
            print("Pinterest: " + URL + "\n")
        else:
            print("Pinterest: No user\n")
        URL = 'https://www.flickr.com/photos/' + check
        responce = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(responce.content, 'html.parser')
        ins = responce.status_code
        if ins == 200:
            print("Flickr: " + URL + "\n")
        else:
            print("Flickr: No user\n")
        URL = 'https://www.tiktok.com/@' + check
        responce = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(responce.content, 'html.parser')
        try:
            for link in soup.find_all('div',class_='jsx-1138300191 error-container'):
                abs = link.find('p',class_='jsx-1138300191 not-found-desc').get_text()
            if abs == "Couldn't find this page":
                print("TikTok: No user\n")
            else:
                print("TikTok: " + URL + "\n")
        except:
            print("")
        menu = 1




    elif write == "5":
        subprocess.call("cls",shell=True)
        print(Fore.GREEN + "[?] Пример https://facebook.com" + Fore.WHITE)
        ur = input(Fore.MAGENTA + "Введите ссылку страницу: " + Fore.WHITE)
        URL = ur
        HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56'
        }

        responce = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(responce.content, 'html.parser')
        for link in soup.find_all('a'):
            print(link.get('href'))
        menu = 1
    elif write == "6":
        subprocess.call("cls",shell=True)
        print("===============")
        print(Fore.BLUE + "S.T.E.A.M" + Fore.WHITE)
        print("===============")
        print(Fore.GREEN + "\n[?] Введите ссылку на профиль!" + Fore.WHITE)
        stm = input(Fore.MAGENTA + "Введите id профиля: " + Fore.WHITE)
        subprocess.call("cls",shell=True)
        print("===============")
        print(Fore.BLUE + "S.T.E.A.M" + Fore.WHITE)
        print("===============\n")
        print(Fore.GREEN + "[!] Данные по профилю Steam!" + Fore.WHITE)
        URL = "https://csgopedia.com/ru/steam-id-finder/?profiles=" + stm
        HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56'
        }
        responce = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(responce.content, 'html.parser')
        for link in soup.find_all('tr'):
            try:
                print(link.find('td').get_text())
                print(link.find('strong').get_text())
            except:
                print("")
        for link1 in soup.find_all('span', class_= 'btn-danger'):
            try:
                print("Vac ban: " + link1.find('strong').get_text() + "\n")
            except:
                print("")
        print(Fore.GREEN + "[!] Данные по инвентарю Steam! (CS:GO)\n" + Fore.WHITE)
        URL = "https://csgopedia.com/ru/inventory-value/?profiles=" + stm
        HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56'
        }
        responce = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(responce.content, 'html.parser')
        for link in soup.find_all('div',class_ = 'item'):
            try:
                #print(link.find('a', 'href', class_ = 'overlink'))
                print("Название придмета: " + link.find('div', class_ = 'name').get_text())
                print("Стоимость придмета: " + link.find('div', class_ = 'price').get_text() + "\n")
            except:
                print("")
        menu = 1
            #print(link.get_text())
        #items = soup.findAll('div', class_ = 'hscroll')
        #item.find('div', class_ = 'name')
    elif write == "0":
        menu = 0
    else:
        subprocess.call("cls",shell=True)
        print(Fore.RED + "[!] Неизвесный раздел!" + Fore.WHITE)
        menu = 1
