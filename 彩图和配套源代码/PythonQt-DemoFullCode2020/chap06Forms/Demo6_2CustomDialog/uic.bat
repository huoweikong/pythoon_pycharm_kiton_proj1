echo off

rem ����Ŀ¼ QtApp �µ�.ui�ļ����Ƶ���ǰĿ¼�£����ұ���

copy .\QtApp\MainWindow.ui  MainWindow.ui
pyuic5 -o ui_MainWindow.py  MainWindow.ui

copy .\QtApp\QWDialogSize.ui QWDialogSize.ui
pyuic5 -o ui_QWDialogSize.py  QWDialogSize.ui


copy .\QtApp\QWDialogLocate.ui QWDialogLocate.ui
pyuic5 -o ui_QWDialogLocate.py  QWDialogLocate.ui

copy .\QtApp\QWDialogHeaders.ui QWDialogHeaders.ui
pyuic5 -o ui_QWDialogHeaders.py  QWDialogHeaders.ui


rem ���벢������Դ�ļ�

pyrcc5 .\QtApp\res.qrc -o res_rc.py

