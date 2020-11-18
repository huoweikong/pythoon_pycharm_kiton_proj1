# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 533)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_6 = QtWidgets.QFrame(self.centralWidget)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.toolBtn_GenData = QtWidgets.QToolButton(self.frame_6)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/828.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBtn_GenData.setIcon(icon)
        self.toolBtn_GenData.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBtn_GenData.setObjectName("toolBtn_GenData")
        self.horizontalLayout_7.addWidget(self.toolBtn_GenData)
        self.toolBtn_Counting = QtWidgets.QToolButton(self.frame_6)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/216.GIF"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBtn_Counting.setIcon(icon1)
        self.toolBtn_Counting.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBtn_Counting.setObjectName("toolBtn_Counting")
        self.horizontalLayout_7.addWidget(self.toolBtn_Counting)
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.comboTheme = QtWidgets.QComboBox(self.frame_6)
        self.comboTheme.setMinimumSize(QtCore.QSize(120, 0))
        self.comboTheme.setObjectName("comboTheme")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.horizontalLayout_7.addWidget(self.comboTheme)
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.comboAnimation = QtWidgets.QComboBox(self.frame_6)
        self.comboAnimation.setObjectName("comboAnimation")
        self.comboAnimation.addItem("")
        self.comboAnimation.addItem("")
        self.comboAnimation.addItem("")
        self.comboAnimation.addItem("")
        self.horizontalLayout_7.addWidget(self.comboAnimation)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.toolBtn_Quit = QtWidgets.QToolButton(self.frame_6)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBtn_Quit.setIcon(icon2)
        self.toolBtn_Quit.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBtn_Quit.setObjectName("toolBtn_Quit")
        self.horizontalLayout_7.addWidget(self.toolBtn_Quit)
        self.verticalLayout_13.addWidget(self.frame_6)
        self.splitter_2 = QtWidgets.QSplitter(self.centralWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.frameData = QtWidgets.QFrame(self.splitter_2)
        self.frameData.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameData.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameData.setObjectName("frameData")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameData)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.frameData)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setContentsMargins(11, 2, 11, 2)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.spinCount = QtWidgets.QSpinBox(self.frame_2)
        self.spinCount.setMinimum(5)
        self.spinCount.setMaximum(5000)
        self.spinCount.setProperty("value", 20)
        self.spinCount.setObjectName("spinCount")
        self.horizontalLayout_6.addWidget(self.spinCount)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_2)
        self.tableView = QtWidgets.QTableView(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableView.setFont(font)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setDefaultSectionSize(80)
        self.tableView.verticalHeader().setDefaultSectionSize(25)
        self.verticalLayout.addWidget(self.tableView)
        self.groupBox_7 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox_7)
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.setFont(font)
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setIndentation(0)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(2, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(3, QtCore.Qt.AlignCenter)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setDefaultSectionSize(90)
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.verticalLayout_3.addWidget(self.splitter)
        self.tabWidget = QtWidgets.QTabWidget(self.splitter_2)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBuildBarChart = QtWidgets.QPushButton(self.frame)
        self.btnBuildBarChart.setObjectName("btnBuildBarChart")
        self.horizontalLayout.addWidget(self.btnBuildBarChart)
        self.btnBuildBarChartH = QtWidgets.QPushButton(self.frame)
        self.btnBuildBarChartH.setObjectName("btnBuildBarChartH")
        self.horizontalLayout.addWidget(self.btnBuildBarChartH)
        spacerItem2 = QtWidgets.QSpacerItem(662, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_8.addWidget(self.frame)
        self.chartViewBar = QmyChartView(self.widget)
        self.chartViewBar.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.chartViewBar.setObjectName("chartViewBar")
        self.verticalLayout_8.addWidget(self.chartViewBar)
        self.verticalLayout_9.addWidget(self.widget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon3, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.widget_2 = QtWidgets.QWidget(self.tab_3)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.widget_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnBuildStackedBar = QtWidgets.QPushButton(self.frame_3)
        self.btnBuildStackedBar.setObjectName("btnBuildStackedBar")
        self.horizontalLayout_3.addWidget(self.btnBuildStackedBar)
        self.btnBuildStackedBarH = QtWidgets.QPushButton(self.frame_3)
        self.btnBuildStackedBarH.setObjectName("btnBuildStackedBarH")
        self.horizontalLayout_3.addWidget(self.btnBuildStackedBarH)
        spacerItem3 = QtWidgets.QSpacerItem(536, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.chartViewStackedBar = QmyChartView(self.widget_2)
        self.chartViewStackedBar.setObjectName("chartViewStackedBar")
        self.verticalLayout_5.addWidget(self.chartViewStackedBar)
        self.verticalLayout_10.addWidget(self.widget_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/281.GIF"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.widget_4 = QtWidgets.QWidget(self.tab_5)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.widget_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnPercentBar = QtWidgets.QPushButton(self.frame_5)
        self.btnPercentBar.setObjectName("btnPercentBar")
        self.horizontalLayout_4.addWidget(self.btnPercentBar)
        self.btnPercentBarH = QtWidgets.QPushButton(self.frame_5)
        self.btnPercentBarH.setObjectName("btnPercentBarH")
        self.horizontalLayout_4.addWidget(self.btnPercentBarH)
        spacerItem4 = QtWidgets.QSpacerItem(523, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.chartViewPercentBar = QmyChartView(self.widget_4)
        self.chartViewPercentBar.setObjectName("chartViewPercentBar")
        self.verticalLayout_6.addWidget(self.chartViewPercentBar)
        self.verticalLayout_12.addWidget(self.widget_4)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/f4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_5, icon5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.widget_3 = QtWidgets.QWidget(self.tab_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.widget_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboCourse = QtWidgets.QComboBox(self.frame_4)
        self.comboCourse.setMinimumSize(QtCore.QSize(60, 0))
        self.comboCourse.setObjectName("comboCourse")
        self.comboCourse.addItem("")
        self.comboCourse.addItem("")
        self.comboCourse.addItem("")
        self.horizontalLayout_2.addWidget(self.comboCourse)
        self.btnDrawPieChart = QtWidgets.QPushButton(self.frame_4)
        self.btnDrawPieChart.setObjectName("btnDrawPieChart")
        self.horizontalLayout_2.addWidget(self.btnDrawPieChart)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinHoleSize = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.spinHoleSize.setMinimumSize(QtCore.QSize(70, 0))
        self.spinHoleSize.setDecimals(2)
        self.spinHoleSize.setMaximum(1.0)
        self.spinHoleSize.setSingleStep(0.1)
        self.spinHoleSize.setObjectName("spinHoleSize")
        self.horizontalLayout_2.addWidget(self.spinHoleSize)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinPieSize = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.spinPieSize.setMinimumSize(QtCore.QSize(70, 0))
        self.spinPieSize.setMaximum(1.0)
        self.spinPieSize.setSingleStep(0.1)
        self.spinPieSize.setProperty("value", 0.7)
        self.spinPieSize.setObjectName("spinPieSize")
        self.horizontalLayout_2.addWidget(self.spinPieSize)
        self.chkBox_PieLegend = QtWidgets.QCheckBox(self.frame_4)
        self.chkBox_PieLegend.setChecked(True)
        self.chkBox_PieLegend.setObjectName("chkBox_PieLegend")
        self.horizontalLayout_2.addWidget(self.chkBox_PieLegend)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.chartViewPie = QmyChartView(self.widget_3)
        self.chartViewPie.setObjectName("chartViewPie")
        self.verticalLayout_4.addWidget(self.chartViewPie)
        self.verticalLayout_11.addWidget(self.widget_3)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/43.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon6, "")
        self.verticalLayout_13.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBtn_Quit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "饼图和柱状图"))
        self.toolBtn_GenData.setToolTip(_translate("MainWindow", "重新生成数据并统计"))
        self.toolBtn_GenData.setText(_translate("MainWindow", "重新生成数据"))
        self.toolBtn_Counting.setToolTip(_translate("MainWindow", "重新统计"))
        self.toolBtn_Counting.setText(_translate("MainWindow", "重新统计"))
        self.label_7.setText(_translate("MainWindow", "图表主题"))
        self.comboTheme.setItemText(0, _translate("MainWindow", "Light"))
        self.comboTheme.setItemText(1, _translate("MainWindow", "BlueCerulean"))
        self.comboTheme.setItemText(2, _translate("MainWindow", "Dark"))
        self.comboTheme.setItemText(3, _translate("MainWindow", "BrownSand"))
        self.comboTheme.setItemText(4, _translate("MainWindow", "BlueNcs"))
        self.comboTheme.setItemText(5, _translate("MainWindow", "HighContrast"))
        self.comboTheme.setItemText(6, _translate("MainWindow", "BlueIcy"))
        self.comboTheme.setItemText(7, _translate("MainWindow", "Qt"))
        self.label_8.setText(_translate("MainWindow", "图表动画效果"))
        self.comboAnimation.setItemText(0, _translate("MainWindow", "NoAnimation"))
        self.comboAnimation.setItemText(1, _translate("MainWindow", "GridAxisAnimations"))
        self.comboAnimation.setItemText(2, _translate("MainWindow", "SeriesAnimations"))
        self.comboAnimation.setItemText(3, _translate("MainWindow", "AllAnimations"))
        self.toolBtn_Quit.setText(_translate("MainWindow", "退出"))
        self.groupBox.setTitle(_translate("MainWindow", "原始分数"))
        self.label_5.setText(_translate("MainWindow", "学生人数"))
        self.groupBox_7.setTitle(_translate("MainWindow", "人数统计"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "分数段"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "数学"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "语文"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "英语"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "60分以下"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "60-69分"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "70-79分"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "80-89分"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "90分以上"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.btnBuildBarChart.setText(_translate("MainWindow", "绘制柱状图"))
        self.btnBuildBarChartH.setText(_translate("MainWindow", "绘制水平柱状图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "BarChart"))
        self.btnBuildStackedBar.setText(_translate("MainWindow", "绘制堆叠柱状图"))
        self.btnBuildStackedBarH.setText(_translate("MainWindow", "绘制水平堆叠柱状图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "StackedBar"))
        self.btnPercentBar.setText(_translate("MainWindow", "绘制百分比柱状图"))
        self.btnPercentBarH.setText(_translate("MainWindow", "绘制水平百分比柱状图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "PercentBar"))
        self.label.setText(_translate("MainWindow", "分析数据"))
        self.comboCourse.setItemText(0, _translate("MainWindow", "数学"))
        self.comboCourse.setItemText(1, _translate("MainWindow", "语文"))
        self.comboCourse.setItemText(2, _translate("MainWindow", "英语"))
        self.btnDrawPieChart.setText(_translate("MainWindow", "绘制饼图"))
        self.label_2.setText(_translate("MainWindow", "HoleSize"))
        self.label_3.setText(_translate("MainWindow", "PieSize"))
        self.chkBox_PieLegend.setText(_translate("MainWindow", "显示图例"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "PieChart"))

from myChartView import QmyChartView
import res_rc
