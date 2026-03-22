name="LineNumbers"
def run(app):
    def go():
        lines=app.current().toPlainText().splitlines()
        app.current().setPlainText("\n".join(f"{i+1}: {l}" for i,l in enumerate(lines)))
    app.menuBar().addAction(name,go)