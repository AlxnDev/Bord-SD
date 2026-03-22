name="Reverse"
def run(app):
    app.menuBar().addAction(name,lambda:app.current().setPlainText(app.current().toPlainText()[::-1]))