from PyQt4 import QtGui QtCore
import sys


app = QtGui.QAllplication(sys.argv)



class MyWidget(QtGui.QWidget):
  def __init__(self, parent=None):
    super(MyWidget, self).__init__(parent)
    self.__createLayout()
    
  def __createLayout(self):
    
    # create element for choose coin name and set buy/sell criterion
    self.chooseCoin = QtGui.QComboBox()
    self.chooseCoin.addItem("美金")
    self.chooseCoin.addItem("紐西蘭幣")
    self.chooseCoin.addItem("澳幣")
    self.chooseCoin.addItem("歐元")
    self.chooseCoin.addItem("南非幣")
    
    self.setBuyValue = QtGui.QLineEdit()
    self.setSellValue = QtGui.QLineEdit()
    
    # layout for setting coin name and buy/sell criterion
    self.coinEditLayout = QtGui.QFormLayout()
    self.coinEditLayout.addRow("設定幣別", self.chooseCoin)
    self.coinEditLayout.addRow("設定買入條件", self.setBuyValue)
    self.coinEditLayout.addRow("設定賣出條件", self.setSellValue)
    
    
    
    
    
    
    
    # Quit Button
    self.quitBut = QtGui.QPushButton('Quit')
    self.quitBut.clicked.connect(self.myQuit)
    
    self.quitLayout = QtGui.QHBoxLayout()
    self.quitLayout.addWidget(self.quitBut)
    
    
    # Top layout
    self.topLayout = QtGui.QVBoxLayout()
    self.topLayout.addLayout(self.coinEditLayout)
    self.topLayout.addLayout(self.quitLayout)
    
    self.setLayout(self.topLayout)
    

    
wigdet = MyWidget()
widget.setFixSize(200,270)
wigdet.show()
app.exec_()