import sys

from PyQt5.QtWidgets import  QApplication, QDialog, QAbstractItemView

from PyQt5.QtCore import  QStringListModel,Qt

##from PyQt5.QtCore import  pyqtSlot,Qt

##from PyQt5.QtWidgets import  

##from PyQt5.QtGui import

from ui_QWDialogHeaders import Ui_QWDialogHeaders

class QmyDialogHeaders(QDialog): 
   def __init__(self, parent=None):
      super().__init__(parent)      #调用父类构造函数，创建窗体
      self.ui=Ui_QWDialogHeaders()  #创建UI对象
      self.ui.setupUi(self)         #构造UI界面
      pass


   def __del__(self): #析构函数
      pass
      
        
##  ==============自定义功能函数============
   def setHeaderList(self,headerStrList):
      pass
   

   def headerList(self):
      pass
        
        
##  ==========由connectSlotsByName() 自动连接的槽函数==================        
    
        
        
##  =============自定义槽函数===============================        


   
##  ============窗体测试程序 ================================
if  __name__ == "__main__":         #用于当前窗体测试
   app = QApplication(sys.argv)     #创建GUI应用程序
   form=QmyDialogHeaders()          #创建窗体
   form.show()
   sys.exit(app.exec_())
