from PyQt5 import QtGui, QtCore, QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)



class MyWidget(QtWidgets.QWidget):
  def __init__(self, parent=None):
    super(MyWidget, self).__init__(parent)
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
#    self.quitBut.clicked.connect(self.myQuit)
    
    self.quitLayout = QtWidgets.QHBoxLayout()
    self.quitLayout.addWidget(self.quitBut)
    
    
    # Top layout
    self.topLayout = QtWidgets.QVBoxLayout()
    self.topLayout.addLayout(self.coinEditLayout)
    self.topLayout.addLayout(self.quitLayout)
    
    self.setLayout(self.topLayout)
    

    
widget = MyWidget()
widget.setFixedSize(200,270)
widget.show()
app.exec_()