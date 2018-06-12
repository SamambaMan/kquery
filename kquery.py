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


def listtables():
    cursor = connection.cursor()
    cursor.execute(_LIST_TABLES)
    tables = cursor.fetchall()
    return [item[0] for item in tables]


def splitquerybyposition(query, position):
    querysliced = [query[:position], query[position:]]
    return querysliced[0].split(";")[-1] + querysliced[1].split(';')[0]


class Connection(QtWidgets.QDialog):
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


class Connections(QtWidgets.QDialog):
    def __init__(self, parent):
        super(Connections, self).__init__(parent=parent)
        self.ui = connections.Ui_connections()
        self.ui.setupUi(self)
        self.read_connection_settings()
        self.ui.add.clicked.connect(self.new_connection)
    
    def new_connection(self):
        new_connection = Connection(self)
        new_connection.show()
    
    def read_connection_settings(self):
        settings = QSettings(parent=self)
        stored_connections = settings.value(_CONNECTIONS)
        if stored_connections:
            model = QStandardItemModel()
            for nconnection, connection in enumerate(stored_connections):
                import ipdb; ipdb.set_trace()
                model.setItem(nconnection, 0, QStandardItem(connection['name']))
                model.setItem(nconnection, 1, QStandardItem(connection['username']))
                model.setItem(nconnection, 2, QStandardItem(connection['host']))
            self.ui.connectionslist.setModel(model)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.executequery.clicked.connect(self.execute_query)
        self.ui.actionConex_es.triggered.connect(self.show_connections)

        # model = QStandardItemModel()
        # for ntable, table in enumerate(listtables()):
        #     model.setItem(ntable, 0, QStandardItem(str(table)))
        
        # self.ui.tables.setModel(model)

    def show_connections(self):
        connections_window = Connections(self)
        connections_window.show()

    def execute_query(self):
        with connection.cursor() as cursor:
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
settings.setValue(_CONNECTIONS, [])

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
