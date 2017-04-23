from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import requests
from bs4 import BeautifulSoup

app = QtWidgets.QApplication(sys.argv)



class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.getSinoPacForeignExchange()
        self.__createLayout()

    def __createLayout(self):
        # create element for choose coin name and set buy/sell criterion
        self.chooseCoin = QtWidgets.QComboBox()
        self.chooseCoin.addItem("美金")
        self.chooseCoin.addItem("紐西蘭幣")
        self.chooseCoin.addItem("澳幣")
        self.chooseCoin.addItem("歐元")
        self.chooseCoin.addItem("南非幣")
    
        self.setBuyValue = QtWidgets.QLineEdit()
        self.setSellValue = QtWidgets.QLineEdit()
        
        # layout for setting coin name and buy/sell criterion
        self.coinEditLayout = QtWidgets.QFormLayout()
        self.coinEditLayout.addRow("設定幣別", self.chooseCoin)
        self.coinEditLayout.addRow("設定買入條件", self.setBuyValue)
        self.coinEditLayout.addRow("設定賣出條件", self.setSellValue)

        # Quit Button
        self.quitBut = QtWidgets.QPushButton('Quit')
        self.quitBut.clicked.connect(self.myQuit)
        
        self.quitLayout = QtWidgets.QHBoxLayout()
        self.quitLayout.addWidget(self.quitBut)
        
        
        # Top layout
        self.topLayout = QtWidgets.QVBoxLayout()
        self.topLayout.addLayout(self.coinEditLayout)
        self.topLayout.addLayout(self.quitLayout)
        
        self.setLayout(self.topLayout)

#   def startTracking(self):

    def myQuit(self):
        self.close();

    def getSinoPacForeignExchange(self):
        self.CoinData={}
        # get ashx url response data
        __url = "https://mma.sinopac.com/ws/share/rate/ws_exchange.ashx?exchangeType=REMIT&Cross=genREMITResult"
        __urlReq = requests.get(__url)

        # transfer response data into text file
        __soup = BeautifulSoup(__urlReq.content, 'html.parser')
        __soupText = __soup.get_text()

        __coinInfo = __soupText.split('"SubInfo":')

        __coinLine = __coinInfo[1].split('},{')

        for __line in __coinLine:
            print(__line)



    
widget = MyWidget()
widget.setFixedSize(200,270)
widget.show()
app.exec_()