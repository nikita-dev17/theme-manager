import shutil
from .path import USER_THEME_DIR, COLOR_CSS


def create_dirs():
    if not USER_THEME_DIR.exists():
        print(f"Create folder 'theme-manager' on this way: {USER_THEME_DIR}")
        USER_THEME_DIR.mkdir(parents=True, exist_ok=True)

    if not COLOR_CSS.exists():
        print(f"Create color.css for waybar on this way: {COLOR_CSS}")
        COLOR_CSS.touch(exist_ok=True)


def clear_current_theme():
    if USER_THEME_DIR.exists():
        shutil.rmtree(USER_THEME_DIR)

    USER_THEME_DIR.mkdir(parents=True, exist_ok=True)
    COLOR_CSS.touch(exist_ok=True)
