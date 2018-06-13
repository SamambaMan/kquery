# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './kquery/forms/connection.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_connection(object):
    def setupUi(self, connection):
        connection.setObjectName("connection")
        connection.resize(193, 236)
        connection.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(connection)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLineEdit(connection)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.host = QtWidgets.QLineEdit(connection)
        self.host.setObjectName("host")
        self.verticalLayout.addWidget(self.host)
        self.database = QtWidgets.QLineEdit(connection)
        self.database.setObjectName("database")
        self.verticalLayout.addWidget(self.database)
        self.username = QtWidgets.QLineEdit(connection)
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.password = QtWidgets.QLineEdit(connection)
        self.password.setInputMask("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.port = QtWidgets.QSpinBox(connection)
        self.port.setMinimum(1)
        self.port.setMaximum(65000)
        self.port.setProperty("value", 3306)
        self.port.setObjectName("port")
        self.verticalLayout.addWidget(self.port)
        self.buttonBox = QtWidgets.QDialogButtonBox(connection)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(connection)
        self.buttonBox.rejected.connect(connection.close)
        QtCore.QMetaObject.connectSlotsByName(connection)

    def retranslateUi(self, connection):
        _translate = QtCore.QCoreApplication.translate
        connection.setWindowTitle(_translate("connection", "Conexão"))
        self.name.setPlaceholderText(_translate("connection", "Nome da Conexão"))
        self.host.setPlaceholderText(_translate("connection", "Host"))
        self.database.setPlaceholderText(_translate("connection", "Base de Dados"))
        self.username.setPlaceholderText(_translate("connection", "Usuário"))
        self.password.setPlaceholderText(_translate("connection", "Senha"))
        self.port.setToolTip(_translate("connection", "Porta TCP"))

