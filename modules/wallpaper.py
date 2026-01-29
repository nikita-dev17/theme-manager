import subprocess
from utils.path import USER_THEME_DIR


def apply_wallpaper(theme: str) -> bool:
    subprocess.run([
        "swww", "img",
        str(USER_THEME_DIR / f"{theme}.gif"),
        "--transition-type", "any",
        "--transition-duration", "0.5"
    ])
    return True
