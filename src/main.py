from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMenuBar, QMenu, QWidget,
    QVBoxLayout, QLabel, QStatusBar, QFrame, QListWidget,
    QHBoxLayout, QFileDialog, QMessageBox
)
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt, QSize
import sys
from PySide6.QtCore import QTimer



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("📌DeiCode-App")
        
        self.setMinimumSize(1024, 600)
        
        # Usamos showMaximized para que se vea la barra de título con la "X"
        self.showMaximized()


        # Mensaje que parpadea en la barra de estado
        self.blink_message = "Desarrollado con amor ❤️ por DeiCode | shgcifrado@gmail.com"
        self.blink_state = True  # Estado para alternar el mensaje

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Crear un temporizador para hacer parpadear el mensaje
        self.blink_timer = QTimer(self)
        self.blink_timer.timeout.connect(self.toggle_blink_message)
        self.blink_timer.start(1000)  # Cambia el mensaje cada 1 segundo


        self.setStyleSheet("""
            QMainWindow {
                background-color: #1E1E1E;
            }
            QMenuBar {
                background-color: #252526;
                color: #CCCCCC;
            }
            QMenuBar::item {
                background-color: transparent;
                padding: 5px 15px;
            }
            QMenuBar::item:selected {
                background-color: #007ACC;
            }
            /* Menú principal dei */
            QMenu {
                background-color: #484848 !important; ;
                color: #CCCCCC;
            }
            QMenu::item {
                background-color: transparent;
                padding: 5px 20px;
            }
            QMenu::item:selected {
                background-color: #007ACC;
            }
            /* Submenús */
            QMenu QMenu {
                background-color: #007ACC;  /* Color de fondo para los submenús */
                color: #E6E6E6;
            }
            QMenu QMenu::item {
                background-color: transparent;
                padding: 5px 20px;
            }
            QMenu QMenu::item:selected {
                background-color: #007ACC;
            }
            QStatusBar {
                background-color: #252526;
                color: #CCCCCC;
            }
            QListWidget {
                background-color: #252526;
                color: #CCCCCC;
                border: none;
            }
            QListWidget::item:selected {
                background-color: #007ACC;
            }
        """)


        # Menú
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        menu_file = menu_bar.addMenu("File")
        action_open = QAction("Open", self)
        action_open.setShortcut("Ctrl+O")
        action_open.triggered.connect(self.open_file)

        action_save = QAction("Save", self)
        action_save.setShortcut("Ctrl+S")
        action_save.triggered.connect(self.save_file)

        action_exit = QAction("Exit", self)
        action_exit.setShortcut("Ctrl+Q")
        action_exit.triggered.connect(self.close)

        menu_file.addAction(action_open)
        menu_file.addAction(action_save)
        menu_file.addSeparator()
        menu_file.addAction(action_exit)

        menu_settings = menu_bar.addMenu("Settings")
        action_preferences = QAction("Preferences", self)
        menu_settings.addAction(action_preferences)

        menu_about = menu_bar.addMenu("About")
        action_about = QAction("About this App", self)
        action_about.triggered.connect(self.show_about_dialog)
        menu_about.addAction(action_about)

        # Layout principal
        main_layout = QHBoxLayout()

        # Sidebar
        self.sidebar = QListWidget()
        self.sidebar.addItem("Dashboard")
        self.sidebar.addItem("Projects")
        self.sidebar.addItem("Settings")
        self.sidebar.setMaximumWidth(200)
        self.sidebar.itemClicked.connect(self.handle_sidebar_click)

        # Contenedor principal
        self.content_area = QLabel("Main Content Area", self)
        self.content_area.setAlignment(Qt.AlignCenter)
        self.content_area.setStyleSheet("color: white; font-size: 24px;")

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.content_area, 1)

        # Widget central
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.status_bar.showMessage("Ready")  # Muestra un mensaje inicial


    def handle_sidebar_click(self, item):
        text = item.text()
        if text == "Dashboard":
            self.content_area.setText("Has seleccionado Dashboard")
        elif text == "Projects":
            self.content_area.setText("Has seleccionado Projects")
        elif text == "Settings":
            self.content_area.setText("Has seleccionado Settings")

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if file_name:
            self.statusBar().showMessage(f"Abierto: {file_name}")

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*)")
        if file_name:
            self.statusBar().showMessage(f"Guardado: {file_name}")

    def show_about_dialog(self):
        QMessageBox.about(self, "About",
                          "Desarrollado con amor ❤️ por DeiCode | shgcifrado@gmail.com.\nEstilo VSCode.")
        


    def toggle_blink_message(self):
        if self.blink_state:
            self.status_bar.showMessage(self.blink_message)
        else:
            self.status_bar.clearMessage()  # Borra el mensaje para el efecto de parpadeo
        self.blink_state = not self.blink_state  # Alternar estado


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
