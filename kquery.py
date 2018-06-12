import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QSett
from PyQt5.QtCore import QSettings
import mainwindow
import connections
import psycopg2


connection = None
_LIST_TABLES = ("select relname "
                "from pg_class "
                "where relkind='r' and "
                "relname !~ '^(pg_|sql_)' "
                "order by relname asc")


def listtables():
    cursor = connection.cursor()
    cursor.execute(_LIST_TABLES)
    tables = cursor.fetchall()
    return [item[0] for item in tables]


def splitquerybyposition(query, position):
    querysliced = [query[:position], query[position:]]
    return querysliced[0].split(";")[-1] + querysliced[1].split(';')[0]


class Connections(QtWidgets.QDialog):
    def __init__(self, parent):
        super(Connections, self).__init__(parent=parent)
        self.ui = connections.Ui_connections()
        self.ui.setupUi(self)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.executequery.clicked.connect(self.execute_query)
        self.ui.actionConex_es.triggered.connect(self.show_connections)
        model = QStandardItemModel()
        #for ntable, table in enumerate(listtables()):
        #    model.setItem(ntable, 0, QStandardItem(str(table)))
        
        self.ui.tables.setModel(model)

    def show_connections(self):
        print("fui chamado")
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

#connect()

app = QtWidgets.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
