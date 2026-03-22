from PyQt6.QtGui import QTextDocument
from PyQt6.QtPrintSupport import QPrinter

class PDFExporter:

    @staticmethod
    def export(editor,path):

        printer=QPrinter()
        printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
        printer.setOutputFileName(path)

        doc=QTextDocument()
        doc.setHtml(editor.toHtml())
        doc.print(printer)