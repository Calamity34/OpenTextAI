import datetime
from os.path import dirname
from os.path import abspath

filepath = dirname(abspath(__file__))

f = open(filepath + '/data/lastest.log', 'wt', encoding='UTF-8')
f.close()


def time():
    now = datetime.datetime.now()
    time = now.strftime('%H:%M:%S')
    return(f'[{time}]')


def info(text, func='root'):
    f = open(filepath + '/data/lastest.log', 'at', encoding='UTF-8')
    data = time() + ' [' + func + ']' + " [?] " + text
    print(data)
    f.write(data + '\n')
    f.close()


def warn(text, func='root'):
    f = open(filepath + '/data/lastest.log', 'at', encoding='UTF-8')
    data = time() + ' [' + func + ']' + " [!] " + text
    print(data)
    f.write(data + '\n')
    f.close()


def cmd(command, user, guild):
    f = open(filepath + '/data/lastest.log', 'at', encoding='UTF-8')
    data = '{0} @{1} использовал команду "{2}" на сервере "{3}"'.format(
        time(), user, command, guild)
    print(data)
    f.write(data + '\n')
    f.close()
