echo off

rem ����Ŀ¼ QtApp �µ�.ui�ļ����Ƶ���ǰĿ¼�£����ұ���
copy .\QtApp\MainWindow.ui  MainWindow.ui
pyuic5 -o ui_MainWindow.py  MainWindow.ui

copy .\QtApp\QWFormDoc.ui  QWFormDoc.ui 
pyuic5 -o ui_QWFormDoc.py  QWFormDoc.ui 


rem ���벢������Դ�ļ�
pyrcc5 .\QtApp\res.qrc -o res_rc.py

