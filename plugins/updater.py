name="⬆️Last Version"
protected=True

def run(app):
    def check():
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(app,"Updater","Check https://www.github.com/RockyDevFT/Bord-Pro/releaseds On GitHub")
    app.menuBar().addAction("Search Updates",check)