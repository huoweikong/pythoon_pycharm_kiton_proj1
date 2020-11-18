import sys

from PyQt5.QtWidgets import  QApplication, QWidget

##from PyQt5.QtCore import  pyqtSlot

from PyQt5.QtCore import  QDateTime, QDate, QTime

from ui_Widget import Ui_Widget

class QmyWidget(QWidget): 

   def __init__(self, parent=None):
      super().__init__(parent)   #调用父类构造函数，创建窗体
      self.ui=Ui_Widget()        #创建UI对象
      self.ui.setupUi(self)      #构造UI界面

        
##  =========由connectSlotsByName() 自动连接的槽函数=========================        
   def on_btnGetTime_clicked(self):    ## "读取当前日期时间"按钮
      pass
        
   def on_calendarWidget_selectionChanged(self):   ## 日历组件
      pass

   def on_btnSetTime_clicked(self):    ##“设置时间”按钮
      pass

   def on_btnSetDate_clicked(self):    ##“设置日期”按钮
      pass

   def on_btnSetDateTime_clicked(self):    ##“设置日期时间”按钮
      pass
        
##  ==========自定义槽函数==================================        


   
##  ==========窗体测试程序 ==================================        
if  __name__ == "__main__":        
   app = QApplication(sys.argv)     #创建GUI应用程序
   form=QmyWidget()                 #创建窗体
   form.show()
   sys.exit(app.exec_())
