import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import (
    QStandardItem,
    QStandardItemModel
)
from PyQt5.QtCore import (
    QSettings,
    QThread,
    pyqtSignal)
from .forms import (
    mainwindow,
    connections,
    connection
)
import psycopg2

settings = None
connection_state = None

_LIST_TABLES = ("select relname as Tabelas "
                "from pg_class "
                "where relkind='r' and "
                "relname !~ '^(pg_|sql_)' "
                "order by relname asc")

_CONNECTIONS = 'connections'
_LOFILE = 'lastopen'


def splitquerybyposition(query, position):
    querysliced = [query[:position], query[position:]]
    return querysliced[0].split(';')[-1] + querysliced[1].split(';')[0]


class BaseWindow:
    def error_message(self, message, details=None):
        msg = QtWidgets.QMessageBox(parent=self)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(message)
        msg.setInformativeText(details)
        msg.setWindowTitle('Presta atenção, brother...')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.show()
    
    def alert_message(self, message, details=None):
        msg = QtWidgets.QMessageBox(parent=self)
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(message)
        msg.setInformativeText(details)
        msg.setWindowTitle('Deu ruim, fiel')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.show()

    def ask_message(self, question):
        return QtWidgets.QMessageBox.question(
            self,
            'Escolha sabiamente...',
            question,
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )


class Connection(QtWidgets.QDialog, BaseWindow):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.ui = connection.Ui_connection()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accepted)

    def validate(self):
        field = None
        if not self.ui.name.text():
            field = self.ui.name
        elif not self.ui.host.text():
            field = self.ui.host
        elif not self.ui.database.text():
            field = self.ui.database
        elif not self.ui.username.text():
            field = self.ui.username
        elif not self.ui.password.text():
            field = self.ui.password
        
        if field:
            self.error_message(
                'Ô chapa...'
                '\nTodos os campos são obrigatórios!'
                '\nTá de sacanagem?'
                '\nInforme %s!' % field.placeholderText())
            field.setFocus()
            return False
        return True
    
    def accepted(self):
        if not self.validate():
            return

        ui = self.ui
        parameters = {
            'name': ui.name.text(),
            'host': ui.host.text(),
            'database': ui.database.text(),
            'username': ui.username.text(),
            'password': ui.password.text(),
            'port': ui.port.value()
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
        super().__init__(parent=parent)
        self.ui = connections.Ui_connections()
        self.ui.setupUi(self)
        self.read_connection_settings()
        self.ui.add.clicked.connect(self.new_connection)
        self.ui.connect.clicked.connect(self.connect)
        self.ui.pushButton.clicked.connect(self.delete)
    
    def new_connection(self):
        new_connection = Connection(self)
        new_connection.show()
    
    def read_connection_settings(self):
        settings = QSettings(parent=self)
        stored_connections = settings.value(_CONNECTIONS)
        model = QStandardItemModel()
        if stored_connections:
            for nconnection, connection in enumerate(stored_connections):
                model.setItem(nconnection, 0, QStandardItem(connection['name']))
        self.ui.connectionslist.setModel(model)
    
    def _selected_connection_name(self, message):
        indexes = self.ui.connectionslist.selectedIndexes()
        if not indexes:
            self.alert_message(message)
            return
        return indexes[0].data()

    def _connection_parameters(self, connection_name):
        return next(filter(
            lambda conn: connection_name == conn['name'],
            settings.value(_CONNECTIONS)
        ))

    def delete(self):
        connection_name = self._selected_connection_name(
            'Migue, não posso apagar se você não me disser qual, né?')
        if not connection_name:
            return

        resp = self.ask_message(
            'Está certo disso?\nValendo Hum Milhão de Reais?'
            '\nPosso apagar a conexão %s?' % connection_name)
        if resp == QtWidgets.QMessageBox.Yes:
            connection_parameters = self._connection_parameters(
                connection_name
            )
            all_parameters = settings.value(_CONNECTIONS)
            all_parameters.remove(connection_parameters)
            settings.setValue(_CONNECTIONS, all_parameters)
            self.read_connection_settings()
    
    def connect(self):
        connection_name = self._selected_connection_name(
            'Não consigo adivinhar que conexão você quer usar, informe uma, ô pá!')
        if not connection_name:
            return

        global connection_state
        connection_parameters = self._connection_parameters(connection_name)
        try:
            connection_state = psycopg2.connect(
                database=connection_parameters['database'],
                user=connection_parameters['username'],
                password=connection_parameters['password'],
                host=connection_parameters['host'],
                port=connection_parameters['port']
            )
            self.close()
            self.parent().listtables()
        except Exception as error:
            self.error_message('Deu ruim na conexão', str(error))


class MainWindow(QtWidgets.QMainWindow, BaseWindow):
    def __init__(self, _settings):
        global settings
        super().__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.executequery.clicked.connect(self.execute_query)
        self.ui.actionConex_es.triggered.connect(self.show_connections)
        self.ui.actionAbrir.triggered.connect(self.open)
        self.ui.actionSalvar.triggered.connect(self.save)
        self.ui.actionSalvar_como.triggered.connect(self.saveas)
        self.opened_file = None
        settings = _settings
        self.preload_last_opened()
        self.show_connections()
    
    def preload_last_opened(self):
        if settings.value(_LOFILE):
            try:
                self.opened_file = settings.value(_LOFILE)
                self._readfile()
                self.update_window_title()
            except:
                self.opened_file = None

    def _update_last_opened_setting(self):
        settings.setValue(_LOFILE, self.opened_file)
    
    def update_window_title(self):
        self.setWindowTitle("kquery - %s" % self.opened_file)

    def open(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Abrir um super arquivo SQL!",
            filter="*.sql")

        if filename:
            self.opened_file = filename
            self._readfile()
            self.update_window_title()
            self._update_last_opened_setting()
    
    def _readfile(self):
        with open(self.opened_file, 'r') as file:
            self.ui.queryeditor.setPlainText(
                file.read()
            )

    def _writefile(self):
        with open(self.opened_file, 'w+') as file:
            file.write(
                self.ui.queryeditor.toPlainText()
            )

    def save(self):
        if not self.opened_file:
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(
                self,
                "Salvar o seu arquivinho bonitinho, fofo!",
                filter="*.sql")
            self.opened_file = filename
        
        if self.opened_file:
            self._writefile()
            self.update_window_title()
            self._update_last_opened_setting()

    def saveas(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Vamos então salvar um novo, né?",
            filter="*.sql")
        
        if filename:
            self.opened_file = filename
            self._writefile()
            self.update_window_title()
            self._update_last_opened_setting()

    def listtables(self):
        with connection_state.cursor() as cursor:
            executor = QueryThread(_LIST_TABLES, cursor)
            executor.query_data.connect(self._set_tables_model)
            executor.run()

    def show_connections(self):
        connections_window = Connections(self)
        connections_window.show()

    def execute_query(self):
        with connection_state.cursor() as cursor:
            querys = self.ui.queryeditor.toPlainText()
            position = self.ui.queryeditor.textCursor().position()
            query = splitquerybyposition(querys, position)
            executor = QueryThread(query, cursor)
            executor.query_data.connect(self._set_tableresults_model)
            executor.run()

    def _set_tableresults_model(self, model):
        self.ui.tableresults.setModel(model)
    
    def _set_tables_model(self, model):
        self.ui.tables.setModel(model)


class QueryThread(QThread):
    # Query Thread Execution
    # QT developers discourage QThread subclassing, planing to read
    # and think on that later
    query_data = pyqtSignal(object)

    def __init__(self, query, cursor):
        super().__init__()
        self.cursor = cursor
        self.query = query

    def run(self):
        try:
            self.cursor.execute(self.query)
            headers = [item.name for item in self.cursor.description]
            result = self.cursor.fetchall()
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(headers)
            model.setRowCount(len(result))
            for nline, line in enumerate(result):
                for ncolumn, column in enumerate(line):
                    model.setItem(nline, ncolumn,QStandardItem(str(column)))
        except Exception as error:
            connection_state.rollback()
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(["Deu ruim!"])
            model.setRowCount(1)
            model.setItem(0, 0, QStandardItem(str(error)))

        self.query_data.emit(model)
