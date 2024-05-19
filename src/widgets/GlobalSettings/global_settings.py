import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
sys.path.append('src/widgets')
from GlobalSettings.UI.global_settings_window import Ui_dialog_global_settings
from GlobalSettings.UI.add_steam_account_window import Ui_dialog_add_steam_account

sys.path.append('src')
from models import *
from settings import *

class AddSteamAccountWindow(Ui_dialog_add_steam_account, qtw.QDialog):
    account_created = qtc.Signal(arguments=["account_name", "password"])
    def __init__(self) -> None:
        self.account_created.emit()
        self.accepted.connect(self.process_steam_account)


class AccountsModel(qtg.QStandardItemModel):
    def __init__(self, accounts: list[AccountModel]) -> None:
        super().__init__()

        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Account name", "Region"])

        for account in accounts:
            self.add_account(account)

    def add_account(self, account: AccountModel) -> None:
        row = self.rowCount()

        for column in range(2):
            item = qtg.QStandardItem()
            if column == 0:
                item.setText(account.username)
            else:
                item.setText(account.region)

            self.setItem(row, column, item)

class GlobalSettingsWindow(qtw.QDialog, Ui_dialog_global_settings):
    """
    Isolated sandbox for modifying settings, will only emit a signal for the updated settings once the user has pressed `OK`.

    Once the user has pressed `OK`, it will emit a callback signal with the new `GlobalSettings` object.
    """
    get_settings = qtc.Signal()
    set_settings = qtc.Signal()

    def __init__(self, parent: qtc.QObject | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.dialog = qtw.QFileDialog(self)
        self.dialog.setFileMode(qtw.QFileDialog.FileMode.Directory)

        #set the settings as None for now for better type hinting
        self.settings: GlobalSettings | None = None

        #slot handling
        self.listwidget_page_selector.itemPressed.connect(self.set_page)

        self.treeView.pressed.connect(self.set_remove_enabled)
        self.pb_remove_account.clicked.connect(self.remove_selected_account)

        self.pb_instances_file_dialog.clicked.connect(lambda: self.handle_folder_dialog("Instances Folder", self.le_instances))
        self.pb_mods_file_dialog.clicked.connect(lambda: self.handle_folder_dialog("Mods Folder", self.le_mods))

        self.accepted.connect(self.handle_accepted_dialog)

    #=============#
    #SETUP METHODS#
    #=============#

    def setup_features(self) -> None:
        #check for update on start
        self.cb_update_on_start.setChecked(self.settings.features.check_for_update_on_start)

        #folders
        self.le_instances.setText(self.format_folder_path(self.settings.features.instances_folder))
        self.le_mods.setText(self.format_folder_path(self.settings.features.mods_folder))

        #mode
        if self.settings.features.mode == Mode.USE_SYSTEM_SETTING: self.cb_mode.setCurrentIndex(0)
        elif self.settings.features.mode == Mode.LIGHT: self.cb_mode.setCurrentIndex(1)
        elif self.settings.features.mode == Mode.DARK: self.cb_mode.setCurrentIndex(2)

    def setup_accounts(self) -> None:
        self.accounts_model = AccountsModel(self.settings.accounts)
        self.treeView.setModel(self.accounts_model)

        #by default no account is selected, so we can't remove an account
        self.pb_remove_account.setEnabled(False)
        
    #=====#
    #SLOTS#
    #=====#

    @qtc.Slot()
    def set_page(self) -> None:
        if self.listwidget_page_selector.currentItem().text() == "Features":
            self.stackedWidget.setCurrentIndex(0)
        elif self.listwidget_page_selector.currentItem().text() == "Accounts":
            self.stackedWidget.setCurrentIndex(1)

    @qtc.Slot()
    def handle_folder_dialog(self, title: str, line_edit: qtw.QLineEdit) -> None:
        self.dialog.setWindowTitle(title)

        if os.path.isdir(line_edit.text()):
            self.dialog.setDirectory(os.path.abspath(line_edit.text()))
        else:
            self.dialog.setDirectory(os.getcwd())

        if self.dialog.exec():
            folder = self.dialog.selectedFiles()[0]
            line_edit.setText(self.format_folder_path(folder))

    @qtc.Slot()
    def set_remove_enabled(self) -> None:
        if self.treeView.currentIndex().row() == -1:
            self.pb_remove_account.setEnabled(False)
        else:
            self.pb_remove_account.setEnabled(True)

    @qtc.Slot()
    def remove_selected_account(self) -> None:
        if self.treeView.currentIndex().row() != -1:
            self.treeView.model().removeRow(self.treeView.selectedIndexes()[0].row())
            if self.treeView.currentIndex().row() == -1: self.pb_remove_account.setEnabled(False)

    @qtc.Slot()
    def handle_accepted_dialog(self) -> None:
        #dump features
        if self.cb_mode.currentIndex() == 0: mode = Mode.USE_SYSTEM_SETTING
        elif self.cb_mode.currentIndex() == 1: mode = Mode.LIGHT
        elif self.cb_mode.currentIndex() == 2: mode = Mode.DARK

        features = FeaturesModel(
            mode=mode,
            instances_folder=self.le_instances.text(),
            mods_folder=self.le_mods.text(),
            check_for_update_on_start=self.cb_update_on_start.isChecked()
        )

        #accounts are already dumped as we cannot get password info from the UI

        self.settings.set_features(features)
        self.set_settings.emit()

    #=============#
    #MISCELLANEOUS#
    #=============#

    def format_folder_path(self, path: str) -> str:
        rel_path = os.path.relpath(path)
        if rel_path.startswith('.'):
            return os.path.abspath(rel_path)
        else:
            return rel_path
        
    def exec(self, index: int) -> int:
        """
        Overrides the `QDialog` exec method so we can set the current page to the inputted item and so we can request the `GlobalSettings` object.
        """
        self.get_settings.emit()

        self.setup_features()
        self.setup_accounts()

        self.stackedWidget.setCurrentIndex(index)
        self.listwidget_page_selector.setCurrentRow(index)

        return super().exec()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    global_settings = GlobalSettings()
    global_settings.set_accounts([AccountModel(username="heeheeheehaw", password="no", region="UK"), AccountModel(username="no", password="yes", region="UK")])
    global_settings.dump_settings()

    window = GlobalSettingsWindow(global_settings, 1)
    window.show()

    sys.exit(app.exec())