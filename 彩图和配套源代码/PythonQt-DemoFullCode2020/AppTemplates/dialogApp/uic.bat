echo off

rem ����Ŀ¼ QtApp �µ�.ui�ļ����Ƶ���ǰĿ¼�£����ұ���
copy .\QtApp\Dialog.ui  Dialog.ui
pyuic5 -o ui_Dialog.py  Dialog.ui

rem ���벢������Դ�ļ�
pyrcc5 .\QtApp\res.qrc -o res_rc.py

