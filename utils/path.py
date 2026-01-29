from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent # main.py

ASSETS_THEMES_DIR = BASE_DIR / "assets" / "themes"  # папка готовых тем
USER_THEME_DIR = Path.home() / ".config" / "theme-manager"  # дир текущей темы

# modules
FASTFETCH_CONFIG = Path.home() / ".config" / "fastfetch" / "config.jsonc" # конфиг фастфетча
CAVA_CONFIG = Path.home() / ".config" / "cava" / "config" # конфиг cava
SWAY_CONFIG = Path.home() / ".config" / "sway" / "config" # конфиг sway
KITTY_CONFIG = Path.home() / ".config" / "kitty" / "kitty.conf" # конфиг kitty
WAYBAR_STYLE = Path.home() / ".config" / "waybar" / "sway" / "style.css" # стили waybar
COLOR_CSS = Path.home() / ".config" / "theme-manager" / "color.css"
