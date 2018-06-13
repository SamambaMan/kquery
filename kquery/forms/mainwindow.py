# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './kquery/forms/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1039, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tables = QtWidgets.QTreeView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tables.sizePolicy().hasHeightForWidth())
        self.tables.setSizePolicy(sizePolicy)
        self.tables.setObjectName("tables")
        self.horizontalLayout_2.addWidget(self.tables)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.queryeditor = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.queryeditor.setObjectName("queryeditor")
        self.verticalLayout.addWidget(self.queryeditor)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.executequery = QtWidgets.QPushButton(self.centralwidget)
        self.executequery.setObjectName("executequery")
        self.horizontalLayout.addWidget(self.executequery)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableresults = QtWidgets.QTableView(self.centralwidget)
        self.tableresults.setObjectName("tableresults")
        self.verticalLayout.addWidget(self.tableresults)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1039, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionConex_es = QtWidgets.QAction(MainWindow)
        self.actionConex_es.setObjectName("actionConex_es")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionSalvar_como = QtWidgets.QAction(MainWindow)
        self.actionSalvar_como.setObjectName("actionSalvar_como")
        self.menuFile.addAction(self.actionConex_es)
        self.menuFile.addAction(self.actionAbrir)
        self.menuFile.addAction(self.actionSalvar)
        self.menuFile.addAction(self.actionSalvar_como)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "kquery"))
        self.executequery.setText(_translate("MainWindow", "Executar"))
        self.executequery.setShortcut(_translate("MainWindow", "Ctrl+Return"))
        self.menuFile.setTitle(_translate("MainWindow", "Ar&quivo"))
        self.actionQuit.setText(_translate("MainWindow", "&Sair"))
        self.actionConex_es.setText(_translate("MainWindow", "&Conexões"))
        self.actionAbrir.setText(_translate("MainWindow", "&Abrir"))
        self.actionSalvar.setText(_translate("MainWindow", "Sa&lvar"))
        self.actionSalvar_como.setText(_translate("MainWindow", "Sal&var como..."))

