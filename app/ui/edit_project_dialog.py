# Form implementation generated from reading ui file './app/ui/edit_project_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_edit_project_dialog(object):
    def setupUi(self, edit_project_dialog):
        edit_project_dialog.setObjectName("edit_project_dialog")
        edit_project_dialog.resize(900, 347)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(edit_project_dialog.sizePolicy().hasHeightForWidth())
        edit_project_dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(edit_project_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.GP_edit_project = QtWidgets.QGroupBox(parent=edit_project_dialog)
        self.GP_edit_project.setObjectName("GP_edit_project")
        self.formLayout_2 = QtWidgets.QFormLayout(self.GP_edit_project)
        self.formLayout_2.setObjectName("formLayout_2")
        self.L_filename = QtWidgets.QLabel(parent=self.GP_edit_project)
        self.L_filename.setObjectName("L_filename")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.L_filename)
        self.HL_F_filename = QtWidgets.QHBoxLayout()
        self.HL_F_filename.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.HL_F_filename.setObjectName("HL_F_filename")
        self.F_filename = QtWidgets.QLineEdit(parent=self.GP_edit_project)
        self.F_filename.setObjectName("F_filename")
        self.HL_F_filename.addWidget(self.F_filename)
        self.BT_F_filename_browse = QtWidgets.QToolButton(parent=self.GP_edit_project)
        self.BT_F_filename_browse.setObjectName("BT_F_filename_browse")
        self.HL_F_filename.addWidget(self.BT_F_filename_browse)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.HL_F_filename)
        self.L_name = QtWidgets.QLabel(parent=self.GP_edit_project)
        self.L_name.setObjectName("L_name")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.L_name)
        self.F_name = QtWidgets.QLineEdit(parent=self.GP_edit_project)
        self.F_name.setObjectName("F_name")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.F_name)
        self.L_description = QtWidgets.QLabel(parent=self.GP_edit_project)
        self.L_description.setObjectName("L_description")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.L_description)
        self.F_description = QtWidgets.QTextEdit(parent=self.GP_edit_project)
        self.F_description.setObjectName("F_description")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.F_description)
        self.verticalLayout.addWidget(self.GP_edit_project)
        self.BT_layout = QtWidgets.QHBoxLayout()
        self.BT_layout.setObjectName("BT_layout")
        self.BT_cancel = QtWidgets.QPushButton(parent=edit_project_dialog)
        self.BT_cancel.setObjectName("BT_cancel")
        self.BT_layout.addWidget(self.BT_cancel)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.BT_layout.addItem(spacerItem)
        self.BT_execute = QtWidgets.QPushButton(parent=edit_project_dialog)
        self.BT_execute.setObjectName("BT_execute")
        self.BT_layout.addWidget(self.BT_execute)
        self.verticalLayout.addLayout(self.BT_layout)

        self.retranslateUi(edit_project_dialog)
        QtCore.QMetaObject.connectSlotsByName(edit_project_dialog)

    def retranslateUi(self, edit_project_dialog):
        _translate = QtCore.QCoreApplication.translate
        edit_project_dialog.setWindowTitle(_translate("edit_project_dialog", "Dialog"))
        self.GP_edit_project.setTitle(_translate("edit_project_dialog", "Project"))
        self.L_filename.setText(_translate("edit_project_dialog", "Filename"))
        self.BT_F_filename_browse.setText(_translate("edit_project_dialog", "..."))
        self.L_name.setText(_translate("edit_project_dialog", "Name"))
        self.L_description.setText(_translate("edit_project_dialog", "Description"))
        self.BT_cancel.setText(_translate("edit_project_dialog", "Cancel"))
        self.BT_execute.setText(_translate("edit_project_dialog", "Execute"))
