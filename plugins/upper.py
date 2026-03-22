name="Mayuscle"
Protected=True

def run(app):
    app.menuBar().addAction(name,lambda:app.current().setPlainText(app.current().toPlainText().upper()))