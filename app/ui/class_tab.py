# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'class_tab.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFormLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
import ui.ressources_rc

class Ui_class_tab(object):
    def setupUi(self, class_tab):
        if not class_tab.objectName():
            class_tab.setObjectName(u"class_tab")
        class_tab.resize(1065, 827)
        self.verticalLayout = QVBoxLayout(class_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BT_cancel = QPushButton(class_tab)
        self.BT_cancel.setObjectName(u"BT_cancel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BT_cancel.sizePolicy().hasHeightForWidth())
        self.BT_cancel.setSizePolicy(sizePolicy)
        self.BT_cancel.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BT_cancel.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.BT_cancel)

        self.BT_apply = QPushButton(class_tab)
        self.BT_apply.setObjectName(u"BT_apply")
        self.BT_apply.setMaximumSize(QSize(16777215, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/tick.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BT_apply.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.BT_apply)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 20, -1, -1)
        self.F_class_id = QSpinBox(class_tab)
        self.F_class_id.setObjectName(u"F_class_id")
        self.F_class_id.setEnabled(False)
        self.F_class_id.setMaximum(9999)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.F_class_id)

        self.F_class_description = QTextEdit(class_tab)
        self.F_class_description.setObjectName(u"F_class_description")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.F_class_description.sizePolicy().hasHeightForWidth())
        self.F_class_description.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.F_class_description)

        self.F_class_name = QLineEdit(class_tab)
        self.F_class_name.setObjectName(u"F_class_name")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.F_class_name)

        self.label = QLabel(class_tab)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(class_tab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(class_tab)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.CB_view = QComboBox(class_tab)
        self.CB_view.setObjectName(u"CB_view")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.CB_view)

        self.label_4 = QLabel(class_tab)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.BT_add_field = QPushButton(class_tab)
        self.BT_add_field.setObjectName(u"BT_add_field")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.BT_add_field.sizePolicy().hasHeightForWidth())
        self.BT_add_field.setSizePolicy(sizePolicy2)
        icon2 = QIcon()
        icon2.addFile(u":/icons/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BT_add_field.setIcon(icon2)

        self.horizontalLayout.addWidget(self.BT_add_field)

        self.BT_sub_field = QPushButton(class_tab)
        self.BT_sub_field.setObjectName(u"BT_sub_field")
        sizePolicy2.setHeightForWidth(self.BT_sub_field.sizePolicy().hasHeightForWidth())
        self.BT_sub_field.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/icons/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BT_sub_field.setIcon(icon3)

        self.horizontalLayout.addWidget(self.BT_sub_field)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.fields_list = QTreeWidget(class_tab)
        self.fields_list.setObjectName(u"fields_list")
        self.fields_list.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.fields_list.setProperty("showDropIndicator", True)
        self.fields_list.setAlternatingRowColors(True)
        self.fields_list.setIndentation(0)
        self.fields_list.setExpandsOnDoubleClick(True)

        self.verticalLayout.addWidget(self.fields_list)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.BT_add_ref = QPushButton(class_tab)
        self.BT_add_ref.setObjectName(u"BT_add_ref")
        self.BT_add_ref.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.BT_add_ref)

        self.BT_sub_ref = QPushButton(class_tab)
        self.BT_sub_ref.setObjectName(u"BT_sub_ref")
        self.BT_sub_ref.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.BT_sub_ref)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.ref_list = QTreeWidget(class_tab)
        self.ref_list.setObjectName(u"ref_list")
        self.ref_list.setIndentation(0)

        self.verticalLayout.addWidget(self.ref_list)


        self.retranslateUi(class_tab)

        QMetaObject.connectSlotsByName(class_tab)
    # setupUi

    def retranslateUi(self, class_tab):
        class_tab.setWindowTitle(QCoreApplication.translate("class_tab", u"Form", None))
        self.BT_cancel.setText(QCoreApplication.translate("class_tab", u"Cancel changes", None))
        self.BT_apply.setText(QCoreApplication.translate("class_tab", u"Apply changes", None))
        self.label.setText(QCoreApplication.translate("class_tab", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("class_tab", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("class_tab", u"Description", None))
        self.label_4.setText(QCoreApplication.translate("class_tab", u"View", None))
        self.BT_add_field.setText("")
        self.BT_sub_field.setText("")
        ___qtreewidgetitem = self.fields_list.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("class_tab", u"Description", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("class_tab", u"Default", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("class_tab", u"Mandatory", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("class_tab", u"Type", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("class_tab", u"Field", None));
        self.BT_add_ref.setText("")
        self.BT_sub_ref.setText("")
        ___qtreewidgetitem1 = self.ref_list.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("class_tab", u"Description", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("class_tab", u"Classes", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("class_tab", u"Mandatory", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("class_tab", u"Multiple", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("class_tab", u"Reference", None));
    # retranslateUi

