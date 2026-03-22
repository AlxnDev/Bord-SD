import os
import sys

# 1. Primero definimos la ruta base para que esté disponible siempre
BASE_DIR = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)

# 2. Luego importamos lo demás
from core.app import run

# 3. Y SOLO ejecutamos la app si abrimos el archivo directamente
if __name__ == "__main__":
    run()
