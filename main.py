from uiClass import *
import sys

#### SETTINGS ####
LOGIN_USERNAME = "admin"
LOGIN_PASSWORD = "test123"
ENCRYPTION_THRESHOLD = 2
###################

class My_Window(Ui_MainWindow):
	
	
	def __init__(self, window):
		self.setupUi(window)
		self.loginButton.clicked.connect(self.MainPage)
		self.insertWebAndPass.clicked.connect(self.insertInfo)
		
	def MainPage(self):
		if self.usernameEntry.text() == LOGIN_USERNAME and self.passEntry.text() == LOGIN_PASSWORD:
			with open("database.txt", mode="r") as f:
				for i in f:
					de = self.decryptInfo(i)
					self.webAndPassInfo.setPlainText(self.webAndPassInfo.toPlainText() + de)
					
			self.stackedWidget.setCurrentIndex(1)

		
	def insertInfo(self):
		with open("database.txt", mode="a") as f:
			f.write(f"website:{self.rotateLeft(self.websiteEntry.text(), ENCRYPTION_THRESHOLD)};password:{self.rotateLeft(self.passwordWebsiteEntry.text(), ENCRYPTION_THRESHOLD)}\n")
			self.webAndPassInfo.setPlainText(self.webAndPassInfo.toPlainText() + f"website:{self.websiteEntry.text()};password:{self.passwordWebsiteEntry.text()}\n")
		
		
	def rotateLeft(self,string, chars):
		lFirst = string[0: chars]
		lSecond = string[chars : ]
		return lSecond + lFirst
		
		
	def rotateRight(self, string, chars):
		rFirst = string[0 : len(string)-chars] 
		rSecond = string[len(string)-chars : ] 
		return rSecond + rFirst
		
	def decryptInfo(self, string):
		try:
			websiteName = string.split(";")[0].split(":")[1]
			passwordInput = string.split(";")[1].split(":")[1]
			decryptedWN = self.rotateRight(websiteName, ENCRYPTION_THRESHOLD)
			decryptedPI = self.rotateRight(passwordInput, ENCRYPTION_THRESHOLD + 1)
			return f"\nwebsite:{decryptedWN};password:{decryptedPI}"
		except:
			return "\n"
	

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
	
ui = My_Window(MainWindow)
	
MainWindow.show()
app.exec_()
