import sys

from PyQt5.QtWidgets import  QApplication, QDialog

##from PyQt5.QtWidgets import  QDialog

from PyQt5.QtCore import  Qt

##from PyQt5.QtCore import  pyqtSlot,Qt

##from PyQt5.QtWidgets import  

##from PyQt5.QtGui import

from ui_QWDialogSize import Ui_QWDialogSize

class QmyDialogSize(QDialog): 
   def __init__(self, rowCount=3,colCount=5,parent=None):
      super().__init__(parent)      #调用父类构造函数，创建窗体
      self.ui=Ui_QWDialogSize()     #创建UI对象
      self.ui.setupUi(self)         #构造UI界面
      pass


   def __del__(self):   #析构函数
      pass
      
      
##  ==============自定义功能函数============
   def setIniSize(self,rowCount,colCount):   ##设置表格大小
      pass
   

   def getTableSize(self):    ##以元组数据同时返回行数和列数
      pass
        
        
##  ==========由connectSlotsByName() 自动连接的槽函数==================        
    
        
        
##  =============自定义槽函数===============================        


   
##  ============窗体测试程序 ================================
if  __name__ == "__main__":        #用于当前窗体测试
   app = QApplication(sys.argv)    #创建GUI应用程序
   form=QmyDialogSize()            #创建窗体
   form.show()
   sys.exit(app.exec_())
