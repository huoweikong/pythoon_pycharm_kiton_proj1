﻿#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include    <QMainWindow>
#include    <QMediaPlayer>
#include    <QMediaPlaylist>
#include    <QVideoWidget>

#include    <QGraphicsVideoItem>

#include    <QGraphicsTextItem>


namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
//自定义槽函数
    void do_stateChanged(QMediaPlayer::State state);

    void do_durationChanged(qint64 duration);

    void do_positionChanged(qint64 position);

//
    void on_btnPlay_clicked();

    void on_btnPause_clicked();

    void on_btnStop_clicked();


private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
