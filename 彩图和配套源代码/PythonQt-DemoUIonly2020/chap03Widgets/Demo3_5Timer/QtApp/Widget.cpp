﻿#include "Widget.h"
#include "ui_Widget.h"

Widget::Widget(QWidget *parent) :
   QWidget(parent),
   ui(new Ui::Widget)
{
   ui->setupUi(this);
}

Widget::~Widget()
{
   delete ui;
}


void Widget::on_btnStart_clicked()
{

}

void Widget::on_btnSetIntv_clicked()
{

}
