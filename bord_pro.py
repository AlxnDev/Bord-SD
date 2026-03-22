from core.app import run

run()

BASE_DIR = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)