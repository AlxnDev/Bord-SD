class DocumentManager:

    def __init__(self,window):
        self.window=window

    def list_docs(self):
        docs=[]
        for i in range(self.window.tabs.count()):
            ed=self.window.tabs.widget(i)
            docs.append(ed.path or "Sin guardar")
        return docs