name="Duplicate"
def run(app):
    app.menuBar().addAction(name,lambda:app.current().insertPlainText(app.current().toPlainText()))