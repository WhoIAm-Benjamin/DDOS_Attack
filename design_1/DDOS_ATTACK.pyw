import requests as req
import fake_proxy
import sys
import socket

import design
import dialog_design
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui

def responser(a, p):
	"""
	check response from server
	:param a: URL address;
	:param p: proxy for requests;
	:return: bool value from response;
	"""
	response = req.get(a, proxies = p)
	if response.status_code == 200:
		return True
	else:
		print(a, response.status_code)
		return False

def checker():
	while True:
		if my_main_window.URL_address.text() != '':
			if my_main_window.get_ip_address():
				break
		else:
			sys.exit(app.exec_())
	my_main_window.main()


class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.start_button.clicked.connect(self.main)
		self.stop_button.clicked.connect(self.stop)
		self.pause_continue_button.clicked.connect(self.continues)
		# self.th1 = Th(target = checker)
		# заменить на QtCore.QThread()

	def main(self):
		""" Requests"""
		intermediate_value = self.URL_address.text()
		k = 1
		if 'https://' not in intermediate_value:
			address = 'https://' + intermediate_value
		while True:
			try:
				proxy = fake_proxy.get(proxy_type = 'https')[0]
				if responser(address, proxy):
					print(address,  'Всё прошло успешно, попытка №{}\r'.format(k), end = '\r')
					k += 1
					continue
				else:
					break
			except req.ConnectionError:
				address = 'http://' + intermediate_value
				proxy = fake_proxy.get(proxy_type = 'http')[0]
				responser(address, proxy)
			except ConnectionError:
				print('Ошибка соединения\r')


	def get_ip_address(self):
		try:
			ip = socket.gethostbyname(self.URL_address.text())
			self.IP_address.setText(ip)
			del self.th1
			return True
		except socket.gaierror:
			return False

	def stop(self):
		pass

	def continues(self):
		pass


class FirstWindow(QtWidgets.QDialog, dialog_design.Ui_Dialog):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.welcome_button.clicked.connect(self.hiding)

	@staticmethod
	def hiding():
		global my_main_window
		welcoming.hide()
		my_main_window = MainApp()
		my_main_window.show()


if __name__ == '__main__':
	app = QtWidgets.QApplication()
	welcoming = FirstWindow()
	welcoming.show()
	sys.exit(app.exec_())
