/********************************************************************************
** Form generated from reading UI file 'Widget.ui'
**
** Created by: Qt User Interface Compiler version 5.10.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WIDGET_H
#define UI_WIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QTreeWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Widget
{
public:
    QVBoxLayout *verticalLayout_6;
    QFrame *frame;
    QHBoxLayout *horizontalLayout;
    QGroupBox *groupBox_6;
    QVBoxLayout *verticalLayout_5;
    QRadioButton *radio_Source;
    QRadioButton *radio_List;
    QRadioButton *radio_Tree;
    QRadioButton *radio_Table;
    QGroupBox *groupBox_5;
    QGridLayout *gridLayout;
    QLabel *label_2;
    QCheckBox *chkBox_AcceptDrops;
    QCheckBox *chkBox_DragEnabled;
    QComboBox *combo_DefaultAction;
    QLabel *label_3;
    QComboBox *combo_Mode;
    QSpacerItem *horizontalSpacer;
    QHBoxLayout *horizontalLayout_2;
    QGroupBox *groupBox_1;
    QVBoxLayout *verticalLayout_2;
    QListWidget *listSource;
    QGroupBox *groupBox_2;
    QVBoxLayout *verticalLayout;
    QListWidget *listWidget;
    QGroupBox *groupBox_3;
    QVBoxLayout *verticalLayout_3;
    QTreeWidget *treeWidget;
    QGroupBox *groupBox_4;
    QVBoxLayout *verticalLayout_4;
    QTableWidget *tableWidget;

    void setupUi(QWidget *Widget)
    {
        if (Widget->objectName().isEmpty())
            Widget->setObjectName(QStringLiteral("Widget"));
        Widget->resize(712, 502);
        QFont font;
        font.setPointSize(10);
        Widget->setFont(font);
        verticalLayout_6 = new QVBoxLayout(Widget);
        verticalLayout_6->setSpacing(6);
        verticalLayout_6->setContentsMargins(11, 11, 11, 11);
        verticalLayout_6->setObjectName(QStringLiteral("verticalLayout_6"));
        verticalLayout_6->setContentsMargins(2, 2, 2, 2);
        frame = new QFrame(Widget);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setFrameShape(QFrame::Panel);
        frame->setFrameShadow(QFrame::Raised);
        horizontalLayout = new QHBoxLayout(frame);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalLayout->setContentsMargins(5, 5, 5, 5);
        groupBox_6 = new QGroupBox(frame);
        groupBox_6->setObjectName(QStringLiteral("groupBox_6"));
        verticalLayout_5 = new QVBoxLayout(groupBox_6);
        verticalLayout_5->setSpacing(6);
        verticalLayout_5->setContentsMargins(11, 11, 11, 11);
        verticalLayout_5->setObjectName(QStringLiteral("verticalLayout_5"));
        radio_Source = new QRadioButton(groupBox_6);
        radio_Source->setObjectName(QStringLiteral("radio_Source"));
        radio_Source->setChecked(true);

        verticalLayout_5->addWidget(radio_Source);

        radio_List = new QRadioButton(groupBox_6);
        radio_List->setObjectName(QStringLiteral("radio_List"));

        verticalLayout_5->addWidget(radio_List);

        radio_Tree = new QRadioButton(groupBox_6);
        radio_Tree->setObjectName(QStringLiteral("radio_Tree"));

        verticalLayout_5->addWidget(radio_Tree);

        radio_Table = new QRadioButton(groupBox_6);
        radio_Table->setObjectName(QStringLiteral("radio_Table"));

        verticalLayout_5->addWidget(radio_Table);


        horizontalLayout->addWidget(groupBox_6);

        groupBox_5 = new QGroupBox(frame);
        groupBox_5->setObjectName(QStringLiteral("groupBox_5"));
        gridLayout = new QGridLayout(groupBox_5);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setVerticalSpacing(9);
        label_2 = new QLabel(groupBox_5);
        label_2->setObjectName(QStringLiteral("label_2"));

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        chkBox_AcceptDrops = new QCheckBox(groupBox_5);
        chkBox_AcceptDrops->setObjectName(QStringLiteral("chkBox_AcceptDrops"));

        gridLayout->addWidget(chkBox_AcceptDrops, 0, 0, 1, 1);

        chkBox_DragEnabled = new QCheckBox(groupBox_5);
        chkBox_DragEnabled->setObjectName(QStringLiteral("chkBox_DragEnabled"));

        gridLayout->addWidget(chkBox_DragEnabled, 0, 1, 1, 1);

        combo_DefaultAction = new QComboBox(groupBox_5);
        combo_DefaultAction->addItem(QString());
        combo_DefaultAction->addItem(QString());
        combo_DefaultAction->addItem(QString());
        combo_DefaultAction->addItem(QString());
        combo_DefaultAction->addItem(QString());
        combo_DefaultAction->addItem(QString());
        combo_DefaultAction->setObjectName(QStringLiteral("combo_DefaultAction"));

        gridLayout->addWidget(combo_DefaultAction, 2, 1, 1, 1);

        label_3 = new QLabel(groupBox_5);
        label_3->setObjectName(QStringLiteral("label_3"));

        gridLayout->addWidget(label_3, 2, 0, 1, 1);

        combo_Mode = new QComboBox(groupBox_5);
        combo_Mode->addItem(QString());
        combo_Mode->addItem(QString());
        combo_Mode->addItem(QString());
        combo_Mode->addItem(QString());
        combo_Mode->addItem(QString());
        combo_Mode->setObjectName(QStringLiteral("combo_Mode"));
        combo_Mode->setMinimumSize(QSize(120, 0));

        gridLayout->addWidget(combo_Mode, 1, 1, 1, 1);


        horizontalLayout->addWidget(groupBox_5);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);


        verticalLayout_6->addWidget(frame);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        groupBox_1 = new QGroupBox(Widget);
        groupBox_1->setObjectName(QStringLiteral("groupBox_1"));
        QFont font1;
        font1.setBold(false);
        font1.setWeight(50);
        groupBox_1->setFont(font1);
        groupBox_1->setFlat(false);
        groupBox_1->setCheckable(false);
        verticalLayout_2 = new QVBoxLayout(groupBox_1);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        listSource = new QListWidget(groupBox_1);
        QIcon icon;
        icon.addFile(QStringLiteral(":/icons/images/200.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        QListWidgetItem *__qlistwidgetitem = new QListWidgetItem(listSource);
        __qlistwidgetitem->setIcon(icon);
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/icons/images/202.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        QListWidgetItem *__qlistwidgetitem1 = new QListWidgetItem(listSource);
        __qlistwidgetitem1->setIcon(icon1);
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/icons/images/204.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        QListWidgetItem *__qlistwidgetitem2 = new QListWidgetItem(listSource);
        __qlistwidgetitem2->setIcon(icon2);
        QIcon icon3;
        icon3.addFile(QStringLiteral(":/icons/images/500.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        QListWidgetItem *__qlistwidgetitem3 = new QListWidgetItem(listSource);
        __qlistwidgetitem3->setIcon(icon3);
        QIcon icon4;
        icon4.addFile(QStringLiteral(":/icons/images/502.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        QListWidgetItem *__qlistwidgetitem4 = new QListWidgetItem(listSource);
        __qlistwidgetitem4->setIcon(icon4);
        QIcon icon5;
        icon5.addFile(QStringLiteral(":/icons/images/504.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        QListWidgetItem *__qlistwidgetitem5 = new QListWidgetItem(listSource);
        __qlistwidgetitem5->setIcon(icon5);
        QIcon icon6;
        icon6.addFile(QStringLiteral(":/icons/images/508.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        QListWidgetItem *__qlistwidgetitem6 = new QListWidgetItem(listSource);
        __qlistwidgetitem6->setIcon(icon6);
        QIcon icon7;
        icon7.addFile(QStringLiteral(":/icons/images/510.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        QListWidgetItem *__qlistwidgetitem7 = new QListWidgetItem(listSource);
        __qlistwidgetitem7->setIcon(icon7);
        QIcon icon8;
        icon8.addFile(QStringLiteral(":/icons/images/512.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        QListWidgetItem *__qlistwidgetitem8 = new QListWidgetItem(listSource);
        __qlistwidgetitem8->setIcon(icon8);
        QIcon icon9;
        icon9.addFile(QStringLiteral(":/icons/images/718.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        QListWidgetItem *__qlistwidgetitem9 = new QListWidgetItem(listSource);
        __qlistwidgetitem9->setIcon(icon9);
        QIcon icon10;
        icon10.addFile(QStringLiteral(":/icons/images/724.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        QListWidgetItem *__qlistwidgetitem10 = new QListWidgetItem(listSource);
        __qlistwidgetitem10->setIcon(icon10);
        QIcon icon11;
        icon11.addFile(QStringLiteral(":/icons/images/728.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        QListWidgetItem *__qlistwidgetitem11 = new QListWidgetItem(listSource);
        __qlistwidgetitem11->setIcon(icon11);
        listSource->setObjectName(QStringLiteral("listSource"));
        listSource->setEditTriggers(QAbstractItemView::NoEditTriggers);
        listSource->setDragDropMode(QAbstractItemView::DragOnly);
        listSource->setAlternatingRowColors(true);
        listSource->setUniformItemSizes(false);
        listSource->setSelectionRectVisible(true);

        verticalLayout_2->addWidget(listSource);


        horizontalLayout_2->addWidget(groupBox_1);

        groupBox_2 = new QGroupBox(Widget);
        groupBox_2->setObjectName(QStringLiteral("groupBox_2"));
        verticalLayout = new QVBoxLayout(groupBox_2);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        listWidget = new QListWidget(groupBox_2);
        listWidget->setObjectName(QStringLiteral("listWidget"));
        listWidget->setEditTriggers(QAbstractItemView::NoEditTriggers);
        listWidget->setDragDropMode(QAbstractItemView::NoDragDrop);
        listWidget->setDefaultDropAction(Qt::CopyAction);
        listWidget->setViewMode(QListView::ListMode);

        verticalLayout->addWidget(listWidget);


        horizontalLayout_2->addWidget(groupBox_2);

        groupBox_3 = new QGroupBox(Widget);
        groupBox_3->setObjectName(QStringLiteral("groupBox_3"));
        verticalLayout_3 = new QVBoxLayout(groupBox_3);
        verticalLayout_3->setSpacing(6);
        verticalLayout_3->setContentsMargins(11, 11, 11, 11);
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        treeWidget = new QTreeWidget(groupBox_3);
        new QTreeWidgetItem(treeWidget);
        new QTreeWidgetItem(treeWidget);
        treeWidget->setObjectName(QStringLiteral("treeWidget"));
        treeWidget->setAcceptDrops(true);
        treeWidget->setEditTriggers(QAbstractItemView::NoEditTriggers);
        treeWidget->setDragDropOverwriteMode(true);
        treeWidget->setDragDropMode(QAbstractItemView::InternalMove);
        treeWidget->setDefaultDropAction(Qt::MoveAction);
        treeWidget->header()->setVisible(false);

        verticalLayout_3->addWidget(treeWidget);


        horizontalLayout_2->addWidget(groupBox_3);

        groupBox_4 = new QGroupBox(Widget);
        groupBox_4->setObjectName(QStringLiteral("groupBox_4"));
        verticalLayout_4 = new QVBoxLayout(groupBox_4);
        verticalLayout_4->setSpacing(6);
        verticalLayout_4->setContentsMargins(11, 11, 11, 11);
        verticalLayout_4->setObjectName(QStringLiteral("verticalLayout_4"));
        tableWidget = new QTableWidget(groupBox_4);
        if (tableWidget->columnCount() < 2)
            tableWidget->setColumnCount(2);
        if (tableWidget->rowCount() < 6)
            tableWidget->setRowCount(6);
        tableWidget->setObjectName(QStringLiteral("tableWidget"));
        tableWidget->setMinimumSize(QSize(180, 0));
        tableWidget->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tableWidget->setDragDropMode(QAbstractItemView::DropOnly);
        tableWidget->setDefaultDropAction(Qt::CopyAction);
        tableWidget->setAlternatingRowColors(true);
        tableWidget->setSelectionMode(QAbstractItemView::SingleSelection);
        tableWidget->setRowCount(6);
        tableWidget->setColumnCount(2);
        tableWidget->horizontalHeader()->setDefaultSectionSize(75);
        tableWidget->verticalHeader()->setDefaultSectionSize(25);

        verticalLayout_4->addWidget(tableWidget);


        horizontalLayout_2->addWidget(groupBox_4);


        verticalLayout_6->addLayout(horizontalLayout_2);


        retranslateUi(Widget);

        QMetaObject::connectSlotsByName(Widget);
    } // setupUi

    void retranslateUi(QWidget *Widget)
    {
        Widget->setWindowTitle(QApplication::translate("Widget", "Demo5_5, \345\205\267\346\234\211DragDrop\345\212\237\350\203\275\347\232\204\347\273\204\344\273\266", nullptr));
        groupBox_6->setTitle(QApplication::translate("Widget", "\350\256\276\347\275\256\345\257\271\350\261\241", nullptr));
        radio_Source->setText(QApplication::translate("Widget", "listWidget_Source", nullptr));
        radio_List->setText(QApplication::translate("Widget", "listWidget", nullptr));
        radio_Tree->setText(QApplication::translate("Widget", "treeWidget", nullptr));
        radio_Table->setText(QApplication::translate("Widget", "tableWidget", nullptr));
        groupBox_5->setTitle(QApplication::translate("Widget", "\346\213\226\346\224\276\345\217\202\346\225\260\350\256\276\347\275\256", nullptr));
        label_2->setText(QApplication::translate("Widget", "dragDropMode", nullptr));
        chkBox_AcceptDrops->setText(QApplication::translate("Widget", "acceptDrops", nullptr));
        chkBox_DragEnabled->setText(QApplication::translate("Widget", "dragEnabled", nullptr));
        combo_DefaultAction->setItemText(0, QApplication::translate("Widget", "CopyAction", nullptr));
        combo_DefaultAction->setItemText(1, QApplication::translate("Widget", "MoveAction", nullptr));
        combo_DefaultAction->setItemText(2, QApplication::translate("Widget", "LinkAction", nullptr));
        combo_DefaultAction->setItemText(3, QApplication::translate("Widget", "ActionMask", nullptr));
        combo_DefaultAction->setItemText(4, QApplication::translate("Widget", "IgnoreAction", nullptr));
        combo_DefaultAction->setItemText(5, QApplication::translate("Widget", "TargetMoveAction", nullptr));

        label_3->setText(QApplication::translate("Widget", "defaultDropAction", nullptr));
        combo_Mode->setItemText(0, QApplication::translate("Widget", "NoDragDrop", nullptr));
        combo_Mode->setItemText(1, QApplication::translate("Widget", "DragOnly", nullptr));
        combo_Mode->setItemText(2, QApplication::translate("Widget", "DropOnly", nullptr));
        combo_Mode->setItemText(3, QApplication::translate("Widget", "DragDrop", nullptr));
        combo_Mode->setItemText(4, QApplication::translate("Widget", "InternalMove", nullptr));

        groupBox_1->setTitle(QApplication::translate("Widget", "listWidget_Source", nullptr));

        const bool __sortingEnabled = listSource->isSortingEnabled();
        listSource->setSortingEnabled(false);
        QListWidgetItem *___qlistwidgetitem = listSource->item(0);
        ___qlistwidgetitem->setText(QApplication::translate("Widget", "\345\211\252\345\210\207", nullptr));
        QListWidgetItem *___qlistwidgetitem1 = listSource->item(1);
        ___qlistwidgetitem1->setText(QApplication::translate("Widget", "\345\244\215\345\210\266", nullptr));
        QListWidgetItem *___qlistwidgetitem2 = listSource->item(2);
        ___qlistwidgetitem2->setText(QApplication::translate("Widget", "\347\262\230\350\264\264", nullptr));
        QListWidgetItem *___qlistwidgetitem3 = listSource->item(3);
        ___qlistwidgetitem3->setText(QApplication::translate("Widget", "\347\262\227\344\275\223", nullptr));
        QListWidgetItem *___qlistwidgetitem4 = listSource->item(4);
        ___qlistwidgetitem4->setText(QApplication::translate("Widget", "\346\226\234\344\275\223", nullptr));
        QListWidgetItem *___qlistwidgetitem5 = listSource->item(5);
        ___qlistwidgetitem5->setText(QApplication::translate("Widget", "\344\270\213\345\210\222\347\272\277", nullptr));
        QListWidgetItem *___qlistwidgetitem6 = listSource->item(6);
        ___qlistwidgetitem6->setText(QApplication::translate("Widget", "\345\267\246\345\257\271\351\275\220", nullptr));
        QListWidgetItem *___qlistwidgetitem7 = listSource->item(7);
        ___qlistwidgetitem7->setText(QApplication::translate("Widget", "\344\270\255\351\227\264\345\257\271\351\275\220", nullptr));
        QListWidgetItem *___qlistwidgetitem8 = listSource->item(8);
        ___qlistwidgetitem8->setText(QApplication::translate("Widget", "\345\217\263\345\257\271\351\275\220", nullptr));
        QListWidgetItem *___qlistwidgetitem9 = listSource->item(9);
        ___qlistwidgetitem9->setText(QApplication::translate("Widget", "\347\272\242\350\211\262", nullptr));
        QListWidgetItem *___qlistwidgetitem10 = listSource->item(10);
        ___qlistwidgetitem10->setText(QApplication::translate("Widget", "\347\273\277\350\211\262", nullptr));
        QListWidgetItem *___qlistwidgetitem11 = listSource->item(11);
        ___qlistwidgetitem11->setText(QApplication::translate("Widget", "\350\223\235\350\211\262", nullptr));
        listSource->setSortingEnabled(__sortingEnabled);

        groupBox_2->setTitle(QApplication::translate("Widget", "listWidget", nullptr));
        groupBox_3->setTitle(QApplication::translate("Widget", "treeWidget", nullptr));
        QTreeWidgetItem *___qtreewidgetitem = treeWidget->headerItem();
        ___qtreewidgetitem->setText(0, QApplication::translate("Widget", "\347\274\226\350\276\221", nullptr));

        const bool __sortingEnabled1 = treeWidget->isSortingEnabled();
        treeWidget->setSortingEnabled(false);
        QTreeWidgetItem *___qtreewidgetitem1 = treeWidget->topLevelItem(0);
        ___qtreewidgetitem1->setText(0, QApplication::translate("Widget", "\347\274\226\350\276\221", nullptr));
        QTreeWidgetItem *___qtreewidgetitem2 = treeWidget->topLevelItem(1);
        ___qtreewidgetitem2->setText(0, QApplication::translate("Widget", "\346\240\274\345\274\217", nullptr));
        treeWidget->setSortingEnabled(__sortingEnabled1);

        groupBox_4->setTitle(QApplication::translate("Widget", "tableWidget", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Widget: public Ui_Widget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WIDGET_H
