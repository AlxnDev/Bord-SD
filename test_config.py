import os

def test_base_dir_exists():
    # Este test solo verifica que el código puede identificar su directorio raíz
    from bord_pro import BASE_DIR
    assert BASE_DIR is not None
    assert os.path.exists(os.path.dirname(BASE_DIR))
