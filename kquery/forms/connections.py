# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './kquery/forms/connections.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_connections(object):
    def setupUi(self, connections):
        connections.setObjectName("connections")
        connections.resize(368, 246)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(connections.sizePolicy().hasHeightForWidth())
        connections.setSizePolicy(sizePolicy)
        connections.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(connections)
        self.verticalLayout.setObjectName("verticalLayout")
        self.connectionslist = QtWidgets.QListView(connections)
        self.connectionslist.setObjectName("connectionslist")
        self.verticalLayout.addWidget(self.connectionslist)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add = QtWidgets.QPushButton(connections)
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)
        self.pushButton = QtWidgets.QPushButton(connections)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.connect = QtWidgets.QPushButton(connections)
        self.connect.setObjectName("connect")
        self.horizontalLayout.addWidget(self.connect)
        self.cancel = QtWidgets.QPushButton(connections)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(connections)
        self.cancel.clicked.connect(connections.close)
        QtCore.QMetaObject.connectSlotsByName(connections)

    def retranslateUi(self, connections):
        _translate = QtCore.QCoreApplication.translate
        connections.setWindowTitle(_translate("connections", "Conexões"))
        self.add.setText(_translate("connections", "Incluir"))
        self.pushButton.setText(_translate("connections", "Excluir"))
        self.connect.setText(_translate("connections", "Connectar"))
        self.cancel.setText(_translate("connections", "Cancelar"))

