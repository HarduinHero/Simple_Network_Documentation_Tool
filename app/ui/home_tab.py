# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_tab.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_home_tab(object):
    def setupUi(self, home_tab):
        if not home_tab.objectName():
            home_tab.setObjectName(u"home_tab")
        home_tab.resize(937, 622)
        self.verticalLayout = QVBoxLayout(home_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.F_filter = QLineEdit(home_tab)
        self.F_filter.setObjectName(u"F_filter")
        self.F_filter.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.F_filter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.project_tree = QTreeWidget(home_tab)
        self.project_tree.setObjectName(u"project_tree")
        self.project_tree.setProperty("showDropIndicator", False)
        self.project_tree.setAlternatingRowColors(True)
        self.project_tree.setWordWrap(False)
        self.project_tree.setColumnCount(4)

        self.verticalLayout.addWidget(self.project_tree)


        self.retranslateUi(home_tab)

        QMetaObject.connectSlotsByName(home_tab)
    # setupUi

    def retranslateUi(self, home_tab):
        home_tab.setWindowTitle(QCoreApplication.translate("home_tab", u"Form", None))
        self.F_filter.setPlaceholderText(QCoreApplication.translate("home_tab", u"Filter", None))
        ___qtreewidgetitem = self.project_tree.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("home_tab", u"Class", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("home_tab", u"ID", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("home_tab", u"Description", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("home_tab", u"Object", None));
    # retranslateUi

