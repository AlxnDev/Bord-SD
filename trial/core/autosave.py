from PyQt6.QtCore import QTimer

class AutoSave:

    def __init__(self,window,interval=5000):
        self.window=window
        self.timer=QTimer()
        self.timer.timeout.connect(self.save_all)
        self.timer.start(interval)

    def save_all(self):
        for i in range(self.window.tabs.count()):
            ed=self.window.tabs.widget(i)
            if ed.path:
                open(ed.path,"w",encoding="utf-8").write(ed.toPlainText())