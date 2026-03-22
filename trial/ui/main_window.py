import sys,os,time,json
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from editors.text_editor import TextEditor
from core.autosave import AutoSave
from core.plugin_system import PluginSystem
from core.document_manager import DocumentManager

# ---------- CONFIG ----------
cfg=json.load(open("config.json"))

LIMIT=30
FILE="config.ini"

def start():
    if not os.path.exists(FILE):
        json.dump({"t":time.time()},open(FILE,"w"))
    return json.load(open(FILE))["t"]

days=LIMIT-int((time.time()-start())/86400)

app=QApplication(sys.argv)

APP="Bord Trial"
VER="0.3.21.72"
CRE="RockyDev, Inc"
REL="2026-02-27"
BUI="21.72000"
UPDATE="https://www.github.com/RockyDevFT/Bord/updates.json"
LICENCE="Not Actived"

# ---------- EXPIRE CHECK ----------
if days<=0:
    QMessageBox.critical(None,"Info","Trial Expired: Shop The Pro Version")
    QMessageBox.critical(None,"Info","support to rockydevft@gmail.com")
    sys.exit()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(f'{cfg["name"]} Trial — {days} días')
        self.resize(1080,600)

        self.tabs=QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        self.setCentralWidget(self.tabs)

        self.build_menu()
        self.build_sidebar()
        self.new_tab()

        self.autosave=AutoSave(self)
        self.plugins=PluginSystem(self)
        self.plugins.load()
        self.docs=DocumentManager(self)

    def build_menu(self):

        bar=self.menuBar()

        file=bar.addMenu("📘Archivo")
        file.addAction("📃Nuevo",self.new_tab)
        file.addAction("📂Abrir",self.open_file)
        file.addAction("📁Guardar",self.save_file)
        file.addAction("📜Guardar Proyecto",self.save_project)
        file.addAction("❌Cerrar App",self.close)

        helpm=bar.addMenu("About❓")
        helpm.addAction("App",self.about)
        helpm.addAction("Version",self.about_v2)
        helpm.addAction("Release",self.about_v4)
        helpm.addAction("Build",self.about_v5)
        helpm.addAction("Creator",self.about_v3)
        helpm.addAction("Update",self.about_v6)
        helpm.addAction("LICENCE",self.about_v7)

    def build_sidebar(self):

        dock=QDockWidget("Documentos",self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea,dock)

        self.doc_list=QListWidget()
        dock.setWidget(self.doc_list)

        self.doc_list.itemClicked.connect(self.switch_doc)
        self.tabs.currentChanged.connect(self.refresh_docs)

    def refresh_docs(self):
        self.doc_list.clear()
        for i in range(self.tabs.count()):
            self.doc_list.addItem(self.tabs.tabText(i))

    def switch_doc(self,item):
        self.tabs.setCurrentIndex(self.doc_list.row(item))

    def current(self):
        return self.tabs.currentWidget()

    def new_tab(self):
        ed=TextEditor()
        self.tabs.addTab(ed,"Nuevo")
        self.tabs.setCurrentWidget(ed)
        self.refresh_docs()

    def open_file(self):

        path,_=QFileDialog.getOpenFileName(
            self,"Abrir","","Markdown (*.md);;Git (*.git)"
        )
        if not path:return

        try:
            text=open(path,"r",encoding="utf-8").read()
        except:
            QMessageBox.warning(self,"Error","No se pudo abrir")
            return

        ed=TextEditor()
        ed.setText(text)
        ed.path=path

        self.tabs.addTab(ed,os.path.basename(path))
        self.tabs.setCurrentWidget(ed)
        self.refresh_docs()

    def save_file(self):

        ed=self.current()
        if not ed:return

        if not ed.path:
            self.save_as()
            return

        open(ed.path,"w",encoding="utf-8").write(ed.toPlainText())

    def save_as(self):

        ed=self.current()
        if not ed:return

        path,_=QFileDialog.getSaveFileName(
            self,"Guardar","","Markdown (*.md);;Git (*.git)"
        )
        if not path:return

        ed.path=path
        self.save_file()

        self.tabs.setTabText(
            self.tabs.currentIndex(),
            os.path.basename(path)
        )
      
    def save_file(self):

        ed=self.current()
        if not ed:return

        if not ed.path:
            self.save_as()
            return

        open(ed.path,"w",encoding="utf-8").write(ed.toPlainText())

    def save_project(self):

        ed=self.current()
        if not ed:return

        path,_=QFileDialog.getSaveFileName(
            self,"Guardar","","Bord Project (*.bdp)"
        )
        if not path:return

        ed.path=path
        self.save_file()

        self.tabs.setTabText(
            self.tabs.currentIndex(),
            os.path.basename(path)
        )

   # def open_project(self):

        path,_=QFileDialog.getOpenFileName(
            self,"Abrir","","Bord Project (*.bdp)"
        )
        if not path:return

        try:
            text=open(path,"r",encoding="utf-8").read()
        except:
            QMessageBox.warning(self,"Error","No se pudo abrir")
            return

        ed=TextEditor()
        ed.setText(text)
        ed.path=path

        self.tabs.addTab(ed,os.path.basename(path))
        self.tabs.setCurrentWidget(ed)
        self.refresh_docs()

  #  def export_pdf(self):

        ed=self.current()
        if not ed:return

        from core.pdf_exporter import PDFExporter

        path,_=QFileDialog.getSaveFileName(
            self,"Exportar PDF","","PDF (*.pdf)"
        )
        if not path:return

        PDFExporter.export(ed,path)

   # def open_pdf(self):

        ed=self.current()
        if not ed:return

        from core.open_pdf import OpennedPDF

        path,_=QFileDialog.getOpenFileName(
            self,"Abrir PDF","","PDF (*.pdf)"
        )
        if not path:return

        OpennedPDF.open(ed,path)

    def close_tab(self,i):

        ed=self.tabs.widget(i)

        if ed.toPlainText().strip():
            r=QMessageBox.question(self,"Exit","¿Salir?")
            if r==QMessageBox.StandardButton.Yes:
                self.tabs.setCurrentIndex(i)
                self.save_file()

        self.tabs.removeTab(i)
        self.refresh_docs()

    def about(self):
        QMessageBox.information(self,"About",f"{APP}")

    def about_v2(self):
        QMessageBox.information(self,"About",f"{VER}")

    def about_v3(self):
        QMessageBox.information(self,"About",f"{CRE}")

    def about_v4(self):
        QMessageBox.information(self,"About",f"{BUI}")

    def about_v5(self):
        QMessageBox.information(self,"About",f"{REL}")

    def about_v6(self):
        QMessageBox.information(self,"About",f"{UPDATE}")

    def about_v7(self):
        QMessageBox.information(self,"About",f"{LICENCE}")

    def close(self):
        self.destroy()