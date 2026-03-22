name="⬆️Last Version"
protected=True

def run(app):
    def check():
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(app,"Updater","Check https://www.github.com/RockyDevFT/Bord-Pro/release On GitHub")
    app.menuBar().addAction("⬆️Last Version",check)