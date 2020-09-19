from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from fuzzywuzzy import fuzz
from PyQt5 import QtGui
import smtplib
import socket
import sys
import os


def allProject():


	#							РАБОТА С ФАЙЛАМИ							#

	def workAtFile():
		quest = input('What doit? (create, delete, open, write):\n:').lower()

		if fuzz.WRatio(quest, 'create') >= 70:

			quest_create = input("File name: ")
			with open(quest_create, 'w') as file:

				print('File created')
			
			quest_cont = input('Continue work at file?: ').lower()

			if fuzz.WRatio(quest_cont, 'yes') >= 70:

				workAtFile()

		elif fuzz.WRatio(quest, 'delete') >= 70:

			quest_delete = input("File name: ")
			os.system('del /p /f {}'.format(quest_delete))
			print('Done!')
			quest_cont = input('Continue work at file?: ').lower()

			if fuzz.WRatio(quest_cont, 'yes') >= 70:
				workAtFile()

		elif fuzz.WRatio(quest, 'open') >= 70:

			os.system(input("File name: "))
			print('Done!')
			quest_cont = input('Continue work at file?: ').lower()

			if fuzz.WRatio(quest_cont, 'yes') >= 70:
				workAtFile()

		elif fuzz.WRatio(quest, 'write') >= 70:

			quest_write = input('File name: ')
			quest_msg = input('Write : ')
			with open(quest_write, 'w') as file:
				file.write(quest_msg + '\n')
			quest_cont = input('Continue work at file?: ').lower()

			if quest_cont == 'yes' or quest_cont == 'y':
				workAtFile()

		elif quest == 'no':
			new_start()

		else:
			print('Wrong input')
			quest_cont = input('Continue work at file?: ').lower()

			if quest_cont == 'yes' or quest_cont == 'y':
				workAtFile()
			else:
				new_start()



	#			СОРТИРОВКА ВСТАВКАМИ			#


	def sort():
		arr = input('Write numbers:(with spaces no commas!)\n:')
		arr = arr.split(' ')
		i = 1
		while i < len(arr):
			cur = arr[i]
			j = i
			while j > 0 and arr[j - 1] > cur:
				arr[j] = arr[j - 1]
				j -= 1
			arr[j] = cur
			i += 1
		print(arr)
		new_start()



	#				СКАНИРОВАНИЕ ПОРТОВ					#



	def portScan():

	    host = input("Host --> ")									#ИМЯ САЙТА ЧТО НАДО ПРОВЕРИТЬ
	    print('\n')
	    port = [20, 21, 22, 23, 42, 43, 53, 67, 69, 80, 81, 443]			#ПОРТЫ ЧТО НАДО ПРОВЕРИТЬ

	    for i in port:
		    try:
		        scan = socket.socket()
		        scan.settimeout(0.5)
		        scan.connect((host, i))
		    except socket.error:
		        print("Port -- ", i, " -- [CLOSED]\n")
		    else:
		        print("Port -- ", i, " -- [OPEN]\n")
	    new_start()



	#		РАССТОЯНИЕ ЛЕВЕНШТЕЙНА			#


	def levenshtain():

		Form, _ = uic.loadUiType('levenstain-demo.ui')

		class Ui(QtWidgets.QDialog, Form):
			def __init__(self):
				super(Ui, self).__init__()
				self.setupUi(self)

				self.lineEdit_3.setReadOnly(True)
				self.pushButton.clicked.connect(self.result)

			def result(self):
				str_1 = self.lineEdit.text()
				str_2 = self.lineEdit_2.text()
				res = fuzz.WRatio(str_1, str_2)

				self.lineEdit_3.setText(str(res) + '%')

		if __name__ == '__main__':
			app = QtWidgets.QApplication(sys.argv)
			w = Ui()
			w.setWindowTitle('Levenstain distance')
			w.show()
			app.exec_()
			new_start()


	#			ОТПРАВКА ПИСЕМ				#

	def sendMail(): 
		Form, _ = uic.loadUiType('email-demo.ui')

		class Ui(QtWidgets.QDialog, Form):
			def __init__(self):
				super(Ui, self).__init__()
				self.setupUi(self)

				self.pushButton.clicked.connect(self.send)

			def send(self):
				FROM = 'Me'
				HOST = "imap.gmail.com"
				SUBJECT = self.lineEdit_2.text()
				TO = self.lineEdit.text()
				text = self.textEdit.toPlainText()
				 
				BODY = "\r\n".join((
				    "From: %s" % FROM,
				    "To: %s" % TO,
				    "Subject: %s" % SUBJECT ,
				    "",
				    text
				))
				 
				server = smtplib.SMTP(HOST, 587)
				server.starttls()
				server.login('grin.dmitry2005@gmail.com', 'Lbvf2005')
				server.sendmail(FROM, [TO], BODY)
				server.quit()

				print('Done!')


		if __name__ == '__main__':
			app = QtWidgets.QApplication(sys.argv)
			w = Ui()
			w.setWindowTitle('Email')
			w.show()
			app.exec_()
			new_start()


	#			ШИФРОВАНИЕ МОРЗЕ				#

	def morseTranslate():

		Form, _ = uic.loadUiType('demo.ui')

		class Ui(QtWidgets.QDialog, Form):
			def __init__(self):
				super(Ui, self).__init__()
				self.setupUi(self)

				self.pushButton.clicked.connect(self.translate)
				self.lineEdit_2.setReadOnly(True)

				self.setWindowTitle('Morse')
				self.setWindowIcon(QtGui.QIcon('morse-icon.ico'))

			def translate(self):
				en = self.lineEdit.text()
				ms = en.lower()

				ms = ms.replace('a', ' .- ')
				ms = ms.replace('b', ' -... ')
				ms = ms.replace('c', ' -.-. ')
				ms = ms.replace('d', ' -.. ')
				ms = ms.replace('e', ' . ')
				ms = ms.replace('f', ' ..-. ')
				ms = ms.replace('g', ' --. ')
				ms = ms.replace('h', ' .... ')
				ms = ms.replace('i', ' .. ')
				ms = ms.replace('j', ' .--- ')
				ms = ms.replace('k', ' -.- ')
				ms = ms.replace('l', ' .-.. ')
				ms = ms.replace('m', ' -- ')
				ms = ms.replace('n', ' -. ')
				ms = ms.replace('o', ' --- ')
				ms = ms.replace('p', ' .--. ')
				ms = ms.replace('q', ' --.- ')
				ms = ms.replace('r', ' .-. ')
				ms = ms.replace('s', ' ... ')
				ms = ms.replace('t', ' - ')
				ms = ms.replace('u', ' ..- ')
				ms = ms.replace('v', ' ...- ')
				ms = ms.replace('w', ' .-- ')
				ms = ms.replace('x', ' -..- ')
				ms = ms.replace('y', ' -.-- ')
				ms = ms.replace('z', ' --.. ')

				self.lineEdit_2.setText(ms)


		if __name__ == '__main__':
			app = QtWidgets.QApplication(sys.argv)
			w = Ui()
			w.show()
			app.exec_()
			new_start()



	#			ПОГОДА В ГОРОДАХ				#

	def weather():

		class Example(QWidget):
			def __init__(self):
				super().__init__()

				self.initUI()

			def initUI(self):

				self.city_label = QLabel(self)
				self.city_label.setText('City:')
				self.city_label.setFont(QtGui.QFont("Open-Sans", 11))
				self.city_label.setGeometry(140, 0, 50, 20)


				self.city_line_eidt = QLineEdit(self)
				self.city_line_eidt.setGeometry(20, 25, 257, 25)
				self.city_line_eidt.setToolTip('Write the city you are interested in')


				self.button = QPushButton('Learn', self)
				self.button.setGeometry(115, 55, 75, 25)
				self.button.clicked.connect(self.showWeather)
				self.button.setFont(QtGui.QFont("Open-Sans", 9))


				self.answer_label = QLabel(self)
				self.answer_label.setText('Answer:')
				self.answer_label.setFont(QtGui.QFont("Open-Sans", 11))
				self.answer_label.setGeometry(130, 130, 60, 20)
				self.answer_label.hide()


				self.answer_line_edit = QLineEdit(self)
				self.answer_line_edit.setGeometry(20, 160, 257, 25)
				self.answer_line_edit.setReadOnly(True)
				self.answer_line_edit.setToolTip('Weather in this city')
				self.answer_line_edit.hide()


				self.setGeometry(300, 300, 300, 192)
				self.setWindowTitle('Weather')
				self.show()


			def showWeather(self):
				import pyowm

				self.owm = pyowm.OWM( 'a7b8885d372d23485df3202cf1935ce3' )

				try:
					self.mgr = self.owm.weather_manager()
					self.city = self.city_line_eidt.text()
					self.weather = self.mgr.weather_at_place(self.city)
					self.answer_line_edit.setText(str(self.weather.weather.status) + ' {}°'.format(round(self.weather.weather.temperature('celsius')['temp'])))
				except:
					self.answer_line_edit.setText('You have incorrectly entered the city')


				self.answer_label.show()
				self.answer_line_edit.show()



		if __name__ == '__main__':

			app = QApplication(sys.argv)
			ex = Example()
			app.exec_()
			new_start()



	def start():

		quest_main = input('What doit? (file, sort, scan, levenshtain, send mail, morse, weather)\n:').lower()

		if fuzz.WRatio(quest_main, 'work at file') >= 70 or fuzz.WRatio(quest_main, 'file') >= 70:

			workAtFile()

		elif (quest_main == 'sort' or quest_main == 'sort by inserts'
			or quest_main == 'inserts sort'):

			sort()

		elif (fuzz.WRatio(quest_main, 'scan') >= 70 or fuzz.WRatio(quest_main, 'port scan') >= 70
			or fuzz.WRatio(quest_main, 'scan port') >= 70 or fuzz.WRatio(quest_main, 'port scanning') >= 70):

			portScan()

		elif (fuzz.WRatio(quest_main, 'levenshtain') >= 70 or fuzz.WRatio(quest_main, 'levenshtein distance') >= 70
			or fuzz.WRatio(quest_main, 'distance levenshtein') >= 70 or fuzz.WRatio(quest_main, 'lev') >= 70
			or fuzz.WRatio(quest_main, 'leven') >= 70):

			levenshtain()

		elif (fuzz.WRatio(quest_main, 'send') >= 70 or fuzz.WRatio(quest_main, 'mail') >= 70
			or fuzz.WRatio(quest_main, 'email') >= 70 or fuzz.WRatio(quest_main, 'send mail') >= 70
			or fuzz.WRatio(quest_main, 'send email') >= 70):

			sendMail()

		elif fuzz.WRatio(quest_main, 'morse') >= 70 or fuzz.WRatio(quest_main, 'translate') >= 70:

			morseTranslate()

		elif fuzz.WRatio(quest_main, 'weather') >= 70:

			weather()

		else:

			print('Wrong input')


	def new_start():
		quest_cont = input('Start?: ').lower()

		if quest_cont == 'yes' or quest_cont == 'y':
			start()
		elif quest_cont == 'no' or quest_cont == 'n':
			print('Goodbye!')
	new_start()

allProject()