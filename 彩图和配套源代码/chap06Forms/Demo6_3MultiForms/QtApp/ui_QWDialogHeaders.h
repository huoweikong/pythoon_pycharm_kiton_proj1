/********************************************************************************
** Form generated from reading UI file 'QWDialogHeaders.ui'
**
** Created by: Qt User Interface Compiler version 5.10.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QWDIALOGHEADERS_H
#define UI_QWDIALOGHEADERS_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QListView>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_QWDialogHeaders
{
public:
    QVBoxLayout *verticalLayout_3;
    QHBoxLayout *horizontalLayout;
    QGroupBox *groupBox;
    QVBoxLayout *verticalLayout;
    QListView *listView;
    QFrame *frame;
    QVBoxLayout *verticalLayout_2;
    QSpacerItem *verticalSpacer_4;
    QPushButton *btnOK;
    QSpacerItem *verticalSpacer_2;
    QPushButton *btnCancel;
    QSpacerItem *verticalSpacer;
    QSpacerItem *verticalSpacer_6;
    QSpacerItem *verticalSpacer_5;
    QSpacerItem *verticalSpacer_3;

    void setupUi(QDialog *QWDialogHeaders)
    {
        if (QWDialogHeaders->objectName().isEmpty())
            QWDialogHeaders->setObjectName(QStringLiteral("QWDialogHeaders"));
        QWDialogHeaders->resize(289, 318);
        QFont font;
        font.setPointSize(10);
        QWDialogHeaders->setFont(font);
        verticalLayout_3 = new QVBoxLayout(QWDialogHeaders);
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        verticalLayout_3->setContentsMargins(5, 5, 5, 5);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        groupBox = new QGroupBox(QWDialogHeaders);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        verticalLayout = new QVBoxLayout(groupBox);
        verticalLayout->setSpacing(4);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(5, 5, 5, 5);
        listView = new QListView(groupBox);
        listView->setObjectName(QStringLiteral("listView"));
        listView->setAlternatingRowColors(true);

        verticalLayout->addWidget(listView);


        horizontalLayout->addWidget(groupBox);

        frame = new QFrame(QWDialogHeaders);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        verticalLayout_2 = new QVBoxLayout(frame);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer_4);

        btnOK = new QPushButton(frame);
        btnOK->setObjectName(QStringLiteral("btnOK"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/icons/images/704.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        btnOK->setIcon(icon);

        verticalLayout_2->addWidget(btnOK);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer_2);

        btnCancel = new QPushButton(frame);
        btnCancel->setObjectName(QStringLiteral("btnCancel"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/icons/images/706.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        btnCancel->setIcon(icon1);

        verticalLayout_2->addWidget(btnCancel);

        verticalSpacer = new QSpacerItem(20, 28, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer);

        verticalSpacer_6 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer_6);

        verticalSpacer_5 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer_5);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer_3);


        horizontalLayout->addWidget(frame);


        verticalLayout_3->addLayout(horizontalLayout);


        retranslateUi(QWDialogHeaders);
        QObject::connect(btnOK, SIGNAL(clicked()), QWDialogHeaders, SLOT(accept()));
        QObject::connect(btnCancel, SIGNAL(clicked()), QWDialogHeaders, SLOT(reject()));

        QMetaObject::connectSlotsByName(QWDialogHeaders);
    } // setupUi

    void retranslateUi(QDialog *QWDialogHeaders)
    {
        QWDialogHeaders->setWindowTitle(QApplication::translate("QWDialogHeaders", "\350\256\276\347\275\256\350\241\250\345\244\264\346\240\207\351\242\230", nullptr));
        groupBox->setTitle(QApplication::translate("QWDialogHeaders", "\350\241\250\345\244\264\346\240\207\351\242\230", nullptr));
        btnOK->setText(QApplication::translate("QWDialogHeaders", "\347\241\256\345\256\232", nullptr));
        btnCancel->setText(QApplication::translate("QWDialogHeaders", "\345\217\226\346\266\210", nullptr));
    } // retranslateUi

};

namespace Ui {
    class QWDialogHeaders: public Ui_QWDialogHeaders {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QWDIALOGHEADERS_H
