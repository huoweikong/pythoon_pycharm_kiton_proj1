echo off

rem ����Ŀ¼ QtApp �µ�.ui�ļ����Ƶ���ǰĿ¼�£����ұ���
copy .\QtApp\Widget.ui  Widget.ui
pyuic5 -o ui_Widget.py  Widget.ui


rem ���벢������Դ�ļ�
pyrcc5 .\QtApp\res.qrc -o res_rc.py

