name="☀️LightMode"
def run(app):
    app.menuBar().addAction(name,lambda:app.setStyleSheet("" if app.styleSheet() else "QWidget{background:gray;color:white}"))