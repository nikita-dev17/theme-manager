import shutil
import tomllib

from .path import USER_THEME_DIR, ASSETS_THEMES_DIR
from .files import clear_current_theme
from modules.fastfetch import apply_fastfetch_palette
from modules.cava import apply_cava_palette
from modules.wallpaper import apply_wallpaper
from modules.sway import apply_sway_palette
from modules.kitty import apply_kitty_palette
from modules.waybar import apply_waybar_palette


def apply_theme(theme: str):
    chosen_theme = ASSETS_THEMES_DIR / theme
    if not chosen_theme.exists():
        print("Theme not found!")
        return

    clear_current_theme()
    shutil.copytree(chosen_theme, USER_THEME_DIR, dirs_exist_ok=True)

    palette_path = USER_THEME_DIR / "palette.toml"
    if not palette_path.exists():
        print("palette.toml not found in theme")
        return

    try:
        with palette_path.open("rb") as f:
            palette = tomllib.load(f)
    except tomllib.TOMLDecodeError as e:
        print(f"Palette syntax error: {e}")
        return

    steps = [
        ("wallpaper", apply_wallpaper, theme),
        ("sway", apply_sway_palette, palette),
        ("waybar", apply_waybar_palette, palette),
        ("kitty", apply_kitty_palette, palette),
        ("cava", apply_cava_palette, palette),
        ("fastfetch", apply_fastfetch_palette, palette),
    ]

    for name, fn, arg in steps:
        try:
            result = fn(arg)
        except Exception as e:
            print(f"[ERROR] {name} crashed: {e}")
            continue

        if result:
            print(f"[OK] {name} successfully applied")