echo off

rem ����Ŀ¼ QtApp �µ�.ui�ļ����Ƶ���ǰĿ¼��
copy .\QtApp\Dialog.ui  Dialog.ui

rem ��pyuic5����.ui�ļ�
pyuic5 -o ui_Dialog.py  Dialog.ui