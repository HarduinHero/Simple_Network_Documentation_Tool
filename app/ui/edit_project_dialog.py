# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_project_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QToolButton, QVBoxLayout, QWidget)

class Ui_edit_project_dialog(object):
    def setupUi(self, edit_project_dialog):
        if not edit_project_dialog.objectName():
            edit_project_dialog.setObjectName(u"edit_project_dialog")
        edit_project_dialog.resize(900, 347)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(edit_project_dialog.sizePolicy().hasHeightForWidth())
        edit_project_dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(edit_project_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.GP_edit_project = QGroupBox(edit_project_dialog)
        self.GP_edit_project.setObjectName(u"GP_edit_project")
        self.formLayout_2 = QFormLayout(self.GP_edit_project)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.L_filename = QLabel(self.GP_edit_project)
        self.L_filename.setObjectName(u"L_filename")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.L_filename)

        self.HL_F_filename = QHBoxLayout()
        self.HL_F_filename.setObjectName(u"HL_F_filename")
        self.HL_F_filename.setSizeConstraint(QLayout.SetMinimumSize)
        self.F_filename = QLineEdit(self.GP_edit_project)
        self.F_filename.setObjectName(u"F_filename")

        self.HL_F_filename.addWidget(self.F_filename)

        self.BT_F_filename_browse = QToolButton(self.GP_edit_project)
        self.BT_F_filename_browse.setObjectName(u"BT_F_filename_browse")

        self.HL_F_filename.addWidget(self.BT_F_filename_browse)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.HL_F_filename)

        self.L_name = QLabel(self.GP_edit_project)
        self.L_name.setObjectName(u"L_name")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.L_name)

        self.F_name = QLineEdit(self.GP_edit_project)
        self.F_name.setObjectName(u"F_name")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.F_name)

        self.L_description = QLabel(self.GP_edit_project)
        self.L_description.setObjectName(u"L_description")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.L_description)

        self.F_description = QTextEdit(self.GP_edit_project)
        self.F_description.setObjectName(u"F_description")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.F_description)


        self.verticalLayout.addWidget(self.GP_edit_project)

        self.BT_layout = QHBoxLayout()
        self.BT_layout.setObjectName(u"BT_layout")
        self.BT_cancel = QPushButton(edit_project_dialog)
        self.BT_cancel.setObjectName(u"BT_cancel")

        self.BT_layout.addWidget(self.BT_cancel)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.BT_layout.addItem(self.horizontalSpacer_5)

        self.BT_execute = QPushButton(edit_project_dialog)
        self.BT_execute.setObjectName(u"BT_execute")

        self.BT_layout.addWidget(self.BT_execute)


        self.verticalLayout.addLayout(self.BT_layout)


        self.retranslateUi(edit_project_dialog)

        QMetaObject.connectSlotsByName(edit_project_dialog)
    # setupUi

    def retranslateUi(self, edit_project_dialog):
        edit_project_dialog.setWindowTitle(QCoreApplication.translate("edit_project_dialog", u"Dialog", None))
        self.GP_edit_project.setTitle(QCoreApplication.translate("edit_project_dialog", u"Project", None))
        self.L_filename.setText(QCoreApplication.translate("edit_project_dialog", u"Filename", None))
        self.BT_F_filename_browse.setText(QCoreApplication.translate("edit_project_dialog", u"...", None))
        self.L_name.setText(QCoreApplication.translate("edit_project_dialog", u"Name", None))
        self.L_description.setText(QCoreApplication.translate("edit_project_dialog", u"Description", None))
        self.BT_cancel.setText(QCoreApplication.translate("edit_project_dialog", u"Cancel", None))
        self.BT_execute.setText(QCoreApplication.translate("edit_project_dialog", u"Execute", None))
    # retranslateUi

