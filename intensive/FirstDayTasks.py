import requests
servers = 'https://vk.com/ ' \
          'https://www.jetbrains.com/pycharm/ ' \
          'https://www.codingame.com/ide/puzzle/power-of-thor-episode-1 ' \
          'https://e.mail.ru/trash/0:16033848941010094127:500002/ ' \
          'https://metanit.com/python/tutorial/'
servers = servers.split()
rezults = []
print(servers)
input('press enter to proceed')
for i in servers:
    for j in range(1000):
        k = (requests.get(i))
        print(f'номер попытки {j + 1}, результат запроса к {i}: {k}')
    rezults.append([i, j + 1, k])
    input ('press any key and enter to proceed')
print(rezults)
