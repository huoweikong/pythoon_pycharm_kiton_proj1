﻿#include "QWDialogHeaders.h"
#include "ui_QWDialogHeaders.h"

QWDialogHeaders::QWDialogHeaders(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::QWDialogHeaders)
{
    ui->setupUi(this);

}

QWDialogHeaders::~QWDialogHeaders()
{
    delete ui;
}

