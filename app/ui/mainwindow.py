# Form implementation generated from reading ui file './app/ui/mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(970, 600)
        main_window.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        main_window.setWindowTitle("SNDT : Simple Network Documentation Tool")
        main_window.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.central_widget = QtWidgets.QWidget(parent=main_window)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.central_splitter = QtWidgets.QSplitter(parent=self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_splitter.sizePolicy().hasHeightForWidth())
        self.central_splitter.setSizePolicy(sizePolicy)
        self.central_splitter.setAutoFillBackground(False)
        self.central_splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.central_splitter.setOpaqueResize(True)
        self.central_splitter.setHandleWidth(10)
        self.central_splitter.setChildrenCollapsible(True)
        self.central_splitter.setObjectName("central_splitter")
        self.nav_tree_frame = QtWidgets.QFrame(parent=self.central_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nav_tree_frame.sizePolicy().hasHeightForWidth())
        self.nav_tree_frame.setSizePolicy(sizePolicy)
        self.nav_tree_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nav_tree_frame.setBaseSize(QtCore.QSize(0, 0))
        self.nav_tree_frame.setAcceptDrops(False)
        self.nav_tree_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.nav_tree_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.nav_tree_frame.setObjectName("nav_tree_frame")
        self.nav_tree_frame_layout = QtWidgets.QVBoxLayout(self.nav_tree_frame)
        self.nav_tree_frame_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.nav_tree_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.nav_tree_frame_layout.setObjectName("nav_tree_frame_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.F_nav_tree_filter = QtWidgets.QLineEdit(parent=self.nav_tree_frame)
        self.F_nav_tree_filter.setInputMask("")
        self.F_nav_tree_filter.setText("")
        self.F_nav_tree_filter.setDragEnabled(False)
        self.F_nav_tree_filter.setObjectName("F_nav_tree_filter")
        self.horizontalLayout.addWidget(self.F_nav_tree_filter)
        self.nav_tree_frame_layout.addLayout(self.horizontalLayout)
        self.treeWidget = QtWidgets.QTreeWidget(parent=self.nav_tree_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.nav_tree_frame_layout.addWidget(self.treeWidget)
        self.editing_frame = QtWidgets.QFrame(parent=self.central_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editing_frame.sizePolicy().hasHeightForWidth())
        self.editing_frame.setSizePolicy(sizePolicy)
        self.editing_frame.setBaseSize(QtCore.QSize(0, 0))
        self.editing_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.editing_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.editing_frame.setObjectName("editing_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.editing_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addWidget(self.central_splitter, 0, 0, 1, 1)
        main_window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(parent=main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 970, 21))
        self.menubar.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(parent=self.menubar)
        self.menu_file.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.menu_file.setObjectName("menu_file")
        self.menu_load_example_project = QtWidgets.QMenu(parent=self.menu_file)
        self.menu_load_example_project.setObjectName("menu_load_example_project")
        self.menu_help = QtWidgets.QMenu(parent=self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_display = QtWidgets.QMenu(parent=self.menubar)
        self.menu_display.setObjectName("menu_display")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=main_window)
        self.statusbar.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.action_user_guide = QtGui.QAction(parent=main_window)
        self.action_user_guide.setObjectName("action_user_guide")
        self.action_about = QtGui.QAction(parent=main_window)
        self.action_about.setObjectName("action_about")
        self.action_new_project = QtGui.QAction(parent=main_window)
        self.action_new_project.setObjectName("action_new_project")
        self.action_open_project = QtGui.QAction(parent=main_window)
        self.action_open_project.setObjectName("action_open_project")
        self.action_settings = QtGui.QAction(parent=main_window)
        self.action_settings.setObjectName("action_settings")
        self.action_save = QtGui.QAction(parent=main_window)
        self.action_save.setObjectName("action_save")
        self.menu_file.addAction(self.action_new_project)
        self.menu_file.addAction(self.action_open_project)
        self.menu_file.addAction(self.menu_load_example_project.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_save)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_settings)
        self.menu_help.addAction(self.action_user_guide)
        self.menu_help.addAction(self.action_about)
        self.menu_display.addSeparator()
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_display.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        self.F_nav_tree_filter.setPlaceholderText(_translate("main_window", "Filter"))
        self.treeWidget.headerItem().setText(0, _translate("main_window", "Object"))
        self.treeWidget.headerItem().setText(1, _translate("main_window", "Type"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("main_window", "Test"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("main_window", "Project"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.menu_file.setTitle(_translate("main_window", "File"))
        self.menu_load_example_project.setTitle(_translate("main_window", "Load example project"))
        self.menu_help.setTitle(_translate("main_window", "Help"))
        self.menu_display.setTitle(_translate("main_window", "Display"))
        self.action_user_guide.setText(_translate("main_window", "User guide"))
        self.action_about.setText(_translate("main_window", "About SNDT"))
        self.action_new_project.setText(_translate("main_window", "New project"))
        self.action_open_project.setText(_translate("main_window", "Open project"))
        self.action_settings.setText(_translate("main_window", "Settings"))
        self.action_save.setText(_translate("main_window", "Save"))
