import subprocess
import re
from utils.path import KITTY_CONFIG


def apply_kitty_palette(palette: dict) -> bool:
    if not KITTY_CONFIG.exists():
        print("Default way of kitty config not found!")
        return False

    with KITTY_CONFIG.open("r") as f:
        config_kitty = f.read()

    kt = palette["kitty"]

    simple_key = {
        "cursor": kt["cursor"],
        "foreground": kt["foreground"],
        "background": kt["background"],
        "selection_foreground": kt["selection_foreground"],
        "selection_background": kt["selection_background"]
    }

    for key, value in simple_key.items():
        pattern = re.compile(rf"^{re.escape(key)}\s+.*$", re.MULTILINE)
        config_kitty = pattern.sub(f"{key} {value}", config_kitty)

    for i in range(16):
        key = f"color{i}"
        value = kt["colors"][key]

        pattern = re.compile(rf"^{key}\s+.*$", re.MULTILINE)
        config_kitty = pattern.sub(f"{key} {value}", config_kitty)

    with KITTY_CONFIG.open("w") as f:
        f.write(config_kitty)

    subprocess.run(["kitty", "@", "set-colors", "--all", "--configured", KITTY_CONFIG])
    return True
