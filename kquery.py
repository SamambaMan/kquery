import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import QSettings
import mainwindow
import connections
import connection
import psycopg2


connection_state = None
_LIST_TABLES = ("select relname "
                "from pg_class "
                "where relkind='r' and "
                "relname !~ '^(pg_|sql_)' "
                "order by relname asc")

_CONNECTIONS = "connections"


def splitquerybyposition(query, position):
    querysliced = [query[:position], query[position:]]
    return querysliced[0].split(";")[-1] + querysliced[1].split(';')[0]


class BaseWindow:
    def errorMessage(self, message, details):
        msg = QtWidgets.QMessageBox(parent=self)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(message)
        msg.setInformativeText(details)
        msg.setWindowTitle("Presta atenção, brother...")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.show()
    
    def alertMessage(self, message, details=None):
        msg = QtWidgets.QMessageBox(parent=self)
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(message)
        msg.setInformativeText(details)
        msg.setWindowTitle("Deu ruim, fiel")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.show()


class Connection(QtWidgets.QDialog, BaseWindow):
    def __init__(self, parent):
        super(Connection, self).__init__(parent=parent)
        self.ui = connection.Ui_connection()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accepted)
    
    def accepted(self):
        ui = self.ui
        parameters = {
            "name": ui.name.text(),
            "host": ui.host.text(),
            "database": ui.database.text(),
            "username": ui.username.text(),
            "password": ui.password.text(),
            "port": ui.port.value()
        }

        connections = settings.value(_CONNECTIONS)
        if not connections:
            connections = []
        connections += [parameters]

        settings.setValue(_CONNECTIONS, connections)
        self.close()
        self.parent().read_connection_settings()


class Connections(QtWidgets.QDialog, BaseWindow):
    def __init__(self, parent):
        super(Connections, self).__init__(parent=parent)
        self.ui = connections.Ui_connections()
        self.ui.setupUi(self)
        self.read_connection_settings()
        self.ui.add.clicked.connect(self.new_connection)
        self.ui.connect.clicked.connect(self.connect)
    
    def new_connection(self):
        new_connection = Connection(self)
        new_connection.show()
    
    def read_connection_settings(self):
        settings = QSettings(parent=self)
        stored_connections = settings.value(_CONNECTIONS)
        if stored_connections:
            model = QStandardItemModel()
            for nconnection, connection in enumerate(stored_connections):
                model.setItem(nconnection, 0, QStandardItem(connection['name']))
            self.ui.connectionslist.setModel(model)
    
    def connect(self):
        indexes = self.ui.connectionslist.selectedIndexes()
        if not indexes:
            self.alertMessage("Não consigo adivinhar que conexão você quer usar, informe uma, ô pá!")
            return

        connection_name = indexes[0].data()

        global connection_state
        connection_parameters = next(filter(
            lambda conn: connection_name == conn['name'],
            settings.value(_CONNECTIONS)
        ))
        try:
            connection_state = psycopg2.connect(
                database=connection_parameters["database"],
                user=connection_parameters["username"],
                password=connection_parameters["password"],
                host=connection_parameters["host"],
                port=connection_parameters["port"]
            )
            self.close()
            self.parent().listtables()
        except Exception as error:
            self.errorMessage("Deu ruim na conexão", str(error))


class MainWindow(QtWidgets.QMainWindow, BaseWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.executequery.clicked.connect(self.execute_query)
        self.ui.actionConex_es.triggered.connect(self.show_connections)

    def listtables(self):
        cursor = connection_state.cursor()
        cursor.execute(_LIST_TABLES)
        tables = cursor.fetchall()
        tables = [item[0] for item in tables]
        model = QStandardItemModel()
        for ntable, table in enumerate(tables):
            model.setItem(ntable, 0, QStandardItem(str(table)))
        
        self.ui.tables.setModel(model)

    def show_connections(self):
        connections_window = Connections(self)
        connections_window.show()

    def execute_query(self):
        with connection_state.cursor() as cursor:
            querys = self.ui.queryeditor.toPlainText()
            position = self.ui.queryeditor.textCursor().position()
            query = splitquerybyposition(querys, position)
            query = query + " limit 10"
            cursor.execute(query)
            headers = [item.name for item in cursor.description]
            result = cursor.fetchall()
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(headers)
            model.setRowCount(len(result))
            for nline, line in enumerate(result):
                for ncolumn, column in enumerate(line):
                    model.setItem(nline, ncolumn,QStandardItem(str(column)))
  
            self.ui.tableresults.setModel(model)


app = QtWidgets.QApplication(sys.argv)
app.setOrganizationName("kquery")
app.setOrganizationDomain("github.com/samambaman")

settings = QSettings(app)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
