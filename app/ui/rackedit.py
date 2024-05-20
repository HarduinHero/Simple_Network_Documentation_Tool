# Form implementation generated from reading ui file './app/ui/rackedit.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_rack_edit(object):
    def setupUi(self, rack_edit):
        rack_edit.setObjectName("rack_edit")
        rack_edit.resize(714, 533)
        self.verticalLayout = QtWidgets.QVBoxLayout(rack_edit)
        self.verticalLayout.setObjectName("verticalLayout")
        self.l_rack_edit_title = QtWidgets.QLabel(parent=rack_edit)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.l_rack_edit_title.setFont(font)
        self.l_rack_edit_title.setObjectName("l_rack_edit_title")
        self.verticalLayout.addWidget(self.l_rack_edit_title)
        self.line = QtWidgets.QFrame(parent=rack_edit)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.form = QtWidgets.QFormLayout()
        self.form.setObjectName("form")
        self.l_rack_id = QtWidgets.QLabel(parent=rack_edit)
        self.l_rack_id.setObjectName("l_rack_id")
        self.form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l_rack_id)
        self.i_rack_id = QtWidgets.QSpinBox(parent=rack_edit)
        self.i_rack_id.setEnabled(False)
        self.i_rack_id.setObjectName("i_rack_id")
        self.form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.i_rack_id)
        self.l_label_1 = QtWidgets.QLabel(parent=rack_edit)
        self.l_label_1.setObjectName("l_label_1")
        self.form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l_label_1)
        self.i_label_1 = QtWidgets.QLineEdit(parent=rack_edit)
        self.i_label_1.setObjectName("i_label_1")
        self.form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.i_label_1)
        self.l_label_2 = QtWidgets.QLabel(parent=rack_edit)
        self.l_label_2.setObjectName("l_label_2")
        self.form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l_label_2)
        self.i_label_2 = QtWidgets.QLineEdit(parent=rack_edit)
        self.i_label_2.setObjectName("i_label_2")
        self.form.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.i_label_2)
        self.l_height = QtWidgets.QLabel(parent=rack_edit)
        self.l_height.setObjectName("l_height")
        self.form.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l_height)
        self.i_height = QtWidgets.QSpinBox(parent=rack_edit)
        self.i_height.setObjectName("i_height")
        self.form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.i_height)
        self.l_description = QtWidgets.QLabel(parent=rack_edit)
        self.l_description.setObjectName("l_description")
        self.form.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l_description)
        self.i_description = QtWidgets.QTextEdit(parent=rack_edit)
        self.i_description.setObjectName("i_description")
        self.form.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.i_description)
        self.verticalLayout.addLayout(self.form)
        self.rack_actions = QtWidgets.QHBoxLayout()
        self.rack_actions.setObjectName("rack_actions")
        self.bt_cancel = QtWidgets.QPushButton(parent=rack_edit)
        self.bt_cancel.setObjectName("bt_cancel")
        self.rack_actions.addWidget(self.bt_cancel)
        self.bt_save = QtWidgets.QPushButton(parent=rack_edit)
        self.bt_save.setObjectName("bt_save")
        self.rack_actions.addWidget(self.bt_save)
        self.verticalLayout.addLayout(self.rack_actions)
        self.l_rack_id.setBuddy(self.i_rack_id)
        self.l_label_1.setBuddy(self.i_label_1)
        self.l_label_2.setBuddy(self.i_label_2)
        self.l_height.setBuddy(self.i_height)
        self.l_description.setBuddy(self.i_description)

        self.retranslateUi(rack_edit)
        QtCore.QMetaObject.connectSlotsByName(rack_edit)

    def retranslateUi(self, rack_edit):
        _translate = QtCore.QCoreApplication.translate
        rack_edit.setWindowTitle(_translate("rack_edit", "Frame"))
        self.l_rack_edit_title.setText(_translate("rack_edit", "Rack edit :"))
        self.l_rack_id.setText(_translate("rack_edit", "Rack ID"))
        self.l_label_1.setText(_translate("rack_edit", "Label 1"))
        self.l_label_2.setText(_translate("rack_edit", "Label 2"))
        self.l_height.setText(_translate("rack_edit", "Height (number of Us)"))
        self.l_description.setText(_translate("rack_edit", "Description"))
        self.bt_cancel.setText(_translate("rack_edit", "Cancel"))
        self.bt_save.setText(_translate("rack_edit", "Valider"))