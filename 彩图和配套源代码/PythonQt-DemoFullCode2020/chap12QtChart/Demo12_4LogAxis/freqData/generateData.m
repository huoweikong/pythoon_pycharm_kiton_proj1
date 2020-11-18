% generateData.m, �������׻��ڵķ�Ƶ,��Ƶ����  
clc
clear
wn=5;  % natural frequency
zta=0.2; %damping ratio
num=[wn*wn];  %numerator of 2nd-order system
den=[1,2*zta*wn,wn*wn];  %denominator of 2nd-order system

w=logspace(-1,2);  %10**(-1) ~10**1

[mag,ph,w]=bode(num,den,w); % generate frequency response data

mag=20*log10(mag);

subplot(2,1,1)
semilogx(w,mag,'r')
title('��Ƶ����')
% xlabel('Ƶ��rad/sec')
ylabel('����dB')
grid on

%legend('��=0.2','��=0.4','��=0.8');
subplot(2,1,2)
semilogx(w,ph,'b')
title('��Ƶ����')
xlabel('Ƶ��rad/sec')
ylabel('��λ(��)')
grid on

% format long
% mag_dB=20*log10(mag);
freqResp=[w,mag,ph];  % frequency, magnitude in dB, phase
save freqData.txt freqResp -ascii


