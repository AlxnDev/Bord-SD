name="TrimLines"
def run(app):
    app.menuBar().addAction(name,lambda:app.current().setPlainText("\n".join(l.strip() for l in app.current().toPlainText().splitlines())))